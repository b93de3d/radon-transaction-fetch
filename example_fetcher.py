from datetime import datetime
from typing import List, Dict

from base_fetcher import Fetcher
from config import CONFIG


class ExampleFetcher(Fetcher):

    def __init__(self):
        """
        Add whatever config is needed to config.json then load config into fetcher at init
        """
        super().__init__()

        self._api_url = CONFIG["EXAMPLE_API_URL"]
        self._api_key = CONFIG["EXAMPLE_API_KEY"]

    def _dummy_api_call(self):
        """
        Add whatever other functions are needed as private methods
        """
        print("DUMMY API CALL TO:", self._api_url)
        return [
            {"type": "CREDIT", "amount": 52.40, "currency": "EUR"},
            {"type": "DEBIT", "amount": 4.45, "currency": "EUR"},
            {"type": "DEBIT", "amount": 42, "currency": "EUR"},
            {"type": "CREDIT", "amount": 40.52, "currency": "EUR"},
            {"type": "CREDIT", "amount": 2.45, "currency": "EUR"},
            {"type": "DEBIT", "amount": 25.44, "currency": "EUR"},
            {"type": "DEBIT", "amount": 400, "currency": "EUR"},
        ]

    def fetch_range(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        return self._dummy_api_call()


if __name__ == "__main__":

    example_fetcher = ExampleFetcher()
    data = example_fetcher.fetch_range(datetime(2025, 1, 1), datetime(2025, 1, 15))
    print(f"FETCHED DATA FOR RANGE:")
    for d in data:
        print("  -->", d)
