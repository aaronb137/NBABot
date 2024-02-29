from datetime import datetime
from dateutil import parser
import pytz


def get_today_date():
    today = datetime.today()
    formatted_date = today.strftime("%B %d, %Y")

    return formatted_date


def utc_to_pst(game):
    gametime_utc = (
        parser.parse(game["gameTimeUTC"])
        .replace(tzinfo=datetime.utc)
        .astimezone(tz=None)
    )

    pacific_timezone = pytz.timezone("America/Los_Angeles")
    pacific_datetime = gametime_utc.astimezone(pacific_timezone)

    return pacific_datetime.strftime("%Y-%m-%d %I:%M %p %Z")
