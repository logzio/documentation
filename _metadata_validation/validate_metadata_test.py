import logging
import os
import unittest

import validate_metadata


class TestValidateMetadata(unittest.TestCase):
    PATH_PREFIX = '_metadata_validation/test/'
    VALID_FILE_PATH = '_metadata_validation/test/valid-sample.md'
    ID_VALUE = 'sample'
    TITLE_VALUE = 'Sample Document'
    OVERVIEW_VALUE = 'this is the description of a test'
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
        self.assertFalse(validate_metadata.is_valid_product('[\'logs\', \'metrics\', \'invalid\']'))

    def test_is_valid_product_invalid_value_type(self):
        self.assertFalse(validate_metadata.is_valid_product('[\'logs\', 2, \'invalid\']'))

    def test_is_valid_filters(self):
        self.assertTrue(validate_metadata.is_valid_filters(self.FILTERS_VALUE))

    def test_is_valid_filters_empty_array(self):
        self.assertTrue(validate_metadata.is_valid_filters('[]'))

    def test_is_valid_filters_empty_field(self):
        self.assertFalse(validate_metadata.is_valid_filters(''))

    def test_is_valid_filters_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_filters(42))

    def test_is_valid_filters_invalid_value_type(self):
        self.assertFalse(validate_metadata.is_valid_filters('[\'aws\', 1, \'cloud\']'))

    def test_is_valid_logo(self):
        self.assertTrue(validate_metadata.is_valid_logo(self.LOGO_VALUE))

    def test_is_valid_logo_empty(self):
        self.assertFalse(validate_metadata.is_valid_logo(''))

    def test_is_valid_logo_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_logo(37))

    def test_is_valid_logo_invalid_url(self):
        self.assertFalse(validate_metadata.is_valid_logo('htps://docs.logz.io/images/logo/logz-symbol.svg'))

    def test_is_valid_logo_ping_error(self):
        self.assertFalse(validate_metadata.is_valid_logo('http://httpstat.us/500'))

    def test_is_valid_bundle(self):
        self.assertTrue(validate_metadata.is_valid_bundle(self.LOGS_ALERTS_VALUE, validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_is_valid_bundle_empty_array(self):
        self.assertTrue(validate_metadata.is_valid_bundle('[]', validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_is_valid_bundle_empty_field(self):
        self.assertFalse(validate_metadata.is_valid_bundle('', validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_is_valid_bundle_invalid_type(self):
        self.assertFalse(validate_metadata.is_valid_bundle(33, validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_is_valid_bundle_invalid_field(self):
        self.assertFalse(validate_metadata.is_valid_bundle('invalid', validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_is_valid_bundle_invalid_field_value(self):
        self.assertFalse(validate_metadata.is_valid_bundle('[\'hello\', \'world\', 3]', validate_metadata.consts.FIELD_LOGS_ALERTS))

    def test_get_files_to_ids(self):
        files_to_ids = validate_metadata.get_files_to_ids()
        print(files_to_ids)
        self.assertTrue(len(files_to_ids), 4)

    def test_get_changed_files(self):
        changed_set = f'{self.PATH_PREFIX}valid-sample.md'
        os.environ[validate_metadata.consts.ENV_FILES_TO_TRACK] = changed_set
        changed_files = validate_metadata.get_changed_files()
        self.assertEqual(len(changed_files), 1)
        self.assertEqual(changed_files[0], changed_set)

    def test_get_changed_files_empty(self):
        os.environ[validate_metadata.consts.ENV_FILES_TO_TRACK] = ''
        changed_files = validate_metadata.get_changed_files()
        self.assertEqual(len(changed_files), 0)

    def test_get_file_metadata(self):
        file_metadata = validate_metadata.get_file_metadata(f'{self.PATH_PREFIX}valid-sample.md')
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_ID], self.ID_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_TITLE], self.TITLE_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_OVERVIEW], self.OVERVIEW_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_PRODUCT], self.PRODUCT_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_OS], self.OS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_FILTERS], self.FILTERS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_LOGO], self.LOGO_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_LOGS_ALERTS], self.LOGS_ALERTS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_LOGS_DASHBOARD], self.LOGS_DASHBOARDS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_LOGS_2_METRICS], self.LOGS2METRICS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_METRICS_ALERTS], self.METRICS_ALERTS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_METRICS_DASHBOARDS], self.METRICS_DASHBOARDS_VALUE)
        self.assertEqual(file_metadata[validate_metadata.consts.FIELD_DROP_FILTER], self.DROP_FILTERS_VALUE)

    def test_validate_changed_files(self):
        os.environ[validate_metadata.consts.ENV_FILES_TO_TRACK] = f'{self.PATH_PREFIX}valid-sample.md'
        with self.assertRaises(SystemExit) as cm:
            validate_metadata.validate_changed_files()
        self.assertEqual(cm.exception.code, 0)

    def test_validate_changed_files_invalid_file(self):
        os.environ[validate_metadata.consts.ENV_FILES_TO_TRACK] = f'{self.PATH_PREFIX}invalid-missing-field.md'
        with self.assertRaises(SystemExit) as cm:
            validate_metadata.validate_changed_files()
        self.assertEqual(cm.exception.code, 1)

    def test_validate_changed_files_missing_seperator(self):
        os.environ[validate_metadata.consts.ENV_FILES_TO_TRACK] = f'{self.PATH_PREFIX}invalid-missing-seperator.md'
        with self.assertRaises(SystemExit) as cm:
            validate_metadata.validate_changed_files()
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
