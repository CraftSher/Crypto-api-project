import sys
from colorama import Fore, Style, init
from utils import get_top_coins

# Инициализация colorama для работы на всех платформах
init(autoreset=True)

def display_coins(coins_data):
    """
    Красиво выводит данные о монетах в консоль.
    """
    if not coins_data:
        print(f"{Fore.RED}Нет данных для отображения.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Топ криптовалют по рыночной капитализации:{Style.RESET_ALL}\n")

    # Форматирование для выравнивания колонок
    headers = ["№", "Название", "Символ", "Цена (USD)", "Рыночная капит.", "Изменение 1ч", "Изменение 24ч", "Изменение 7д"]
    col_widths = [len(h) for h in headers] # Инициализируем ширину по заголовкам

    # Вычисляем максимальную ширину для каждой колонки
    for i, _ in enumerate(headers):
        for idx, coin in enumerate(coins_data):
            if i == 0: # №
                col_widths[i] = max(col_widths[i], len(str(idx + 1)))
            elif i == 1: # Название
                col_widths[i] = max(col_widths[i], len(str(coin.get('name', 'N/A'))))
            elif i == 2: # Символ
                col_widths[i] = max(col_widths[i], len(str(coin.get('symbol', 'N/A').upper())))
            elif i == 3: # Цена (USD)
                col_widths[i] = max(col_widths[i], len(f"{coin.get('current_price', 0):,.2f}"))
            elif i == 4: # Рыночная капит.
                col_widths[i] = max(col_widths[i], len(f"{coin.get('market_cap', 0):,.0f}"))
            elif i == 5: # Изменение 1ч
                val = coin.get('price_change_percentage_1h_in_currency')
                col_widths[i] = max(col_widths[i], len(f"{val:.2f}%" if val is not None else "N/A"))
            elif i == 6: # Изменение 24ч
                val = coin.get('price_change_percentage_24h_in_currency')
                col_widths[i] = max(col_widths[i], len(f"{val:.2f}%" if val is not None else "N/A"))
            elif i == 7: # Изменение 7д
                val = coin.get('price_change_percentage_7d_in_currency')
                col_widths[i] = max(col_widths[i], len(f"{val:.2f}%" if val is not None else "N/A"))


    # Выводим заголовки
    header_line = " | ".join([f"{h:<{col_widths[idx]}}" for idx, h in enumerate(headers)])
    print(f"{Fore.BLUE}{Style.BRIGHT}{header_line}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{'-' * (sum(col_widths) + len(headers) * 3 - 3)}{Style.RESET_ALL}") # Разделитель

    # Выводим данные
    for i, coin in enumerate(coins_data):
        price_1h = coin.get('price_change_percentage_1h_in_currency')
        price_24h = coin.get('price_change_percentage_24h_in_currency')
        price_7d = coin.get('price_change_percentage_7d_in_currency')

        # Определяем цвет для процентных изменений
        color_1h = Fore.GREEN if price_1h is not None and price_1h >= 0 else Fore.RED
        color_24h = Fore.GREEN if price_24h is not None and price_24h >= 0 else Fore.RED
        color_7d = Fore.GREEN if price_7d is not None and price_7d >= 0 else Fore.RED

        # Форматирование значений
        name = coin.get('name', 'N/A')
        symbol = coin.get('symbol', 'N/A').upper()
        current_price = f"{coin.get('current_price', 0):,.2f}" if coin.get('current_price') is not None else "N/A"
        market_cap = f"{coin.get('market_cap', 0):,.0f}" if coin.get('market_cap') is not None else "N/A"

        row_data = [
            f"{i + 1:<{col_widths[0]}}",
            f"{name:<{col_widths[1]}}",
            f"{symbol:<{col_widths[2]}}",
            f"{current_price:<{col_widths[3]}}",
            f"{market_cap:<{col_widths[4]}}",
            f"{color_1h}{f'{price_1h:.2f}%' if price_1h is not None else 'N/A':<{col_widths[5]}}{Style.RESET_ALL}",
            f"{color_24h}{f'{price_24h:.2f}%' if price_24h is not None else 'N/A':<{col_widths[6]}}{Style.RESET_ALL}",
            f"{color_7d}{f'{price_7d:.2f}%' if price_7d is not None else 'N/A':<{col_widths[7]}}{Style.RESET_ALL}"
        ]

        print(" | ".join(row_data))

    print(f"\n{Fore.GREEN}Данные успешно загружены и отображены.{Style.RESET_ALL}")


if __name__ == "__main__":
    print(f"{Fore.YELLOW}Попытка получить данные о криптовалютах...{Style.RESET_ALL}")
    # Получаем топ-15 монет в долларах США
    top_coins = get_top_coins(vs_currency="usd", per_page=15)

    if top_coins:
        display_coins(top_coins)
    else:
        print(f"{Fore.RED}Не удалось получить данные о криптовалютах. Проверьте соединение и повторите попытку.{Style.RESET_ALL}")
        sys.exit(1) # Выход с кодом ошибки