import csv
import pandas as pd
from sqlalchemy import Integer, String, Date, Time, Float
from sqlalchemy.orm import Session

from app.database.session import engine
from app.settings.settings import BASE_DIR

# make sure all SQL Alchemy models are imported (app.database.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
from app.database import base  # noqa: F401


def init_db(db: Session) -> None:
    init_customers()
    init_products()
    init_orders()


def init_customers():
    with open(f'{BASE_DIR}/dataset/customer.csv', mode="r") as f:
        reader = csv.DictReader(f)
        columns = ['customer_id', 'home_store', 'customer_first_name', 'customer_email', 'customer_since',
                   'loyalty_card_number', 'birthdate', 'gender', 'birth_year']
        df = pd.DataFrame(data=reader, columns=columns)

    try:
        types = {
            'customer_id': Integer,
            'home_store': Integer,
            'customer_first_name': String,
            'customer_email': String,
            'customer_since': Date,
            'loyalty_card_number': String,
            'birthdate': Date,
            'gender': String,
            'birth_year': Integer
        }
        with engine.begin() as connection:
            df.to_sql('customers', index=False, con=connection, if_exists='replace', dtype=types)
            print('Done, ok!')
    except Exception as e:
        print(e)


def init_products():
    with open(f'{BASE_DIR}/dataset/product.csv', mode="r") as f:
        reader = csv.DictReader(f)
        columns = ['product_id', 'product_group', 'product_category', 'product_type', 'product',
                   'product_description']
        df = pd.DataFrame(data=reader, columns=columns)

    try:
        types = {
            'product_id': Integer,
            'product_group': String,
            'product_category': String,
            'product_type': String,
            'product': String,
            'product_description': String,
        }
        with engine.begin() as connection:
            df.to_sql('products', index=False, con=connection, if_exists='replace', dtype=types)
            print('Done, ok!')
    except Exception as e:
        print(e)


def init_orders():
    with open(f'{BASE_DIR}/dataset/sales_reciepts.csv', mode="r") as f:
        reader = csv.DictReader(f)
        columns = ["transaction_id", "transaction_date", "transaction_time", "sales_outlet_id",
                   "staff_id", "customer_id", "instore_yn", "order", "line_item_id", "product_id",
                   "quantity", "line_item_amount", "unit_price", "promo_item_yn"]
        df = pd.DataFrame(data=reader, columns=columns)

    try:
        types = {
            'transaction_id': Integer,
            'transaction_date': Date,
            'transaction_time': Time,
            'sales_outlet_id': Integer,
            'staff_id': Integer,
            'customer_id': Integer,
            'instore_yn': String,
            'order': Integer,
            'line_item_id': Integer,
            'product_id': Integer,
            'quantity': Integer,
            'line_item_amount': Float,
            'unit_price': Float,
            'promo_item_yn': String,
        }
        with engine.begin() as connection:
            df.to_sql('orders', index=False, con=connection, if_exists='replace', dtype=types)
            print('Done, ok!')
    except Exception as e:
        print(e)
