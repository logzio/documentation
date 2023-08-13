import ast
import json
import logging
import os
import sys
import urllib.parse

import consts

# set logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s line:%(lineno)d %(levelname)s - %(message)s')
logger = logging.getLogger()


def run():
    manifest_path = os.getenv(consts.ENV_MANIFEST_PATH, consts.DEFAULT_MANIFEST_PATH)
    manifest_object = get_manifest()
    try:
        update_manifest(manifest_object, manifest_path)
    except Exception as e:
        logger.fatal(f'Could not update manifest: {e}')
        exit(1)
    logger.info(f'New manifest successfully generated at {manifest_path}')


def get_manifest():
    shipping_path_prefix = os.getenv(consts.ENV_SHIPPING_PATH_PREFIX, consts.DEFAULT_SHIPPING_PATH_PREFIX)
    manifest_object = {consts.FIELD_COLLECTORS: [], consts.FIELD_AVAILABLE_FILTERS: []}
    shipping_paths = get_file_paths(shipping_path_prefix)
    logger.info(f'Handling the following paths: {shipping_paths}')
    for file_path in shipping_paths:
        collector_item = get_collector_item_from_file(file_path)
        manifest_object[consts.FIELD_COLLECTORS].append(collector_item)
        for tag in collector_item[consts.FIELD_FILTER_TAGS]:
            if tag not in manifest_object[consts.FIELD_AVAILABLE_FILTERS]:
                manifest_object[consts.FIELD_AVAILABLE_FILTERS].append(tag)
    return manifest_object


def get_file_paths(path_prefix):
    md_files = []

    for root, _, files in os.walk(path_prefix):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
            else:
                logger.info(f'Ignoring file {file}')

    return md_files


def get_collector_item_from_file(file_path):
    separator = '---'
    separator_appearances = 2
    key_index = 0
    value_index = 1
    line_number = 0
    collector_item = {}
    link_prefix = os.getenv(consts.ENV_LINK_PREFIX, consts.DEFAULT_LINK_PREFIX)
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
                if norm_key == consts.FIELD_BUNDLES:
                    if consts.FIELD_BUNDLES in collector_item:
                        collector_item[norm_key] = collector_item[norm_key] + norm_val
                        continue
                collector_item[norm_key] = norm_val
            except KeyError as ke:
                logger.warning(ke)
            except Exception as e:
                logger.error(e)
        file_encode = urllib.parse.quote(file_path)
        collector_item[consts.FIELD_LINK] = f'{link_prefix}{file_encode}'
        return collector_item


def normalize_key_val(key, val):
    is_valid_key = False
    norm_key = key.strip().lower()
    if norm_key in consts.MD_TO_MANIFEST_KEYS:
        norm_key = consts.MD_TO_MANIFEST_KEYS[norm_key]
        is_valid_key = True
    norm_val = val.strip()
    if norm_key in consts.ARRAY_KEYS or norm_key in consts.BUNDLE_META:
        norm_val = ast.literal_eval(norm_val)
    if norm_key in consts.BUNDLE_META:
        is_valid_key = True
        return normalize_bundle_item(norm_key, norm_val)
    if norm_key == consts.FIELD_PRODUCT_TAGS:
        return normalize_product_types(norm_key, norm_val)
    if not is_valid_key:
        raise KeyError(f'Specified key {key} not in list of supported keys')
    return norm_key, norm_val


def normalize_bundle_item(norm_key, id_arr):
    bundles = []
    bundle_type = consts.META_TO_BUNDLE_TYPE[norm_key]
    for item_id in id_arr:
        bundles.append({consts.FIELD_BUNDLES_TYPE: bundle_type, consts.FIELD_BUNDLES_ID: item_id})
    return consts.FIELD_BUNDLES, bundles


def normalize_product_types(key, tags_arr):
    norm_tags = []
    for tag in tags_arr:
        try:
            norm_tags.append(consts.DOCS_TO_OBJ_PRODUCT_TYPE[tag.strip()])
        except KeyError:
            logger.error(f'Specified product type {tag} is not supported. Skipping.')
    return key, norm_tags


def update_manifest(manifest_object, manifest_path):
    try:
        logger.info('converting manifest to JSON...')
        manifest_json = json.dumps(manifest_object)
    except TypeError as te:
        raise TypeError(f'Could not convert manifest to JSON due to TypeError: {te}')

    try:
        with open(manifest_path, 'w') as manifest_file:
            manifest_file.write(manifest_json)
    except (FileNotFoundError, PermissionError, OSError) as e:
        raise Exception(f'Could not convert manifest to JSON: {e}')


if __name__ == '__main__':
    run()
