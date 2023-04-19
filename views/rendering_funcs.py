from datetime import datetime


def format_date(iso_date):
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }
    dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    day = dt.strftime("%d")
    month = months[dt.strftime("%m")]
    year = dt.strftime("%Y")
    return f"{day} {month} {year}"