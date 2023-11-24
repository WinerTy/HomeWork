import requests
import json
from config import keys

class APIException(Exception):        
    pass


class CurrencyConverter:                    
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = keys[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена")

        try:
            quote_key = keys[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена")

        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        try:
            r = requests.get(f"https://v6.exchangerate-api.com/v6/21f06fdeca94bec898957a26/latest/{base_key}")     #https://currate.ru/#list API
            r.raise_for_status()
            resp = r.json()

        except requests.RequestException as e:
            raise APIException(f"Ошибка при запросе к API: {e}")
        except ValueError as e:
            raise APIException(f"Ошибка при обработке ответа API: {e}")

        try:
            new_price = resp['conversion_rates'][quote_key] * amount
        except KeyError as e:
            raise APIException(f"Ошибка при получении курса валюты: {e}")

        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message
