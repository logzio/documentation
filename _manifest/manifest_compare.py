import json
import os
from deepdiff import DeepDiff
import consts

GENERATED_MANIFEST_PATH = os.getenv(consts.ENV_MANIFEST_PATH, consts.DEFAULT_MANIFEST_PATH)
TEST_MANIFEST_PATH = os.getenv(consts.ENV_TEST_MANIFEST_PATH, consts.DEFAULT_TEST_MANIFEST_PATH)


def compare_manifests():
    with open(GENERATED_MANIFEST_PATH) as generated_manifest_file, open(TEST_MANIFEST_PATH) as test_manifest_file:
        generated_manifest = json.load(generated_manifest_file)
        test_manifest = json.load(test_manifest_file)
        diff = DeepDiff(generated_manifest, test_manifest)
        if len(diff) == 0:
            print('Manifest looks good!\n')
            exit(0)
        else:
            print('Found differences between the manifests :( Please check your PR\n')
            print('=============================\n')
            print(diff)
            print('\n=============================')
            exit(1)


compare_manifests()
