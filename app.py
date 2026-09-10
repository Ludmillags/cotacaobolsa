"""Aplicação desktop para consulta de cotações em BRL."""

import tkinter as tk
from tkinter import messagebox

import requests

API_URL = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
TIMEOUT_SECONDS = 10


def format_brl(value: str, decimals: int = 2) -> str:
    """Converte um valor numérico da API para formato monetário brasileiro."""
    number = float(value)
    formatted = f"{number:,.{decimals}f}"
    return "R$ " + formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def fetch_quotes() -> dict:
    """Consulta a API e retorna as três cotações utilizadas pela interface."""
    response = requests.get(API_URL, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()

    return {
        "Dólar (USD)": format_brl(data["USDBRL"]["bid"]),
        "Euro (EUR)": format_brl(data["EURBRL"]["bid"]),
        "Bitcoin (BTC)": format_brl(data["BTCBRL"]["bid"]),
    }


def update_quotes() -> None:
    """Atualiza a interface e informa falhas sem encerrar o programa."""
    status_label.config(text="Consultando cotações...")
    root.update_idletasks()

    try:
        quotes = fetch_quotes()
    except (requests.RequestException, KeyError, ValueError) as error:
        status_label.config(text="Não foi possível atualizar as cotações.")
        messagebox.showerror(
            "Erro na consulta",
            "Não foi possível consultar a API neste momento.\n"
            "Verifique sua conexão e tente novamente.\n\n"
            f"Detalhe técnico: {error}",
        )
        return

    result = "\n".join(f"{currency}: {value}" for currency, value in quotes.items())
    quotes_label.config(text=result)
    status_label.config(text="Cotações atualizadas com sucesso.")


root = tk.Tk()
root.title("Cotação de Moedas")
root.geometry("460x330")
root.resizable(False, False)

container = tk.Frame(root, padx=28, pady=26)
container.pack(fill="both", expand=True)

header = tk.Label(container, text="Cotação de Moedas", font=("Segoe UI", 18, "bold"))
header.pack(anchor="w")

subtitle = tk.Label(
    container,
    text="Consulte Dólar, Euro e Bitcoin em relação ao Real brasileiro.",
    font=("Segoe UI", 10),
    wraplength=390,
    justify="left",
)
subtitle.pack(anchor="w", pady=(6, 18))

update_button = tk.Button(
    container,
    text="Atualizar cotações",
    command=update_quotes,
    font=("Segoe UI", 10, "bold"),
    padx=16,
    pady=8,
)
update_button.pack(anchor="w")

quotes_label = tk.Label(
    container,
    text="Clique no botão para consultar as cotações.",
    font=("Segoe UI", 12),
    justify="left",
)
quotes_label.pack(anchor="w", pady=(22, 12))

status_label = tk.Label(container, text="Aguardando consulta.", font=("Segoe UI", 9))
status_label.pack(anchor="w")

root.mainloop()
