# RN Transaction Fetch

A simple template for sharing "Transaction Fetchers" for a range of accounts.


Transaction Fetchers accept a `start_date`, an `end_date` and a `currency` and return a
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
as commented out lines. If you're API code filters for a value from a limited set of values,
include the possible values in a comment. This is only for "bonus points" and where you feel the additional info
could be of use to future users of the function.

## Quickstart

```sh
git clone ...
cd rn_transaction_fetch
cp example_config.json config.json
python example_fetcher.py # Run the example
```

## Develop your own fetcher
```sh
cp example_fetcher.py my_fetcher.py
```
Open `my_fetcher.py` and add your fetcher code to the `fetch_range` method.

Test it out:
```sh
python my_fetcher.py
```

## Sharing developed fetchers

As fetcher.py files contain potentially sensitive credentials in the `CONFIG` variable, newly developed fetchers should
not be commited to the codebase. Contact us to organise secure transfer of 
