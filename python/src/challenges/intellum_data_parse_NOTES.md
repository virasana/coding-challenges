# Notes for the intellum job prep "data parsing" challenge

## Tasks

### Set up logging
This does it on the instance - don't set up basic congig statically
```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
```

### Load all file paths from disk

Using a list comprehension with pathlib.Path, __file__, .glob

```python
file_paths = [str(path) for path in pathlib.Path(__file__).parent.glob("intellum_data_parse_data*")]
```

