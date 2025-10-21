
--- 

<div align="center">
    <img src="radon.webp" alt="Radon" style="width:260px;">
</div>

--- 

# Radon Transaction Fetch

A simple template for sharing "Transaction Fetchers" for a range of accounts.


Transaction Fetchers are functions that accept a `start_date`, an `end_date` and a `currency` and return a
list of objects in the original provider format.

Parsing and transforming transactions into a standardised format is handled elsewhere.
Fetchers simply fetch transactions in their original format for a given date range and currency.

#### Simplifying assumption for paginated APIs
When dealing with paginated APIs, please fetch the maximum number of transactions allowable per call.
Do not worry about implementing the logic of fetching each page. If the number of transactions for a given 
range exceeds what can be fetched in a single API call, throw an error.
It is up to the caller to limit the range fetched with each call.

#### Self-documenting code
Where possible, comments describing how the fetcher code could be customised are
appreciated. For example, if additional filter parameters are available for an API call, you might include these
as commented out lines. If your API code filters for a value from a limited set of values,
include the possible values in a comment. This is only for "bonus points" and where you feel the additional info
could be of use to future users of the function.

## Quickstart

```sh
git clone git@github.com:b93de3d/radon-transaction-fetch.git
cd radon-transaction-fetch
cp example_config.json config.json
python example_fetcher.py # Run the example
```

## Develop your own fetcher
```sh
cp example_fetcher.py my_fetcher.py
```
Open `my_fetcher.py` and add your fetcher code to the `fetch_range` method.

```py
class MyFetcher(Fetcher):
    def fetch_range(
        self, start_date: datetime, end_date: datetime, currency: str
    ) -> List[Dict]:
        """
        :param start_date: Python datetime object
        :param end_date: Python datetime object
        :param currency: ISO Currency String
        :return: Array of provider transaction objects in original provider format
        """
        # TODO: Implement transaction fetching
        return []
```

Test it out:
```sh
python my_fetcher.py
```
