from datetime import datetime
from typing import List, Dict


class Fetcher:

    def __init__(self):
        super().__init__()

    def fetch_range(
        self, start_date: datetime, end_date: datetime, currency: str
    ) -> List[Dict]:
        """
        :param start_date: Python datetime object
        :param end_date: Python datetime object
        :param currency: ISO Currency String
        :return: Array of provider transaction objects in original provider format
        """
        raise NotImplemented
