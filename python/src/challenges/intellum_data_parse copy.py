
import pathlib
import logging
from typing import List, Any, Dict, Iterable, TypedDict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def parse_all_files_lazy(file_paths: List[str]) -> Iterable[Product]:
    pass

if __name__ == "__main__":
    file_paths = [str(path) for path in pathlib.Path(__file__).parent.glob("intellum_data_parse_data*")]
    logger.info(file_paths)

    parse_all_files(file_paths)