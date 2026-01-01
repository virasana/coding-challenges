import logging
from typing import Iterable, List, Mapping, Any
from dataclasses import dataclass
from pathlib import Path
import csv
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@dataclass
class Product:
    id: str = ""
    name: str = ""
    price: float = 0.00
    quantity: int = 0
    error: str | None = None

def create_product(row: Mapping[str, Any]) -> Product:
    product = Product()
    try:
        # Assign fields
        product.id = str(row['id']).strip()
        product.name = str(row['name']).strip()
        product.price = round(float(row['price']), 2)
        product.quantity = int(row['quantity'])

        # Validate mandatory string fields
        if not product.id or not product.name:
            raise ValueError("Mandatory field id or name is empty")

        return product
    except Exception as e:
        product.error = f"Could not create product from args: row={row}. {e}"
        return product

def parse_all_files_lazy(file_paths: List[str]) -> Iterable[Product]:
    for file_path in file_paths:
        yield from parse_file_path(file_path)

def parse_file_path(file_path: str) -> Iterable[Product]:
    extension = Path(file_path).suffix
    parsers = {
        '.csv': parse_csv,
        '.txt': parse_txt,
        '.json': parse_json
    }
    if extension in parsers:
        yield from parsers[extension](file_path)
    else:
        logger.warning(f"Extension not supported for file_path. Skipping: {file_path}")

def parse_txt(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter=';', fieldnames=['id', 'name', 'price', 'quantity'])
        for row in reader:
            yield create_product(row)

def parse_csv(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield create_product(row)

def parse_json(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for row in data:
            yield create_product(row)

if __name__ == '__main__':
    file_paths = [
        str(file_path)
        for file_path in Path(__file__).parent.glob('intel_data_parse_data*')
    ]

    for product in parse_all_files_lazy(file_paths):
        if product.error:
            logger.error(product.error)
        else:
            logger.debug(product)
