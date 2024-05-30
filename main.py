import requests
from pprint import pprint
import json


page = 1
def get_category():
    # URL для запроса к API
    url = f'https://catalog.wb.ru/catalog/bl_shirts/v2/catalog?appType=1&cat=8126&curr=rub&dest=-1257786&page={page}&sort=popular&spp=30'
    headers = {
        'Accept': '*/*',  # Заголовок Accept для запроса
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',  # Язык для Accept-Language
        'Connection': 'keep-alive',  # Заголовок Connection
        'Origin': 'https://www.wildberries.ru',  # Заголовок Origin
        'Referer': 'https://www.wildberries.ru/catalog/podarki/detyam/igrushki',  # Заголовок Referer
        'Sec-Fetch-Dest': 'empty',  # Заголовок Sec-Fetch-Dest
        'Sec-Fetch-Mode': 'cors',  # Заголовок Sec-Fetch-Mode
        'Sec-Fetch-Site': 'cross-site',  # Заголовок Sec-Fetch-Site
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',  # Заголовок User-Agent
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',  # Дополнительный заголовок sec-ch-ua
        'sec-ch-ua-mobile': '?0',  # Дополнительный заголовок sec-ch-ua-mobile
        'sec-ch-ua-platform': 'Windows'  # Дополнительный заголовок sec-ch-ua-platform
    }

    # Отправляем GET-запрос к API и получаем ответ в формате JSON
    response = requests.get(url, headers=headers)
    return response.json()

def prepare_items(response):
    products = []
    products_row = response.get('data', {}).get('products', None)

    # Проверяем, есть ли в ответе продукты и не пустой ли список
    if products_row is not None and len(products_row) > 0:
        # Перебираем каждый продукт
        for product in products_row:
            sizes = []
            # Перебираем размеры продукта
            for size in product.get('sizes', []):
                # Добавляем информацию о размере в список sizes
                sizes.append({
                    'Размер': size.get('name', None),
                    'Цена': size.get('price', {}).get('total', None),
                })

            colors = []
            # Перебираем цвета продукта
            for color in product.get('colors', []):
                # Добавляем информацию о цвете в список colors
                colors.append({
                    'Цвет': color.get('name', None),
                })

            # Добавляем информацию о продукте в список products
            products.append({
                'Артикул': product.get('id', None),
                'Бренд': product.get('brand', None),
                'Название': product.get('name', None),
                'Поставщик': product.get('supplier', None),
                'Рейтинг поставщика': product.get('supplierRating', None),
                'Рейтинг': product.get('rating', None),
                'Отзывы': product.get('feedbacks', None),
                'Фото': product.get('pics', None),
                'Количество отзывов': product.get('feedbacks', None),
                'Текст промо-акции для карточки продукта': product.get('promoTextCard', None),
                'Текст промо-акции для категории продукта': product.get('promoTextCat', None),
                'Объем продукта': product.get('volume', None),
                'Просмотры': product.get('viewFlags', None),
                'Цвета': colors,
                'Размеры': sizes
            })
    return products


def main():
    response = get_category()
    products = prepare_items(response)

    for product in products:
        pprint(f"Артикул: {product['Артикул']}")
        pprint(f"Бренд: {product['Бренд']}")
        pprint(f"Название: {product['Название']}")
        pprint(f"Поставщик: {product['Поставщик']}")
        pprint(f"Рейтинг поставщика: {product['Рейтинг поставщика']}")
        pprint(f"Рейтинг: {product['Рейтинг']}")
        pprint(f"Отзывы: {product['Отзывы']}")
        pprint(f"Фото: {product['Фото']}")
        pprint(f"Количество отзывов: {product['Количество отзывов']}")
        pprint(f"Текст промо-акции для карточки продукта: {product['Текст промо-акции для карточки продукта']}")
        pprint(f"Текст промо-акции для категории продукта: {product['Текст промо-акции для категории продукта']}")
        pprint(f"Объем продукта: {product['Объем продукта']}")
        pprint(f"Просмотры: {product['Просмотры']}")

        pprint("Цвета:")
        for color in product['Цвета']:
            pprint(f"  Цвет: {color['Цвет']}")

        pprint("Размеры:")
        for size in product['Размеры']:
            pprint(
                f"  Размер: {size['Размер']}, Цена: {size['Цена']}")

        print('*' * 50)  # Добавляем пустую строку между каждым продуктом


if __name__ == '__main__':
    main()
