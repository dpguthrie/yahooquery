# Keyword Arguments

The `Ticker` class also takes in additional keyword arguments that modify certain behavior.  The majority of the keyword arguments will affect how requests are made.

## Regular

### **asynchronous**

=== "Details"

    - *Description*: When set to `True`, requests made to Yahoo Finance will be made asynchronously
    - *Default*:  `False`
    - *Type*: `bool`

    !!! tip
        Only necessary when you have more than one symbol

=== "Example"

    ```python hl_lines="4"
    symbols = 'fb aapl amzn nflx goog'
    Ticker(
        symbols,
        asynchronous=True
    )
    ```

### **backoff_factor**

=== "Details"

    - *Description*: A factor, in seconds, to apply between attempts after the second try
    - *Default*: `0.3`
    - *Implementation*: `{backoff_factor} * (2 ** ({number of total retries} - 1))`
    - *Example*:  If the backoff factor is 0.1, then `sleep()` will sleep for [0.0s, 0.2s, 0.4s, ...] between retries

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        backoff_factor=1
    )
    ```

### **country**

=== "Details"

    - *Description*: Alter the language, region, and corsDomain that each request utilizes as a query parameter.
    - *Default*: `United States`

    !!! info
        This functionality has not been thoroughly tested as far as comparing data returned for each country.  You will see a difference, though, in the data returned from the `news` method:

    ??? example "View Countries"
        ```python
        {
            'france': {
                'lang': 'fr-FR',
                'region': 'FR',
                'corsDomain': 'fr.finance.yahoo.com'
            },
            'india': {
                'lang': 'en-IN',
                'region': 'IN',
                'corsDomain': 'in.finance.yahoo.com'
            },
            'hong kong': {
                'lang': 'zh-Hant-HK',
                'region': 'HK',
                'corsDomain': 'hk.finance.yahoo.com'
            },
            'germany': {
                'lang': 'de-DE',
                'region': 'DE',
                'corsDomain': 'de.finance.yahoo.com'
            },
            'canada': {
                'lang': 'en-CA',
                'region': 'CA',
                'corsDomain': 'ca.finance.yahoo.com'
            },
            'spain': {
                'lang': 'es-ES',
                'region': 'ES',
                'corsDomain': 'es.finance.yahoo.com'
            },
            'italy': {
                'lang': 'it-IT',
                'region': 'IT',
                'corsDomain': 'it.finance.yahoo.com'
            },
            'united states': {
                'lang': 'en-US',
                'region': 'US',
                'corsDomain': 'finance.yahoo.com'
            },
            'australia': {
                'lang': 'en-AU',
                'region': 'AU',
                'corsDomain': 'au.finance.yahoo.com'
            },
            'united kingdom': {
                'lang': 'en-GB',
                'region': 'GB',
                'corsDomain': 'uk.finance.yahoo.com'
            },
            'brazil': {
                'lang': 'pt-BR',
                'region': 'BR',
                'corsDomain': 'br.financas.yahoo.com'
            },
            'new zealand': {
                'lang': 'en-NZ',
                'region': 'NZ',
                'corsDomain': 'nz.finance.yahoo.com'
            },
            'singapore': {
                'lang': 'en-SG',
                'region': 'SG',
                'corsDomain': 'sg.finance.yahoo.com'
            }
        }
        ```

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        country='France'
    )
    ```

### **formatted**

=== "Details"

    - *Description* - When `formatted=True`, most numerical data from the API will be returned as a dictionary:
    ```python
    "totalCash": {
        "raw": 94051000320
        "fmt": "94.05B"
        "longFmt": "94,051,000,320"
    }
    ```
    When formatted is set to False, an internal method will return the value in the "raw" key.
    - *Default* - `False`
    - *Type* - `bool`

    !!! warning
        When `formatted=True`, all data will be returned as a `dict`

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        formatted=True
    )
    ``` 

### **max_workers**

=== "Details"

    - *Description* - Defines the number of workers used to make asynchronous requests.
    - *Default* - `8`
    - *Type* - `int`

    !!! tip
        This is only relevant when `asynchronous=True`

=== "Example"

    ```python hl_lines="3 4"
    Ticker(
        'aapl',
        asynchronous=True,
        max_workers=4
    )
    ```

### **proxies**

=== "Details"

    - *Description* - Make each request with a proxy.  Simply pass a dictionary, mapping URL schemes to the URL to the proxy.
    - *Default* - `None`
    - *Type* - `dict`

    !!! tip
        You can also configure proxies by setting the environment variables `HTTP_PROXY` and `HTTPS_PROXY`.

=== "Example"

    ```python hl_lines="1 2 3 4 8"
    proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
    }

    Ticker(
        'aapl',
        proxies=proxies
    )
    ```

### **retry**

=== "Details"

    - *Description* - Number of times to retry a failed request
    - *Default* - `5`
    - *Type* - `int`

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        retry=10
    )
    ```

### **status_forcelist**

=== "Details"

    - *Description* - A set of integer HTTP status codes that we should force a retry on.
    - *Default* - `[429, 500, 502, 503, 504]`
    - *Type* - `list`

    !!! tip
        This is especially useful when retrieving historical pricing data for a large amount of symbols.  Currently, Yahoo Finance has been displaying 404 errors for mass download requests.

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        status_forcelist=[404, 429, 500, 502, 503, 504]
    )
    ```

### **timeout**

=== "Details"

    - *Description* - Stop waiting for a response after a given number of seconds
    - *Default* - `5`
    - *Type* - `int`

    !!! note
        This is not a time limit on the entire response download; rather, an exception is raised if the server has not issued a response for timeout seconds (more precisely, if no bytes have been received on the underlying socket for timeout seconds). If no timeout is specified explicitly, requests do not time out.

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        timeout=3
    )
    ```

### **user_agent**

=== "Details"

    - *Description* - A browser's user-agent string that is sent with the headers with each request.
    - *Default* - Random selection from the list below:
    ```python
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    ]
    ```
    - *Type* - `str`

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    )
    ```

### **validate**

=== "Details"

    - *Description* - Validate existence of symbols during instantiation.  Invalid symbols will be dropped but you can view them through the `invalid_symbols` property.
    - *Default* - `False`
    - *Type* - `bool`

=== "Example"

    ```python hl_lines="7 10"
    from yahooquery import Ticker

    symbols = 'fb facebook aapl apple amazon amzn netflix nflx goog alphabet'

    t = Ticker(
        symbols,
        validate=True)
    print(t.symbols)
    ['NFLX', 'GOOG', 'AAPL', 'FB', 'AMZN']
    print(t.invalid_symbols)
    ['FACEBOOK', 'AMAZON', 'APPLE', 'NETFLIX', 'ALPHABET']
    ```

### **verify**

=== "Details"

    - *Description* - Either a boolean, in which case it controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use.
    - *Default* - `True`
    - *Type* - `bool` or `str`

=== "Example"

    ```python hl_lines="3"
    Ticker(
        'aapl',
        verify=False
    )
    ```

## Premium

### **username and password**

=== "Details"

    - *Description*: If you're a subscriber to Yahoo Finance Premium, you'll be able to retrieve data available through that subscription.  Simply pass your `username` and `password` to the `Ticker` class

    !!! note
        Selenium is utilized to login to Yahoo.  It should take around 15-20 seconds to login.

    !!! tip
        Set environment variables for your username and password as `YF_USERNAME` and `YF_PASSWORD`, respectively.

=== "Example"

    ```python hl_lines="3 4"
    Ticker(
        'aapl',
        username='fake_username',
        password='fake_password'
    )
    ```

## Advanced

### **crumb and session**

=== "Details"

    - *Description*: Some requests to Yahoo Finance require a crumb to make the request.  **This is only utilized for [advanced configuration](../advanced.md)**
    - *Default*:  `None`
    - *Type*: `str`

=== "Example"

    See the [Advanced Section](../advanced.md)
