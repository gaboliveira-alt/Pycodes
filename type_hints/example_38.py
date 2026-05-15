import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypedDict, TypeIs, cast

from utils import cyan_print, sep_print


class ProductDict(TypedDict, total=False):
    name: str
    price: int
    stock: int
    url: str


@dataclass
class PyshicalProduct:
    name: str
    price: int
    stock: int


@dataclass
class DigitalProduct:
    name: str
    price: int
    url: str


type Product = PyshicalProduct | DigitalProduct


def load_json_data() -> object:
    database = Path("example_38.json").resolve()

    with database.open("r", enconding="utf-8") as file:
        return json.load(file)


def is_valid_dict(item: object) -> TypeIs[dict[Any, Any]]:
    return isinstance(item, dict)


def is_pyshical_product(item: object) -> TypeIs[ProductDict]:
    if not is_valid_dict(item):
        return False

    has_str_name = isinstance(item.get("name"), str)
    has_numeric_price = isinstance(item.get("price"), int | float)
    has_int_stock = isinstance(item.get("stock"), int)
    has_no_url = not item.get("url")

    return has_str_name and has_numeric_price and has_int_stock and has_no_url


def is_digital_product(item: object) -> TypeIs[ProductDict]:
    if not is_valid_dict(item):
        return False

    has_str_name = isinstance(item.get("name"), str)
    has_numeric_price = isinstance(item.get("price"), int | float)
    has_str_url = isinstance(item.get("url"), str)
    has_no_stock = not item.get("stock")

    return has_str_name and has_numeric_price and has_str_url and has_no_stock


def parse_api_products(api_data: object) -> list[Product]:
    assert isinstance(api_data, Iterable)

    api_data = cast("Iterable[dict[str, Any]]", api_data)
    parsed_products: list[Product] = []

    for item in api_data:
        if is_pyshical_product(item):
            product = PyshicalProduct(
                name=item["name"], price=item["price"], stock=item["stock"]
            )
            parsed_products.append(product)
            continue

        if is_digital_product(item):
            product = DigitalProduct(
                name=item["name"], price=item["price"], url=item["url"]
            )
            parsed_products.append(product)
            continue

        cyan_print("Not a valid product")
        cyan_print(item)

    return parsed_products


if __name__ == "__main__":
    sep_print()

    data = load_json_data()
    parsed_products = parse_api_products(data)

    sep_print()

    for product in parsed_products:
        if isinstance(product, PyshicalProduct):
            cyan_print("Fisico:", product.name, product.price, product.stock)
        if isinstance(product, DigitalProduct):
            cyan_print("Digital:", product.name, product.price, product.url)

    sep_print()
