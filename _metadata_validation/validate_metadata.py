import ast
import logging
import os
import re
import requests
import sys

import consts

# set logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s line:%(lineno)d %(levelname)s - %(message)s')
logger = logging.getLogger()


def validate_changed_files():
    error_counter = 0
    changed_files = get_changed_files()
    if len(changed_files) == 0:
        logger.error('Could not find changed files, exiting')
        exit(1)
    logger.info(f'Files to scan: {changed_files}')
    files_to_unique_fields = get_files_to_unique_fields()
    if len(files_to_unique_fields) == 0:
        logger.error('Cannot get files ids to compare id uniqueness, exiting')
        exit(1)
    for file in changed_files:
        try:
            file_metadata = get_file_metadata(file)
        except Exception as e:
            logger.error(f'Could not get metadata for file {file}: {e}... Is your file structured properly with seperators? ')
            error_counter += 1
            continue
        if len(file_metadata) < len(consts.REQUIRED_FIELDS):
            logger.info(f'Current metadata for file {file}: {file_metadata}')
            logger.error(f'File {file} is missing some required fields')
            print_missing_fields(file_metadata)
            error_counter += 1
            continue
        errors = check_valid_unique_fields(file, file_metadata, files_to_unique_fields)
        error_counter += errors
        if not is_valid_overview(file_metadata[consts.FIELD_OVERVIEW]):
            logger.error(f'Invalid overview for file {file}')
            error_counter += 1
        if not is_valid_product(file_metadata[consts.FIELD_PRODUCT]):
            logger.error(f'Invalid product for file {file}')
            error_counter += 1
        if not is_valid_os(file_metadata[consts.FIELD_OS]):
            logger.error(f'Invalid os for file {file}')
            error_counter += 1
        if not is_valid_filters(file_metadata[consts.FIELD_FILTERS]):
            logger.error(f'Invalid filters for file {file}')
            error_counter += 1
        if not is_valid_logo(file_metadata[consts.FIELD_LOGO]):
            logger.error(f'Invalid logo for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_DASHBOARD], consts.FIELD_LOGS_DASHBOARD):
            logger.error(f'Invalid logs dashboard for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_ALERTS], consts.FIELD_LOGS_ALERTS):
            logger.error(f'Invalid logs alerts for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_2_METRICS], consts.FIELD_LOGS_2_METRICS):
            logger.error(f'Invalid logs2metrics for file: {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_METRICS_DASHBOARDS], consts.FIELD_METRICS_DASHBOARDS):
            logger.error(f'Invalid metrics dashboard for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_METRICS_ALERTS], consts.FIELD_METRICS_ALERTS):
            logger.error(f'Invalid metrics alerts for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_DROP_FILTER], consts.FIELD_DROP_FILTER):
            logger.error(f'Invalid drop filter for file {file}')
            error_counter += 1

    if error_counter == 0:
        logger.info(f'Good job, scanned files are valid!')
        exit(0)
    else:
        logger.error(f'Found {error_counter} validation violations in scanned files. See this run\'s previous '
                     f'logs for more details')
        exit(1)


def print_missing_fields(file_metadata):
    missing_fields = []
    for required_field in consts.REQUIRED_FIELDS:
        if required_field not in file_metadata:
            missing_fields.append(required_field)
    logger.error(f'Missing required fields: {missing_fields}')


def get_changed_files():
    files_str = os.getenv(consts.ENV_FILES_TO_TRACK, '')
    if files_str == '':
        return []
    files_str = files_str.replace(' ', '')
    files_arr = files_str.split(',')
    files_to_track = []
    for file in files_arr:
        docs_path = os.getenv(consts.ENV_DOCS_PREFIX, consts.DOCS_PATH)
        if file.startswith(docs_path):
            files_to_track.append(file)
    return files_to_track


def get_files_to_unique_fields():
    file_to_id_arr = []
    docs_path = os.getenv(consts.ENV_DOCS_PREFIX, consts.DOCS_PATH)
    files_paths = get_file_paths(docs_path)
    id_regex = r"^id: *.+$"
    title_regex = r"^title: *.+$"
    for path in files_paths:
        id = ''
        title = ''
        with open(path) as current_file:
            for line in current_file:
                stripped_line = line.strip()
                if id != '' and title != '':
                    break
                tmp_id = is_field_match_regex(stripped_line, id_regex)
                if tmp_id != '':
                    id = tmp_id
                    continue
                tmp_title = is_field_match_regex(stripped_line, title_regex)
                if tmp_title != '':
                    title = tmp_title
                    continue
            file_to_id_arr.append({consts.OBJ_ID: id, consts.OBJ_FILE: path, consts.OBJ_TITLE: title})
    return file_to_id_arr


def is_field_match_regex(stripped_line, regex):
    try:
        if bool(re.match(regex, stripped_line)):
            line_key_val = stripped_line.split(':')
            val = line_key_val[1].strip()
            return val
        return ''
    except Exception as e:
        logger.error(f'Error while trying to match regex {regex} to line {stripped_line}')
        return ''


def get_file_paths(path_prefix):
    md_files = []

    for root, _, files in os.walk(path_prefix):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
            else:
                logger.info(f'Ignoring file {file}')

    return md_files


def get_file_metadata(file_path):
    seperator = '---'
    seperator_counter = 0
    metadata = {}
    iteration = 0
    with open(file_path) as f:
        for line in f:
            iteration += 1
            if iteration == consts.MAX_FIELDS_TO_COVER:
                logger.error(f'Could not find closing seperator ({seperator}) in file {file_path}. Make sure file is '
                             f'structured properly.')
                break
            stripped_line = line.strip()
            if stripped_line == seperator:
                seperator_counter += 1
                continue
            if seperator_counter >= 2:
                break
            line_key_value = stripped_line.split(':')
            key = line_key_value[0].strip()
            value = line_key_value[1].strip()
            if key == consts.FIELD_LOGO:
                if len(line_key_value) > 2:
                    value += f':{line_key_value[2].strip()}'
                else:
                    logger.error('Field logo is not populated or not in a valid url format')
                    continue
            if key not in consts.REQUIRED_FIELDS:
                logger.warning(f'Field {key} not in list of required values... Is it on purpose?')
                continue
            metadata[key] = value
    return metadata


def check_valid_unique_fields(file_path, file_metadata, files_to_unique_fields):
    errors_counter = 0
    check_title = True
    check_id = True
    if not is_type_str(file_metadata[consts.FIELD_ID], consts.FIELD_ID, file_path):
        errors_counter += 1
        check_id = False
    else:
        if file_metadata[consts.FIELD_ID] == '':
            logger.error(f'File {file_path} has an empty ID')
            errors_counter += 1
            check_id = False

    if not is_type_str(file_metadata[consts.FIELD_TITLE], consts.FIELD_TITLE, file_path):
        errors_counter += 1
        check_title = False
    else:
        if file_metadata[consts.FIELD_TITLE] == '':
            logger.error(f'File {file_path} has an empty title')
            errors_counter += 1
            check_title = False

    for compare_file in files_to_unique_fields:
        if check_id:
            if compare_file[consts.OBJ_ID].lower() == file_metadata[consts.FIELD_ID].lower() and \
                    compare_file[consts.OBJ_FILE] != file_path:
                logger.error(f'Files {compare_file[consts.OBJ_FILE]} and {file_path} have the same ID - {file_metadata[consts.FIELD_ID]}')
                errors_counter += 1
        if check_title:
            if compare_file[consts.OBJ_TITLE].lower() == file_metadata[consts.FIELD_TITLE].lower() and \
                    compare_file[consts.OBJ_FILE] != file_path:
                logger.error(f'Files {compare_file[consts.OBJ_FILE]} and {file_path} have the same title - {file_metadata[consts.FIELD_TITLE]}')
                errors_counter += 1
    return errors_counter


def is_type_str(field, field_type_msg, file_path):
    if type(field) is not str:
        logger.error(f'File {file_path}\'s  field {field_type_msg} is not string')
        return False
    return True

def is_valid_overview(overview):
    if type(overview) is not str or overview == '':
        return False
    return True


def is_valid_product(product_str):
    try:
        if type(product_str) is not str:
            logger.error(f'Invalid product type: {product_str}')
            return False
        product_arr = ast.literal_eval(product_str.strip())
        for product in product_arr:
            if type(product) is not str:
                logger.error(f'Invalid value type in product field: {product}')
                return False
            if product.strip() not in consts.PRODUCTS:
                logger.error(f'Invalid value in product field: {product}, valid types are: {consts.PRODUCTS}')
                return False
        return True
    except Exception as e:
        logger.error(f'Error with product field. {e}')
        return False


def is_valid_os(os_str):
    try:
        if type(os_str) is not str:
            logger.error(f'Invalid os type: {os_str}')
            return False
        os_arr = ast.literal_eval(os_str.strip())
        for os_type in os_arr:
            if type(os_type) is not str:
                logger.error(f'Invalid value type in os field: {os_type}')
                return False
            if os_type.strip() not in consts.OS:
                logger.error(f'Invalid value in os field: {os_type}, valid types are: {consts.OS}')
                return False
        return True
    except Exception as e:
        logger.error(f'Error with os field. {e}')
        return False


def is_valid_filters(filters_str):
    try:
        if type(filters_str) is not str:
            logger.error(f'Invalid filters type: {filters_str}')
            return False
        filters_arr = ast.literal_eval(filters_str.strip())
        for filter_type in filters_arr:
            if type(filter_type) is not str:
                logger.error(f'Invalid value in filter field: {filter_type}')
                return False
            if filter_type == '':
                logger.error('Redundant empty value in filter')
                return False
        return True
    except Exception as e:
        logger.error(f'Error with filter field. {e}')
        return False


def is_valid_logo(logo):
    if type(logo) is not str:
        logger.error(f'Invalid type for logo field: {logo}')
        return False
    if logo.strip() == '':
        logger.error('Empty value for logo')
        return False
    link_regex = r"^https?:\/\/[^\s\/$.?#].[^\s]*$"
    match = re.match(link_regex, logo.strip())
    if match is None:
        logger.error(f'Logo is not a valid url: {logo}')
        return False
    try:
        response = requests.get(logo.strip())
        if response.status_code != requests.codes.ok:
            logger.error(f'Got {response.status_code} while trying to ping logo url: {logo}')
            return False
        else:
            return True
    except requests.exceptions.RequestException:
        logger.error(f'Error while trying to ping logo {logo}')
        return False


def is_valid_bundle(bundle_str, bundle_type):
    try:
        if type(bundle_str) is not str:
            logger.error('Invalid type for bundle field: {bundle_str}')
            return False
        bundle_arr = ast.literal_eval(bundle_str.strip())
        for bundle in bundle_arr:
            if type(bundle) is not str:
                logger.error(f'Invalid value in {bundle_type} field: {bundle}')
                return False
            if bundle == '':
                logger.error(f'Redundant empty value in {bundle_type}')
                return False
        return True
    except Exception as e:
        logger.error(f'Error with {bundle_type} field. {e}')
        return False


if __name__ == '__main__':
    validate_changed_files()
