from datetime import datetime
from typing import List, Dict


class Fetcher:

    def __init__(self):
        super().__init__()

    def fetch_range(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        raise NotImplemented
