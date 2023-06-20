import ast
import json
import logging
import os
import sys

# set logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

LINK_PREFIX = 'https://raw.githubusercontent.com/logzio/documentation/master/'
SHIPPING_PATH_PREFIX = 'docs/shipping/'
MANIFEST_PATH = 'manifest/manifest.json'

FIELD_COLLECTORS = 'collectors'
FIELD_AVAILABLE_FILTERS = 'availableFilters'
FIELD_LINK = 'dataLink'
FIELD_ID = 'id'
FIELD_TITLE = 'title'
FIELD_DESCRIPTION = 'description'
FIELD_LOGO = 'logo'
FIELD_PRODUCT_TAGS = 'productTags'
FIELD_FILTER_TAGS = 'filterTags'
FIELD_OS_TAGS = 'osTags'
FIELD_TAG = 'tag'
FIELD_DISPLAY_NAME = 'displayName'

MD_TO_MANIFEST_KEYS = {
    'id': FIELD_ID,
    'title': FIELD_TITLE,
    'overview': FIELD_DESCRIPTION,
    'logo': FIELD_LOGO,
    'product': FIELD_PRODUCT_TAGS,
    'filters': FIELD_FILTER_TAGS,
    'os': FIELD_OS_TAGS
}

ARRAY_KEYS = [FIELD_PRODUCT_TAGS, FIELD_FILTER_TAGS, FIELD_OS_TAGS]


def run():
    manifest_object = handle_shipping_docs()
    try:
        update_manifest(manifest_object)
    except Exception as e:
        logger.fatal(f'Could not update manifest: {e}')
        exit(1)
    logger.info(f'New manifest successfully generated at {MANIFEST_PATH}')


def handle_shipping_docs():
    manifest_object = {FIELD_COLLECTORS: [], FIELD_AVAILABLE_FILTERS: []}
    shipping_paths = get_file_paths(SHIPPING_PATH_PREFIX)
    logger.info(f'Handling the following paths: {shipping_paths}')
    for file_path in shipping_paths:
        collector_item = get_metadata_from_file(file_path)
        manifest_object[FIELD_COLLECTORS].append(collector_item)
        for tag in collector_item[FIELD_FILTER_TAGS]:
            if tag not in manifest_object[FIELD_AVAILABLE_FILTERS]:
                    manifest_object[FIELD_AVAILABLE_FILTERS].append(tag)
    return manifest_object


def get_file_paths(path_prefix):
    file_names = os.listdir(path_prefix)
    full_paths = []
    for name in file_names:
        full_path = f'{SHIPPING_PATH_PREFIX}{name}'
        full_paths.append(full_path)
    return full_paths


def get_metadata_from_file(file_path):
    separator = '---'
    separator_appearances = 2
    key_index = 0
    value_index = 1
    line_number = 0
    collector_item = {}
    with open(file_path) as doc_file:
        while separator_appearances > 0:
            line = doc_file.readline().strip()
            line_number += 1
            logger.debug(f'Working on line {line_number}: {line}')
            if line == separator:
                separator_appearances -= 1
                continue
            key_val_pair = line.split(':', 1)
            if len(key_val_pair) != 2:
                logger.warning(f'Could not split line {key_val_pair} into a key value pair, ignoring...')
                continue
            if len(key_val_pair[key_index]) == 0:
                logger.error(f'Invalid key in line {line_number}, skipping...')
            try:
                norm_key, norm_val = normalize_key_val(key_val_pair[key_index], key_val_pair[value_index])
                collector_item[norm_key] = norm_val
            except KeyError as ke:
                logger.debug(ke)
            except Exception as e:
                logger.error(e)
        collector_item[FIELD_LINK] = f'{LINK_PREFIX}{file_path}'
        return collector_item



def normalize_key_val(key, val):
    norm_key = key.strip().lower()
    if norm_key in MD_TO_MANIFEST_KEYS:
        norm_key = MD_TO_MANIFEST_KEYS[norm_key]
    else:
        raise KeyError(f'Specified key {key} not in list of supported keys')
    norm_val = val.strip()
    if norm_key in ARRAY_KEYS:
        norm_val = ast.literal_eval(norm_val)
    return norm_key, norm_val


def update_manifest(manifest_object):
    try:
        logger.info('converting manifest to JSON...')
        manifest_json = json.dumps(manifest_object)
        with open(MANIFEST_PATH, 'w') as manifest_file:
            manifest_file.write(manifest_json)
    except Exception as e:
        raise Exception(f'Could not convert manifest to JSON: {e}')


run()
