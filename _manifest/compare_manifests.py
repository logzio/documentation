import json
import os

import consts


def compare():
    current_manifest = ''
    new_manifest = ''
    current_manifest_path = consts.DEFAULT_MANIFEST_PATH
    new_manifest_path = os.getenv(consts.ENV_MANIFEST_PATH)
    if new_manifest_path is None or new_manifest_path == '':
        return 'Could not get current manifest file path'
    with open(current_manifest_path) as cm:
        current_manifest = json.loads(cm.read())
    with open(new_manifest_path) as nm:
        new_manifest = json.loads(nm.read())
    if new_manifest == '' or current_manifest == '':
        return 'Could not open files'
    if current_manifest == new_manifest:
        return 'nodiff'
    else:
        return 'isdiff'


if __name__ == '__main__':
    result = compare()
    print(result)

