from datetime import datetime
from pathlib import Path

import google.auth
import googleapiclient.discovery
from google_calender.protocols import Event


class GoogleCalender:
    """Google Calender"""

    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    def __init__(self, credentials: Path, calender_id: str) -> None:
        gapi_creds = google.auth.load_credentials_from_file(credentials, self.SCOPES)[0]
        # APIと対話するためのResourceオブジェクトを構築する
        self.service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=gapi_creds
        )
        self.calender_id = calender_id

    def get_events(self, start_time: datetime, end_time: datetime) -> list[Event]:
        event_list = (
            self.service.events()
            .list(
                calendarId=self.calender_id,
                timeMin=start_time.isoformat() + "Z",
                timeMax=end_time.isoformat() + "Z",
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = event_list.get("items", [])

        return [
            Event(
                title=event.get("summary", ""),
                start_time=event["start"].get("dateTime", event["start"].get("date")),
                end_time=event["end"].get("dateTime", event["end"].get("date")),
            )
            for event in events
        ]
