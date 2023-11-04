import datetime
from pathlib import Path

from google_calender.gcalender import GoogleCalender

CALENDAR_ID = "noguchi_daiki@avilen.co.jp"
GOOGLE_CREDENTIALS_JSON = Path(__file__).parent / "data/google_credentials.json"


def main() -> None:
    gcalender_app = GoogleCalender(GOOGLE_CREDENTIALS_JSON, CALENDAR_ID)
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(days=3)
    events = gcalender_app.get_events(start_time=start_time, end_time=end_time)

    # eventsを表示する
    response = ""
    for event in events:
        response += (
            f"{event.start_time:%Y-%m-%d %H:%M} ~ {event.end_time:%H:%M}"
            f" {event.title}\n"
        )
    response = response.rstrip("\n")
    print(response)
