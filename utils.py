import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

def get_top_coins(vs_currency="usd", per_page=10, page=1):
    """
    Делает GET-запрос к CoinGecko API для получения данных о монетах.

    :param vs_currency: Целевая валюта (например, "usd", "rub").
    :param per_page: Количество монет на страницу (макс. 250).
    :param page: Номер страницы для пагинации.
    :return: Список словарей с данными о монетах, или None в случае ошибки.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    headers = {"accept": "application/json"}

    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc", # Сортировка по рыночной капитализации (убывание)
        "per_page": per_page,
        "page": page,
        "price_change_percentage": "1h,24h,7d" # Включить изменение цены за 1 час, 24 часа и 7 дней
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10) # Добавим таймаут
        response.raise_for_status()  # Вызовет исключение для ошибок HTTP (4xx или 5xx)

        data = response.json()
        return data

    except ConnectionError:
        print("Ошибка: Нет соединения с интернетом или проблемы с DNS.")
        return None
    except Timeout:
        print("Ошибка: Превышено время ожидания ответа от сервера CoinGecko API.")
        return None
    except RequestException as e:
        print(f"Произошла ошибка запроса: {e}")
        return None
    except ValueError:
        print("Ошибка: Не удалось декодировать ответ JSON от CoinGecko API.")
        return None

if __name__ == "__main__":
    # Этот блок кода выполнится только если utils.py запускается напрямую
    # Позволяет быстро протестировать функцию
    print("Тестирование функции get_top_coins()...")
    coins_data = get_top_coins(vs_currency="usd", per_page=5)
    if coins_data:
        print(f"Получено {len(coins_data)} монет:")
        for coin in coins_data:
            print(f"  {coin.get('name')} ({coin.get('symbol').upper()}): {coin.get('current_price')} USD")
    else:
        print("Не удалось получить данные о монетах.")