from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "8691707413:AAFvIdYvTG2Xy7t_5NQyiYQU7a_JPln_5oQ"
CHAT_ID = "6044514858"

@app.route("/")
def home():

    url = "https://open.er-api.com/v6/latest/USD"

    data = requests.get(url).json()

    rates = data["rates"]

    usd_vnd = round(rates["VND"])
    eur_usd = round(1 / rates["EUR"], 5)
    gbp_usd = round(1 / rates["GBP"], 5)
    usd_jpy = round(rates["JPY"], 3)

    gold_price = "N/A"

    try:
        gold = requests.get(
            "https://api.gold-api.com/price/XAU"
        ).json()

        gold_price = round(
            gold["price"],
            2
        )

    except:
        pass

    date = datetime.now().strftime("%d/%m/%Y")

    message = f"""
📊 BẢN TIN THỊ TRƯỜNG {date}

🏆 Vàng (XAU/USD): {gold_price}
💵 USD/VND: {usd_vnd}
🇪🇺 EUR/USD: {eur_usd}
🇬🇧 GBP/USD: {gbp_usd}
🇯🇵 USD/JPY: {usd_jpy}

📈 Nguồn tham khảo: ForexFactory

👉 Tham gia nhóm: https://t.me/ttadmin68
💬 Trading Time tặng bot miễn phí
"""

    telegram_url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(
        telegram_url,
        data=payload
    )

    return "DONE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)