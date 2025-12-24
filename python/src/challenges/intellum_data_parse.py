import pathlib
import csv
import json
import logging
from typing import TypedDict, Iterable, Dict, Any, List
from decimal import Decimal, ROUND_HALF_UP

# --- Setup logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# --- TypedDict for Product ---
class Product(TypedDict):
    id: str
    name: str
    price: float
    quantity: int

def create_product(id: str, name: str, price: float, quantity: int) -> Product:
    if not id:
        raise ValueError(f"Invalid argument: id={id}")
    if not name:
        raise ValueError(f"Invalid argument: name={name}")
    if price is None:
        raise ValueError(f"Invalid argument: price={price}")
    if quantity is None:
        raise ValueError(f"Invalid argument: quantity={quantity}")
    return {"id": id, "name": name, "price": price, "quantity": quantity}

# --- Generic conversion generator ---
def read_data(rows: Iterable[Dict[str, Any]]) -> Iterable[Product]:
    """
    Lazily converts raw rows from any reader into Product items.
    Skips malformed rows.
    """
    for row in rows:
        try:
            yield create_product(
                id=str(row["id"]),
                name=str(row["name"]),
                price=float(Decimal(row["price"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
                quantity=int(row["quantity"])
            )
        except Exception as e:
            logger.warning(f"Skipping malformed row: {e}, row: {row}")

# --- Parsers ---
def parse_csv(file_path: str) -> Iterable[Product]:
    logger.info(f"Parsing CSV file: {file_path}")
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        yield from read_data(reader)

def parse_txt(file_path: str) -> Iterable[Product]:
    logger.info(f"Parsing TXT file: {file_path}")
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f, delimiter=";", fieldnames=["id", "name", "price", "quantity"])
        yield from read_data(reader)

def parse_json(file_path: str) -> Iterable[Product]:
    logger.info(f"Parsing JSON file: {file_path}")
    with open(file_path, "r") as f:
        data = json.load(f)  # JSON is already a list
        yield from read_data(data)

# --- File dispatcher ---
def parse_file(file_path: str) -> Iterable[Product]:
    extension = pathlib.Path(file_path).suffix
    parsers = {
        ".csv": parse_csv,
        ".txt": parse_txt,
        ".json": parse_json
    }
    parser = parsers.get(extension)
    if parser is None:
        logger.warning(f"Unsupported file extension '{extension}' in file {file_path}")
        return iter([])  # empty iterator
    return parser(file_path)

def parse_all_files_lazy(file_paths: List[str]) -> Iterable[Product]:
    """
    Lazily yields products from all files, one by one.
    """
    for file_path in file_paths:
        logger.info(f"Processing file: {file_path}")
        yield from parse_file(file_path)

# --- Main launcher ---
if __name__ == "__main__":
    file_paths = [
        str(file_path)
        for file_path in pathlib.Path(__file__).parent.glob('intellum_data_parse_data*')
        if file_path.is_file()
    ]

    all_products = parse_all_files_lazy(file_paths)

    # Example: count products without storing them all in memory
    total_count = sum(1 for _ in all_products)
    print(f"Total products: {total_count}")