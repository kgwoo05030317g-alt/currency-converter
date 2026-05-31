from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 나라 이름 -> 통화 코드 매핑
COUNTRY_TO_CURRENCY = {
    "미국": "USD",
    "일본": "JPY",
    "유럽": "EUR",
    "중국": "CNY",
    "영국": "GBP",
    "호주": "AUD",
    "캐나다": "CAD",
    "스위스": "CHF",
    "홍콩": "HKD",
    "싱가포르": "SGD",
    "태국": "THB",
    "말레이시아": "MYR",
    "인도": "INR",
    "러시아": "RUB",
    "브라질": "BRL",
    "멕시코": "MXN",
    "터키": "TRY",
    "뉴질랜드": "NZD",
    "필리핀": "PHP",
    "베트남": "VND",
    "대만": "TWD",
    "인도네시아": "IDR",
}


def fetch_exchange_rate(target_currency: str) -> float:
    """공용 환율 API에서 KRW -> target_currency 환율을 가져옵니다."""
    url = "https://open.er-api.com/v6/latest/KRW"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    if data.get("result") != "success":
        raise ValueError("환율 API에서 유효한 응답을 받지 못했습니다.")

    rates = data.get("rates", {})
    rate = rates.get(target_currency)
    if rate is None:
        raise ValueError(f"환율 정보가 없습니다: {target_currency}")

    return float(rate)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    country = ""

    if request.method == "POST":
        country = request.form.get("country", "").strip()
        if not country:
            error = "나라 이름을 입력해주세요."
        else:
            currency = COUNTRY_TO_CURRENCY.get(country)
            if not currency:
                error = (
                    f"지원하지 않는 나라입니다: {country}. "
                    "예: 미국, 일본, 유럽, 중국, 영국, 호주"
                )
            else:
                try:
                    rate = fetch_exchange_rate(currency)
                    converted = 1000 * rate
                    result = {
                        "country": country,
                        "currency": currency,
                        "rate": rate,
                        "amount_krw": 1000,
                        "converted": converted,
                    }
                except Exception as exc:
                    error = f"환율 정보를 가져오는 중 오류가 발생했습니다: {exc}"

    return render_template(
        "index.html",
        result=result,
        error=error,
        country=country,
        supported_countries=sorted(COUNTRY_TO_CURRENCY.keys()),
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
