from tkinter import *
from tkinter import ttk
# from tkinter import messagebox as mb
# import requests


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

Button(text="Получить курс").pack(padx=10, pady=15)

result_label = Label(text="", font=("Arial", 12), justify=LEFT)
result_label.pack(padx=10, pady=10)


window.mainloop()