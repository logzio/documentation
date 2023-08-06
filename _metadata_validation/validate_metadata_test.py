import logging
import os
import unittest

import validate_metadata


class TestValidateMetadata(unittest.TestCase):
    PATH_PREFIX = '_metadata_validation/test/'
    VALID_FILE_PATH = '_metadata_validation/test/valid-sample.md'
    ID_VALUE = 'sample'
    TITLE_VALUE = 'Sample Document'
    OVERVIEW_VALUE = 'This is a sample document of a test'
    PRODUCT_VALUE = '[\'logs\', \'metrics\']'
    OS_VALUE = '[\'windows\', \'linux\']'
    FILTERS_VALUE = '[\'aws\', \'cloud\']'
    LOGO_VALUE = 'https://docs.logz.io/images/logo/logz-symbol.svg'
    LOGS_DASHBOARDS_VALUE = '[\'dfsdfgsdgfds\', \'sdfgsdfg\', \'hrtgwgs\']'
    LOGS_ALERTS_VALUE = '[\'sdfgs\', \'xcvdb\']'
    LOGS2METRICS_VALUE = '[\'ersefg\']'
    METRICS_DASHBOARDS_VALUE = '[\'sdfgfsdg\', \'sdfgsdyuiuyifg\']'
    METRICS_ALERTS_VALUE = '[\'azxsvb\']'
    DROP_FILTERS_VALUE = '[\'jslijwe\']'

    def setUp(self):
        os.environ[validate_metadata.consts.ENV_DOCS_PREFIX] = self.PATH_PREFIX

    def test_is_valid_id(self):
        files_to_ids = validate_metadata.get_files_to_ids()
        self.assertTrue(validate_metadata.is_valid_id(self.ID_VALUE, self.VALID_FILE_PATH, files_to_ids))

    def test_is_valid_id_id_not_exists(self):
        files_to_ids = validate_metadata.get_files_to_ids()
        self.assertFalse(validate_metadata.is_valid_id('', f'{self.PATH_PREFIX}id-empty.md', files_to_ids))

    def test_is_valid_id_invalid_type(self):
        files_to_ids = validate_metadata.get_files_to_ids()
        self.assertFalse(validate_metadata.is_valid_id(33, f'{self.PATH_PREFIX}id-invalid-type.md', files_to_ids))

    def test_is_valid_id_duplicate_id(self):
        files_to_ids = validate_metadata.get_files_to_ids()
        self.assertFalse(validate_metadata.is_valid_id('sample', f'{self.PATH_PREFIX}id-duplicate.md', files_to_ids))

    def test_is_valid_title(self):
        self.assertTrue(validate_metadata.is_valid_title(self.TITLE_VALUE))

    def test_is_valid_title_empty(self):
        self.assertFalse(validate_metadata.is_valid_title(''))

    def test_is_valid_title_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_title(33))

    def test_is_valid_overview(self):
        self.assertTrue(validate_metadata.is_valid_overview(self.OVERVIEW_VALUE))

    def test_is_valid_overview_empty(self):
        self.assertFalse(validate_metadata.is_valid_overview(''))

    def test_is_valid_overview_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_overview({'hello': 'world'}))

    def test_is_valid_product(self):
        self.assertTrue(validate_metadata.is_valid_product(self.PRODUCT_VALUE))

    def test_is_valid_product_empty_array(self):
        self.assertTrue(validate_metadata.is_valid_product('[]'))

    def test_is_valid_product_empty_field(self):
        self.assertFalse(validate_metadata.is_valid_product(''))

    def test_is_valid_product_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_product(33))

    def test_is_valid_product_invalid_value(self):
        self.assertFalse(validate_metadata.is_valid_product('[\'logs\', \'metrics\', 4]'))


    # def test_get_files_to_ids(self):
    #     files_to_ids = validate_metadata.get_files_to_ids()
    #     print(files_to_ids)
    #     self.assertNotEqual(len(files_to_ids), 0)


if __name__ == '__main__':
    unittest.main()
