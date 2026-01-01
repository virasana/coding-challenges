import logging
from pathlib import Path
from dataclasses import dataclass
from typing import List, Iterable, Any, Callable
import csv
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@dataclass
class Product:
    id: str = ""
    name: str = ""
    price: float = 0.0
    quantity: int = 0
    error: str | None = None

def parse_csv(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield create_product(row)

def parse_txt(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter=';', fieldnames=['id','name','price','quantity'])
        for row in reader:
            yield create_product(row)

def parse_json(file_path: str) -> Iterable[Product]:
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = json.load(f)
        for row in reader:
            yield create_product(row)


PARSERS: dict[str, Callable[[str], Iterable[Product]]] = {
    '.csv': parse_csv,
    '.txt': parse_txt,
    '.json': parse_json
}

def create_product(row: dict[str, Any]) -> Product:
    product = Product()
    try:
        product.id = str(row['id']).strip()
        product.name = str(row['name']).strip()
        product.price = round(float(row['price']), 2)
        product.quantity = int(row['quantity'])
    except Exception as e:
        product.error = f'Could not create product from args. row={row}. {e}'
    
    return product

   
def parse_file_paths(file_paths: List[str]) -> Iterable[Product]:
    for file_path in file_paths:
        file_extension = Path(file_path).suffix

        if not file_extension in PARSERS:
            logger.warning(f'File {file_path} has an unsupported extension.  Skipping this file')
        else:
            yield from PARSERS[file_extension](file_path)

if(__name__ == '__main__'):
    file_paths = [
        str(file_path) 
        for file_path in Path(__file__).parent.glob("intel_data_parse_data*")
    ]

    for product in parse_file_paths(file_paths):
        if product.error:
            logger.error(product)
        else:
            logger.debug(product)
        
    
