from datetime import datetime

from pydantic import BaseModel


def get_h_m_s(sec: int) -> tuple[int, int, int]:
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return h, m, s


class Event(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime

    @property
    def working_hours(self) -> str:
        td = self.end_time - self.start_time
        h, m, _ = get_h_m_s(td.seconds)
        return f"{str(h).zfill(0)}:{str(m).zfill(0)}"
