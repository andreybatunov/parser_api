import requests
from bs4 import BeautifulSoup
from time import sleep
from config import (
    HENDERSON_HEADERS,
    URL_HENDERSON,
    PRODUCT_TAG_HENDERSON,
    PRODUCT_NAME_TAG_HENDERSON,
    PRODUCT_PRICE_TAG_HENDERSON,
    PAGES_HENDERSON,
    SHORT_URL_HENDERSON,
    SDVOR_HEADERS,
    URL_SDVOR,
    PRODUCT_TAG_SDVOR,
    PRODUCT_NAME_TAG_SDVOR,
    PRODUCT_PRICE_TAG_SDVOR,
    PAGES_SDVOR,
    COOKIES,
)
from models import get_db, ParsedData
from fastapi import HTTPException
from dto import DataSchemaOut, DataSchemaIn
import asyncio


class ParserService:
    def __init__(self, site_config):
        self.site_config = site_config
        self._set_config()
        self.db = get_db()

    def _set_config(self):
        if self.site_config == "HENDERSON":
            self.HEADERS = HENDERSON_HEADERS
            self.URL = URL_HENDERSON
            self.PRODUCT_TAG = PRODUCT_TAG_HENDERSON
            self.PRODUCT_NAME_TAG = PRODUCT_NAME_TAG_HENDERSON
            self.PRODUCT_PRICE_TAG = PRODUCT_PRICE_TAG_HENDERSON
            self.PAGES = PAGES_HENDERSON
            self.SHORT_URL = SHORT_URL_HENDERSON
        else:
            self.HEADERS = SDVOR_HEADERS
            self.URL = URL_SDVOR
            self.PRODUCT_TAG = PRODUCT_TAG_SDVOR
            self.PRODUCT_NAME_TAG = PRODUCT_NAME_TAG_SDVOR
            self.PRODUCT_PRICE_TAG = PRODUCT_PRICE_TAG_SDVOR
            self.PAGES = PAGES_SDVOR

    def get_products(self):
        all_products = []
        page = 1
        response = requests.get(self.URL, headers=self.HEADERS, cookies=COOKIES)
        soup = BeautifulSoup(response.text, "lxml")
        if self.PAGES:
            pages = soup.find_all(self.PAGES["tag"], class_=self.PAGES["class_name"])

        while True:
            if self.PAGES:
                print(f"Обработка страницы {page}")
            response = requests.get(self.URL, headers=self.HEADERS, cookies=COOKIES)
            if response.status_code != 200:
                print(f"Ошибка: статус код {response.status_code}")
                break

            soup = BeautifulSoup(response.text, "lxml")

            products = soup.find_all(
                self.PRODUCT_TAG["tag"], class_=self.PRODUCT_TAG["class_name"]
            )

            if not products:
                print("Товары не найдены на странице.")
                break
            for product in products:
                name_elem = product.find(
                    self.PRODUCT_NAME_TAG["tag"],
                    class_=self.PRODUCT_NAME_TAG["class_name"],
                )
                price_elem = product.find(
                    self.PRODUCT_PRICE_TAG["tag"],
                    class_=self.PRODUCT_PRICE_TAG["class_name"],
                )

                name = name_elem.text.strip() if name_elem else "Нет названия"
                price = price_elem.text.strip() if price_elem else "Нет цены"

                all_products.append({"name": name, "price": price})

            if self.PAGES:
                self.URL = self.SHORT_URL + pages[page - 1]["href"]
                page += 1
                if page > len(pages):
                    break
                sleep(1)  # Задержка между запросами
            else:
                break

        return all_products

    async def parse_website(self):
        try:
            products = self.get_products()
            for product in products:
                data = {"name": product["name"], "price": product["price"]}

                existing_item = (
                    self.db.query(ParsedData)
                    .filter(
                        ParsedData.name == data["name"],
                        ParsedData.price == data["price"],
                    )
                    .first()
                )

                if not existing_item:
                    db_item = ParsedData(**data)
                    self.db.add(db_item)
                    self.db.commit()

            self.db.close()

        except Exception as e:
            print(f"Ошибка при парсинге: {str(e)}")

    def get_all_data(self):
        items = self.db.query(ParsedData).all()
        self.db.close()
        return [DataSchemaOut(**item.__dict__) for item in items]

    def get_data(self, item_id: int):
        item = self.db.query(ParsedData).filter(ParsedData.id == item_id).first()
        self.db.close()
        if not item:
            raise HTTPException(status_code=404, detail="Данные не найдены")
        return DataSchemaOut(**item.__dict__)

    def create_data(self, data: DataSchemaIn):
        db_item = ParsedData(**data.model_dump())
        self.db.add(db_item)
        self.db.commit()
        self.db.close()

    def update_data(self, item_id: int, data: DataSchemaIn):
        item = self.db.query(ParsedData).filter(ParsedData.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Данные не найдены")

        item.name = data.name
        item.price = data.price

        result = DataSchemaOut(id=item.id, name=item.name, price=item.price)

        self.db.commit()
        self.db.close()
        return result

    def delete_data(self, item_id: int):
        item = self.db.query(ParsedData).filter(ParsedData.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Данные не найдены")

        self.db.delete(item)
        self.db.commit()
        self.db.close()

    async def run_parser(self):
        while True:
            await self.parse_website()
            await asyncio.sleep(3600)

    async def startup(self):
        asyncio.create_task(self.run_parser())
