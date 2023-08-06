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
    files_to_ids = get_files_to_ids()
    if len(files_to_ids) == 0:
        logger.error('Cannot get files ids to compare id uniqueness, exiting')
        exit(1)
    for file in changed_files:
        file_metadata = get_file_metadata(file)
        if len(file_metadata) < len(consts.REQUIRED_FIELDS):
            logger.info(f'Current metadata for file {file}: {file_metadata}')
            logger.error(f'File {file} is missing some required fields')
            error_counter += 1
            continue
        if not is_valid_id(file_metadata[consts.FIELD_ID], file, files_to_ids):
            logger.error(f'Invalid id for file: {file}')
            error_counter += 1
        if not is_valid_title(file_metadata[consts.FIELD_TITLE]):
            logger.error(f'Invalid title for file {file}')
            error_counter += 1
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
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_DASHBOARD], 'logs dashboards'):
            logger.error(f'Invalid logs dashboard for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_ALERTS], 'logs alerts'):
            logger.error(f'Invalid logs alerts for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_LOGS_2_METRICS], 'logs2metrics'):
            logger.error(f'Invalid logs2metrics for file: {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_METRICS_DASHBOARDS], 'metrics dashboards'):
            logger.error(f'Invalid metrics dashboard for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_METRICS_ALERTS], 'metrics alerts'):
            logger.error(f'Invalid metrics alerts for file {file}')
            error_counter += 1
        if not is_valid_bundle(file_metadata[consts.FIELD_DROP_FILTER], 'drop filter'):
            logger.error(f'Invalid drop filter for file {file}')
            error_counter += 1

    if error_counter == 0:
        logger.info(f'Good job, scanned files are valid!')
        exit(0)
    else:
        logger.error(f'Found {error_counter} validation violations in scanned files. See this run\'s previous '
                     f'logs for more details')
        exit(1)


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


def get_files_to_ids():
    file_to_id_arr = []
    docs_path = os.getenv(consts.ENV_DOCS_PREFIX, consts.DOCS_PATH)
    files_paths = get_file_paths(docs_path)
    id_regex = r"^id: *.+$"
    for path in files_paths:
        with open(path) as current_file:
            for line in current_file:
                stripped_line = line.strip()
                if bool(re.match(id_regex, stripped_line)):
                    line_key_val = stripped_line.split(':')
                    id = line_key_val[1].strip()
                    file_to_id = {consts.OBJ_ID: id, consts.OBJ_FILE: path}
                    file_to_id_arr.append(file_to_id)
                    break
    return file_to_id_arr


def get_file_paths(path_prefix):
    file_names = os.listdir(path_prefix)
    full_paths = []
    index_suffix = 1
    for name in file_names:
        full_path = os.path.join(path_prefix, name)
        if os.path.splitext(full_path)[index_suffix] != '.md':
            logger.info(f'Ignoring file {name}')
            continue
        full_paths.append(full_path)
    return full_paths


def get_file_metadata(file_path):
    seperator = '---'
    seperator_counter = 0
    metadata = {}
    with open(file_path) as f:
        for line in f:
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


def is_valid_id(current_file_id, current_file_path, files_to_ids):
    if current_file_id == '':
        logger.error(f'File {current_file_path} has an empty ID')
        return False
    if type(current_file_id) is not str:
        logger.error(f'File {current_file_path} has an invalid ID type')
        return False
    for doc in files_to_ids:
        if doc[consts.OBJ_ID].lower() == current_file_id.lower() and doc[consts.OBJ_FILE] != current_file_path:
            logger.info(f'Files {doc[consts.OBJ_FILE]} and {current_file_path} have the same ID - {current_file_id}')
            return False
    return True


def is_valid_overview(overview):
    if type(overview) is not str or overview == '':
        return False
    return True


def is_valid_title(title):
    if type(title) is not str or title == '':
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
                logger.error(f'Invalid value in product field: {product}')
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
                logger.error(f'Invalid value in os field: {os_type}')
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
