from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def get_crypto_prices():
    coin1_id = coin1_combobox.get()
    coin2_id = coin2_combobox.get()

    if not coin1_id or not coin2_id:
        mb.showwarning("Внимание", "Выберите две криптовалюты")
        return

    ids = f"{coin1_id},{coin2_id}"
    url = (f"https://api.coingecko.com/api/v3/simple/price"
           f"?ids={ids}&vs_currencies=usd&include_24hr_change=true")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        price1 = data[coin1_id]["usd"]
        change1 = data[coin1_id]["usd_24h_change"]
        price2 = data[coin2_id]["usd"]
        change2 = data[coin2_id]["usd_24h_change"]

        result_text = (
            f"{coin1_id.capitalize()}: ${price1:,.2f}  ({change1:+.2f}%)\n"
            f"{coin2_id.capitalize()}: ${price2:,.2f}  ({change2:+.2f}%)"
        )
        result_label.config(text=result_text)

    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка сети", f"Не удалось получить данные: {e}")
    except KeyError as e:
        mb.showerror("Ошибка данных", f"Монета не найдена: {e}")


window = Tk()
window.title("Курсы криптовалют")
window.geometry("500x300")


crypto_list = [
    "bitcoin",
    "ethereum",
    "solana",
    "cardano",
    "ripple",
    "dogecoin",
    "polkadot",
    "litecoin"
]

Label(text="Выберите первую криптовалюту:").pack(padx=10, pady=5)

coin1_combobox = ttk.Combobox(values=crypto_list, width=30)
coin1_combobox.pack(padx=10, pady=5)
coin1_combobox.set("bitcoin")

Label(text="Выберите вторую криптовалюту:").pack(padx=10, pady=5)

coin2_combobox = ttk.Combobox(values=crypto_list, width=30)
coin2_combobox.pack(padx=10, pady=5)
coin2_combobox.set("ethereum")

Button(text="Получить курс", command=get_crypto_prices).pack(padx=10, pady=15)
result_label = Label(text="", font=("Arial", 12), justify=LEFT)
result_label.pack(padx=10, pady=10)


window.mainloop()