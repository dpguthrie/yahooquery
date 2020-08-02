<p align="center">
    <a href="#"><img src="img/banner_image_2.png"></a>
</p>
<p align="center">
    <em>Python wrapper for an unofficial Yahoo Finance API</em>
</p>
<p align="center">
    <a href="https://travis-ci.com/dpguthrie/yahooquery" target="_blank">
        <img src="https://travis-ci.com/dpguthrie/yahooquery.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/dpguthrie/yahooquery" target="_blank">
        <img src="https://img.shields.io/codecov/c/github/dpguthrie/yahooquery" alt="Coverage">
    </a>
    <a href="https://pypi.org/project/yahooquery" target="_blank">
        <img src="https://badge.fury.io/py/yahooquery.svg" alt="Package version">
    </a>
</p>

---

**Documentation**: <a target="_blank" href="https://dpguthrie.github.io/yahooquery/">https://dpguthrie.github.io/yahooquery/</a>

**Interactive Demo**: <a target="_blank" href="https://yahooquery-streamlit.herokuapp.com">https://yahooquery-streamlit.herokuapp.com</a>

**Source Code**: <a target="_blank" href="https://github.com/dpguthrie/yahooquery">https://github.com/dpguthrie/yahooquery</a>

**Blog Post**: <a target="_blank" href="https://towardsdatascience.com/the-unofficial-yahoo-finance-api-32dcf5d53df">https://towardsdatascience.com/the-unofficial-yahoo-finance-api-32dcf5d53df</a>

---

## Overview

Yahooquery is a python interface to unofficial Yahoo Finance API endpoints.  The package allows a user to retrieve nearly all the data visible via the Yahoo Finance front-end.

Some features of yahooquery:

- **Fast**:  Data is retrieved through API endpoints instead of web scraping.  Additionally, asynchronous requests can be utilized with simple configuration
- **Simple**:  Data for multiple symbols can be retrieved with simple one-liners
- **User-friendly**:  Pandas Dataframes are utilized where appropriate
- **Premium**:  Yahoo Finance premium subscribers are able to retrieve data available through their subscription

## Requirements

Python 2.7, 3.5+

- [Pandas](https://pandas.pydata.org) - Fast, powerful, flexible and easy to use open source data analysis and manipulation tool
- [Requests](https://requests.readthedocs.io/en/master/) - The elegant and simple HTTP library for Python, built for human beings.
- [Requests-Futures](https://github.com/ross/requests-futures) - Asynchronous Python HTTP Requests for Humans
- [Selenium](https://www.selenium.dev/selenium/docs/api/py/) - Web browser automation

!!! info
    Selenium is only utilized to login to Yahoo, which is done when the user passes certain [keyword arguments](guide/ticker/keyword_arguments.md#username-and-password).  Logging into Yahoo enables users who are subscribers to Yahoo Finance Premium to retrieve data only accessible to premium subscribers.

## Installation

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700">
    <span data-ty="input">pip install yahooquery</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully installed yahooquery</span>
    <a href="#" data-terminal-control="">restart ↻</a>
</div>

## Example

The majority of the data available through the unofficial Yahoo Finance API is related to a company, which is represented in yahooquery as a `Ticker`.  You can instantiate the `Ticker` class by passing the company's ticker symbol.  For instance, to get data for :fontawesome-brands-apple:, pass `aapl` as the first argument to the `Ticker` class:

```python
from yahooquery import Ticker

aapl = Ticker('aapl')

aapl.summary_detail
```

## Multple Symbol Example

The `Ticker` class also makes it easy to retrieve data for a list of symbols with the same API.  Simply pass a list of symbols as the argument to the `Ticker` class.

```python
from yahooquery import Ticker

symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

faang = Ticker(symbols)

faang.summary_detail
```

## License

This project is licensed under the terms of the MIT license.
