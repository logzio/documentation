import os
import unittest
import consts
import manifest_generator


class ManifestGeneratorTest(unittest.TestCase):
    TEST_MANIFEST_PATH = '_manifest/manifest-from-test.json'
    TEST_SHIPPING_PATH = '_manifest/test/'

    def setUp(self):
        os.environ[consts.ENV_MANIFEST_PATH] = self.TEST_MANIFEST_PATH
        os.environ[consts.ENV_SHIPPING_PATH_PREFIX] = self.TEST_SHIPPING_PATH

    def test_update_manifest(self):
        try:
            manifest_path = os.path.join(os.getcwd(), self.TEST_MANIFEST_PATH)
            manifest_generator.run()
            self.assertTrue(os.path.exists(manifest_path))
            os.remove(manifest_path)
        except Exception as e:
            self.fail(f'Manifest generator encountered an error: {e}')

    def test_get_manifest(self):
        manifest_object = manifest_generator.get_manifest()
        collector_item = manifest_object[consts.FIELD_COLLECTORS][0]
        self.assertEqual(collector_item[consts.FIELD_ID], 'sample')
        self.assertEqual(collector_item[consts.FIELD_TITLE], 'Sample Document')
        self.assertNotIn('sidebar_position', collector_item)
        self.assertEqual(collector_item[consts.FIELD_DESCRIPTION], 'this is the description of a test')
        self.assertCountEqual(collector_item[consts.FIELD_PRODUCT_TAGS], ['logs', 'metrics'])
        self.assertCountEqual(collector_item[consts.FIELD_OS_TAGS], ['windows', 'linux'])
        self.assertCountEqual(collector_item[consts.FIELD_FILTER_TAGS], ['aws', 'cloud'])
        self.assertEqual(collector_item[consts.FIELD_LOGO], 'https://docs.logz.io/images/logo/logz-symbol.svg')
        bundles = [{"type": "OSD_DASHBOARD", "id": "dfsdfgsdgfds"}, {"type": "OSD_DASHBOARD", "id": "sdfgsdfg"},
                   {"type": "OSD_DASHBOARD", "id": "hrtgwgs"}, {"type": "LOG_ALERT", "id": "sdfgs"},
                   {"type": "LOG_ALERT", "id": "xcvdb"}, {"type": "LOGS_TO_METRICS", "id": "ersefg"},
                   {"type": "GRAFANA_DASHBOARD", "id": "sdfgfsdg"}, {"type": "GRAFANA_DASHBOARD", "id": "sdfgsdyuiuyifg"},
                   {"type": "GRAFANA_ALERT", "id": "azxsvb"}]
        self.assertCountEqual(collector_item[consts.FIELD_BUNDLES], bundles)

    def test_normalize_key_val_strings(self):
        valid_keys_strings = [consts.META_ID, consts.META_TITLE, consts.META_OVERVIEW, consts.META_LOGO]

        for key in valid_keys_strings:
            try:
                normalized_key, v = manifest_generator.normalize_key_val(key, 'some value')
                self.assertEqual(normalized_key, consts.MD_TO_MANIFEST_KEYS[key])
                self.assertEqual(type(v), str)
            except Exception as e:
                self.fail(f'Exception was raised for supposed valid key {key}: {e}')

    def test_normalize_key_val_arrays(self):
        valid_keys_arrays = [consts.META_FILTERS, consts.META_OS]
        for key in valid_keys_arrays:
            try:
                normalized_key, v = manifest_generator.normalize_key_val(key, "['one', 'two']")
                self.assertEqual(normalized_key, consts.MD_TO_MANIFEST_KEYS[key])
                self.assertEqual(type(v), list)
            except Exception as e:
                self.fail(f'Exception was raised for supposed valid key {key}: {e}')

    def test_normalize_key_val_bundles(self):
        valid_keys_bundles = [consts.META_LOGS_DASHBOARDS, consts.META_LOGS_ALERTS, consts.META_LOGS_TO_METRICS,
                              consts.META_METRICS_DASHBOARDS, consts.META_METRICS_ALERTS, consts.META_DROP_FILTER]
        for key in valid_keys_bundles:
            try:
                normalized_key, v = manifest_generator.normalize_key_val(key, "['one', 'two']")
                self.assertEqual(normalized_key, consts.FIELD_BUNDLES)
                self.assertEqual(type(v), list)
            except Exception as e:
                self.fail(f'Exception was raised for supposed valid key {key}: {e}')

    def test_normalize_key_val_invalid_key(self):
        invalid_key = 'invalid_key'
        val = 'some value'
        self.assertRaises(KeyError, manifest_generator.normalize_key_val, invalid_key, val)


if __name__ == '__main__':
    unittest.main()
