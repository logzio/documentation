# Manifest generator

This is a python script that maps all shipping documents in the repo, and creates a JSON manifest.

### To use this script manually:

#### 1. Set your working directory

Make sure your current working directory is `documentation`.

#### 2. Run the script

```bash
python3 _manifest/manifest_generator.py
```

### Testing the script

In case any changes were made in the script, you can run the tests to make sure your changes didn't break the script.

```bash
python3 _manifest/manifest_generator_test.py
```


### Changelog:

- **0.0.3**:
  - Set default path for manifest under folder `static`.
- **0.0.2**:
  - Ignore files that aren't `.md`.
- **0.0.1**:
  - Initial release.