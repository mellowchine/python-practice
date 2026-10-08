from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_base1_label(event):
    code = base_combobox1.get()
    base1_label.config(text=currencies[code])


def update_base2_label(event):
    code = base_combobox2.get()
    base2_label.config(text=currencies[code])


def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)


def exchange():
    base1_code = base_combobox1.get()
    base2_code = base_combobox2.get()
    target_code = target_combobox.get()

    if base1_code and base2_code and target_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base1_code}')
            response1.raise_for_status()
            data1 = response1.json()

            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()
            data2 = response2.json()

            rate1 = data1['rates'][target_code]
            rate2 = data2['rates'][target_code]

            name1 = currencies[base1_code]
            name2 = currencies[base2_code]
            target = currencies[target_code]

            mb.showinfo(
                "Курс обмена",
                f"{rate1:.1f} {target} за 1 {name1}\n"
                f"{rate2:.1f} {target} за 1 {name2}"
            )
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите все три валюты")



# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x400")

Label(text="Базовая валюта:").pack(padx=10, pady=5)

base_combobox1 = ttk.Combobox(values=list(currencies.keys()))
base_combobox1.pack(padx=10, pady=5)
base_combobox1.bind("<<ComboboxSelected>>", update_base1_label)

base1_label = ttk.Label()
base1_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)

base_combobox2 = ttk.Combobox(values=list(currencies.keys()))
base_combobox2.pack(padx=10, pady=5)
base_combobox2.bind("<<ComboboxSelected>>", update_base2_label)

base2_label = ttk.Label()
base2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)

target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()