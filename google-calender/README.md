# google-calender

GoogleCalenderから予定を読み取る

## Requirements

- Python 3.10.0
- poetry

### Google Credentials

1. GCP公式サイトからGCPプロジェクトを作成
1. Google Calendar APIを有効にする
    1. [APIとサービス]→[ライブラリ]を選択
    1. 検索窓から「Google Calendar API」を検索し、[有効化]をクリック
1. サービスアカウントを作成する
    1. ナビゲーションメニューから、[IAMと管理]→[サービスアカウント]を選択する
    1. 画面上の[+ サービスアカウントを作成]をクリックする
    1. 説明に沿ってサービスアカウント名などを入力する。（省略可の項目は省略してもOK）
1. サービスアカウントの鍵を作成・配置する
    1. サービスアカウントの画面で、該当のサービスアカウントの[鍵を管理]を選択する
    1. 「JSON」を選択して、鍵を作成する
    1. 作成した鍵(JSON)を`google-calender/google_calender/data`に配置する。ファイル名は`google_credentials.json`とリネームする

## build

`poetry install`

## Usage

### for terminal

`poetry run get-events`

### for Python client

```python
>>> import datetime
>>> from pathlib import Path
>>> from google_calender.gcalender import GoogleCalender
>>> 
>>> CALENDAR_ID = "noguchi_daiki@avilen.co.jp"
>>> GOOGLE_CREDENTIALS_JSON = Path("google_calender/data/google_credentials.json")
>>>
>>> gcalender_app = GoogleCalender(GOOGLE_CREDENTIALS_JSON, CALENDAR_ID)
>>> end_time = datetime.datetime.utcnow()
>>> start_time = end_time - datetime.timedelta(days=3)
>>> events = gcalender_app.get_events(start_time=start_time, end_time=end_time)
>>> from pprint import pprint; pprint(events)
[Event(title='', start_time=datetime.datetime(2023, 11, 1, 17, 30, tzinfo=TzInfo(+09:00)), end_time=datetime.datetime(2023, 11, 1, 20, 0, tzinfo=TzInfo(+09:00))),
 ...
 Event(title='', start_time=datetime.datetime(2023, 11, 3, 22, 0, tzinfo=TzInfo(+09:00)), end_time=datetime.datetime(2023, 11, 3, 22, 30, tzinfo=TzInfo(+09:00))),
 Event(title='', start_time=datetime.datetime(2023, 11, 4, 12, 0, tzinfo=TzInfo(+09:00)), end_time=datetime.datetime(2023, 11, 4, 13, 0, tzinfo=TzInfo(+09:00)))]
```
