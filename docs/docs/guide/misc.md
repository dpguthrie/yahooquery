# Miscellaneous Functions

Additional data can be obtained from Yahoo Finance outside of the three classes. The following functions can be utilized to retrieve additional data unrelated to a ticker symbol:

## Import Functions

```python
import yahooquery as yq
```

## Functions

### currency_converter

=== "Details"

    - *Description*: Retrieve current conversion rate between two currencies as well as historical rates
    - *Returns*: `dict`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | from_currency  | Currency to convert from | `str`  | None     | **required**   | See [get_currencies](#get_currencies) - `shortName`|
    | to_currency  | Currency to convert to | `str`  | None     | **required**   | See [get_currencies](#get_currencies) - `shortName`|
    | period  | Length of historical data to return | `str`  | `week`     | optional   | `day`, `week`, `month`, `6month`, `year`, `allTime` |

=== "Example"

    ```python hl_lines="2"
    import yahooquery as yq
    data = yq.currency_converter("USD", "EUR", "day")
    ```

=== "Data"

    ```python
    {
        'CurrentInterbankRate': 0.8403,
        'CurrentInverseInterbankRate': 1.1901,
        'Average': 0.8443,
        'HistoricalPoints': [{
            'PointInTime': '2020-08-21 18:00:00',
            'InterbankRate': 0.8478,
            'InverseInterbankRate': 1.1795
        }, {
            'PointInTime': '2020-08-22 18:00:00',
            'InterbankRate': 0.8478,
            'InverseInterbankRate': 1.1795
        }, {
            'PointInTime': '2020-08-23 18:00:00',
            'InterbankRate': 0.8475,
            'InverseInterbankRate': 1.1799
        }, {
            'PointInTime': '2020-08-24 18:00:00',
            'InterbankRate': 0.8466,
            'InverseInterbankRate': 1.1812
        }, {
            'PointInTime': '2020-08-25 18:00:00',
            'InterbankRate': 0.8453,
            'InverseInterbankRate': 1.183
        }, {
            'PointInTime': '2020-08-26 18:00:00',
            'InterbankRate': 0.8476,
            'InverseInterbankRate': 1.1798
        }, {
            'PointInTime': '2020-08-27 18:00:00',
            'InterbankRate': 0.8409,
            'InverseInterbankRate': 1.1892
        }, {
            'PointInTime': '2020-08-28 18:00:00',
            'InterbankRate': 0.8399,
            'InverseInterbankRate': 1.1906
        }, {
            'PointInTime': '2020-08-29 18:00:00',
            'InterbankRate': 0.8399,
            'InverseInterbankRate': 1.1906
        }, {
            'PointInTime': '2020-08-30 18:00:00',
            'InterbankRate': 0.8373,
            'InverseInterbankRate': 1.1943
        }, {
            'PointInTime': '2020-08-31 18:00:00',
            'InterbankRate': 0.8375,
            'InverseInterbankRate': 1.1941
        }, {
            'PointInTime': '2020-09-01 18:00:00',
            'InterbankRate': 0.8442,
            'InverseInterbankRate': 1.1845
        }, {
            'PointInTime': '2020-09-02 18:00:00',
            'InterbankRate': 0.845,
            'InverseInterbankRate': 1.1834
        }, {
            'PointInTime': '2020-09-03 18:00:00',
            'InterbankRate': 0.8455,
            'InverseInterbankRate': 1.1828
        }, {
            'PointInTime': '2020-09-04 18:00:00',
            'InterbankRate': 0.8447,
            'InverseInterbankRate': 1.1839
        }, {
            'PointInTime': '2020-09-05 18:00:00',
            'InterbankRate': 0.8447,
            'InverseInterbankRate': 1.1839
        }, {
            'PointInTime': '2020-09-06 18:00:00',
            'InterbankRate': 0.8462,
            'InverseInterbankRate': 1.1818
        }, {
            'PointInTime': '2020-09-07 18:00:00',
            'InterbankRate': 0.8478,
            'InverseInterbankRate': 1.1795
        }, {
            'PointInTime': '2020-09-08 18:00:00',
            'InterbankRate': 0.8471,
            'InverseInterbankRate': 1.1805
        }, {
            'PointInTime': '2020-09-09 18:00:00',
            'InterbankRate': 0.8439,
            'InverseInterbankRate': 1.185
        }, {
            'PointInTime': '2020-09-10 18:00:00',
            'InterbankRate': 0.8447,
            'InverseInterbankRate': 1.1839
        }, {
            'PointInTime': '2020-09-11 18:00:00',
            'InterbankRate': 0.8441,
            'InverseInterbankRate': 1.1848
        }, {
            'PointInTime': '2020-09-12 18:00:00',
            'InterbankRate': 0.8441,
            'InverseInterbankRate': 1.1848
        }, {
            'PointInTime': '2020-09-13 18:00:00',
            'InterbankRate': 0.8427,
            'InverseInterbankRate': 1.1867
        }, {
            'PointInTime': '2020-09-14 18:00:00',
            'InterbankRate': 0.8437,
            'InverseInterbankRate': 1.1852
        }, {
            'PointInTime': '2020-09-15 18:00:00',
            'InterbankRate': 0.8451,
            'InverseInterbankRate': 1.1833
        }, {
            'PointInTime': '2020-09-16 18:00:00',
            'InterbankRate': 0.8458,
            'InverseInterbankRate': 1.1822
        }, {
            'PointInTime': '2020-09-17 18:00:00',
            'InterbankRate': 0.8429,
            'InverseInterbankRate': 1.1863
        }, {
            'PointInTime': '2020-09-18 18:00:00',
            'InterbankRate': 0.8446,
            'InverseInterbankRate': 1.184
        }],
        'supportedByOfx': True,
        'fetchTime': 1600636306047
    }
    ```

### get_currencies

=== "Details"

    - *Description*: List of currencies Yahoo Finance supports
    - *Returns*: `list`

=== "Example"

    ```python hl_lines="2"
    import yahooquery as yq
    data = yq.get_currencies()
    ```

=== "Data"

    ```python
    [{
        'shortName': 'FJD',
        'longName': 'Fijian Dollar',
        'symbol': 'FJD',
        'localLongName': 'Fijian Dollar'
    }, {
        'shortName': 'MXN',
        'longName': 'Mexican Peso',
        'symbol': 'MXN',
        'localLongName': 'Mexican Peso'
    }, {
        'shortName': 'STD',
        'longName': 'São Tomé and Príncipe Dobra',
        'symbol': 'STD',
        'localLongName': 'São Tomé and Príncipe Dobra'
    }, {
        'shortName': 'LVL',
        'longName': 'Latvian Lats',
        'symbol': 'LVL',
        'localLongName': 'Latvian Lats'
    }, {
        'shortName': 'SCR',
        'longName': 'Seychellois Rupee',
        'symbol': 'SCR',
        'localLongName': 'Seychellois Rupee'
    }, {
        'shortName': 'CDF',
        'longName': 'Congolese Franc',
        'symbol': 'CDF',
        'localLongName': 'Congolese Franc'
    }, {
        'shortName': 'BBD',
        'longName': 'Barbadian Dollar',
        'symbol': 'BBD',
        'localLongName': 'Barbadian Dollar'
    }, {
        'shortName': 'GTQ',
        'longName': 'Guatemalan Quetzal',
        'symbol': 'GTQ',
        'localLongName': 'Guatemalan Quetzal'
    }, {
        'shortName': 'CLP',
        'longName': 'Chilean Peso',
        'symbol': 'CLP',
        'localLongName': 'Chilean Peso'
    }, {
        'shortName': 'UGX',
        'longName': 'Ugandan Shilling',
        'symbol': 'UGX',
        'localLongName': 'Ugandan Shilling'
    }, {
        'shortName': 'HNL',
        'longName': 'Honduran Lempira',
        'symbol': 'HNL',
        'localLongName': 'Honduran Lempira'
    }, {
        'shortName': 'ZAR',
        'longName': 'South African Rand',
        'symbol': 'ZAR',
        'localLongName': 'South African Rand'
    }, {
        'shortName': 'MXV',
        'longName': 'Mexican Investment Unit',
        'symbol': 'MXV',
        'localLongName': 'Mexican Investment Unit'
    }, {
        'shortName': 'TND',
        'longName': 'Tunisian Dinar',
        'symbol': 'TND',
        'localLongName': 'Tunisian Dinar'
    }, {
        'shortName': 'STN',
        'longName': 'São Tomé and Príncipe Dobra',
        'symbol': 'STN',
        'localLongName': 'São Tomé and Príncipe Dobra'
    }, {
        'shortName': 'CUC',
        'longName': 'Cuban Convertible Peso',
        'symbol': 'CUC',
        'localLongName': 'Cuban Convertible Peso'
    }, {
        'shortName': 'BSD',
        'longName': 'Bahamian Dollar',
        'symbol': 'BSD',
        'localLongName': 'Bahamian Dollar'
    }, {
        'shortName': 'SLL',
        'longName': 'Sierra Leonean Leone',
        'symbol': 'SLL',
        'localLongName': 'Sierra Leonean Leone'
    }, {
        'shortName': 'SDG',
        'longName': 'Sudanese Pound',
        'symbol': 'SDG',
        'localLongName': 'Sudanese Pound'
    }, {
        'shortName': 'IQD',
        'longName': 'Iraqi Dinar',
        'symbol': 'IQD',
        'localLongName': 'Iraqi Dinar'
    }, {
        'shortName': 'CUP',
        'longName': 'Cuban Peso',
        'symbol': 'CUP',
        'localLongName': 'Cuban Peso'
    }, {
        'shortName': 'GMD',
        'longName': 'Gambian Dalasi',
        'symbol': 'GMD',
        'localLongName': 'Gambian Dalasi'
    }, {
        'shortName': 'TWD',
        'longName': 'New Taiwan Dollar',
        'symbol': 'TWD',
        'localLongName': 'New Taiwan Dollar'
    }, {
        'shortName': 'RSD',
        'longName': 'Serbian Dinar',
        'symbol': 'RSD',
        'localLongName': 'Serbian Dinar'
    }, {
        'shortName': 'DOP',
        'longName': 'Dominican Peso',
        'symbol': 'DOP',
        'localLongName': 'Dominican Peso'
    }, {
        'shortName': 'KMF',
        'longName': 'Comorian Franc',
        'symbol': 'KMF',
        'localLongName': 'Comorian Franc'
    }, {
        'shortName': 'MYR',
        'longName': 'Malaysian Ringgit',
        'symbol': 'MYR',
        'localLongName': 'Malaysian Ringgit'
    }, {
        'shortName': 'FKP',
        'longName': 'Falkland Islands Pound',
        'symbol': 'FKP',
        'localLongName': 'Falkland Islands Pound'
    }, {
        'shortName': 'XOF',
        'longName': 'CFA Franc BCEAO',
        'symbol': 'XOF',
        'localLongName': 'CFA Franc BCEAO'
    }, {
        'shortName': 'GEL',
        'longName': 'Georgian Lari',
        'symbol': 'GEL',
        'localLongName': 'Georgian Lari'
    }, {
        'shortName': 'UYU',
        'longName': 'Uruguayan Peso',
        'symbol': 'UYU',
        'localLongName': 'Uruguayan Peso'
    }, {
        'shortName': 'MAD',
        'longName': 'Moroccan Dirham',
        'symbol': 'MAD',
        'localLongName': 'Moroccan Dirham'
    }, {
        'shortName': 'CVE',
        'longName': 'Cape Verdean Escudo',
        'symbol': 'CVE',
        'localLongName': 'Cape Verdean Escudo'
    }, {
        'shortName': 'TOP',
        'longName': 'Tongan Paʻanga',
        'symbol': 'TOP',
        'localLongName': 'Tongan Paʻanga'
    }, {
        'shortName': 'PGK',
        'longName': 'Papua New Guinean Kina',
        'symbol': 'PGK',
        'localLongName': 'Papua New Guinean Kina'
    }, {
        'shortName': 'AZN',
        'longName': 'Azerbaijan Manat',
        'symbol': 'AZN',
        'localLongName': 'Azerbaijan Manat'
    }, {
        'shortName': 'OMR',
        'longName': 'Omani Rial',
        'symbol': 'OMR',
        'localLongName': 'Omani Rial'
    }, {
        'shortName': 'SEK',
        'longName': 'Swedish Krona',
        'symbol': 'SEK',
        'localLongName': 'Swedish Krona'
    }, {
        'shortName': 'KES',
        'longName': 'Kenyan Shilling',
        'symbol': 'KES',
        'localLongName': 'Kenyan Shilling'
    }, {
        'shortName': 'BTN',
        'longName': 'Bhutanese Ngultrum',
        'symbol': 'BTN',
        'localLongName': 'Bhutanese Ngultrum'
    }, {
        'shortName': 'UAH',
        'longName': 'Ukrainian Hryvnia',
        'symbol': 'UAH',
        'localLongName': 'Ukrainian Hryvnia'
    }, {
        'shortName': 'GNF',
        'longName': 'Guinean Franc',
        'symbol': 'GNF',
        'localLongName': 'Guinean Franc'
    }, {
        'shortName': 'ERN',
        'longName': 'Eritrean Nakfa',
        'symbol': 'ERN',
        'localLongName': 'Eritrean Nakfa'
    }, {
        'shortName': 'MZN',
        'longName': 'Mozambican Metical',
        'symbol': 'MZN',
        'localLongName': 'Mozambican Metical'
    }, {
        'shortName': 'SVC',
        'longName': 'Salvadoran Colón',
        'symbol': 'SVC',
        'localLongName': 'Salvadoran Colón'
    }, {
        'shortName': 'ARS',
        'longName': 'Argentine Peso',
        'symbol': 'ARS',
        'localLongName': 'Argentine Peso'
    }, {
        'shortName': 'QAR',
        'longName': 'Qatari Rial',
        'symbol': 'QAR',
        'localLongName': 'Qatari Rial'
    }, {
        'shortName': 'IRR',
        'longName': 'Iranian Rial',
        'symbol': 'IRR',
        'localLongName': 'Iranian Rial'
    }, {
        'shortName': 'MRO',
        'longName': 'Mauritanian Ouguiya',
        'symbol': 'MRO',
        'localLongName': 'Mauritanian Ouguiya'
    }, {
        'shortName': 'XPD',
        'longName': 'Palladium',
        'symbol': 'XPD',
        'localLongName': 'Palladium'
    }, {
        'shortName': 'THB',
        'longName': 'Thai Baht',
        'symbol': 'THB',
        'localLongName': 'Thai Baht'
    }, {
        'shortName': 'UZS',
        'longName': 'Uzbekistan Som',
        'symbol': 'UZS',
        'localLongName': 'Uzbekistan Som'
    }, {
        'shortName': 'XPF',
        'longName': 'CFP Franc',
        'symbol': 'XPF',
        'localLongName': 'CFP Franc'
    }, {
        'shortName': 'CNY',
        'longName': 'Chinese Yuan',
        'symbol': 'CNY',
        'localLongName': 'Chinese Yuan'
    }, {
        'shortName': 'MRU',
        'longName': 'Mauritanian Ouguiya',
        'symbol': 'MRU',
        'localLongName': 'Mauritanian Ouguiya'
    }, {
        'shortName': 'BDT',
        'longName': 'Bangladeshi Taka',
        'symbol': 'BDT',
        'localLongName': 'Bangladeshi Taka'
    }, {
        'shortName': 'LYD',
        'longName': 'Libyan Dinar',
        'symbol': 'LYD',
        'localLongName': 'Libyan Dinar'
    }, {
        'shortName': 'BMD',
        'longName': 'Bermudan Dollar',
        'symbol': 'BMD',
        'localLongName': 'Bermudan Dollar'
    }, {
        'shortName': 'PHP',
        'longName': 'Philippine Peso',
        'symbol': 'PHP',
        'localLongName': 'Philippine Peso'
    }, {
        'shortName': 'KWD',
        'longName': 'Kuwaiti Dinar',
        'symbol': 'KWD',
        'localLongName': 'Kuwaiti Dinar'
    }, {
        'shortName': 'XPT',
        'longName': 'Platinum',
        'symbol': 'XPT',
        'localLongName': 'Platinum'
    }, {
        'shortName': 'RUB',
        'longName': 'Russian Ruble',
        'symbol': 'RUB',
        'localLongName': 'Russian Ruble'
    }, {
        'shortName': 'PYG',
        'longName': 'Paraguayan Guarani',
        'symbol': 'PYG',
        'localLongName': 'Paraguayan Guarani'
    }, {
        'shortName': 'JMD',
        'longName': 'Jamaican Dollar',
        'symbol': 'JMD',
        'localLongName': 'Jamaican Dollar'
    }, {
        'shortName': 'ISK',
        'longName': 'Icelandic Króna',
        'symbol': 'ISK',
        'localLongName': 'Icelandic Króna'
    }, {
        'shortName': 'COP',
        'longName': 'Colombian Peso',
        'symbol': 'COP',
        'localLongName': 'Colombian Peso'
    }, {
        'shortName': 'USD',
        'longName': 'US Dollar',
        'symbol': 'USD',
        'localLongName': 'US Dollar'
    }, {
        'shortName': 'MKD',
        'longName': 'Macedonian Denar',
        'symbol': 'MKD',
        'localLongName': 'Macedonian Denar'
    }, {
        'shortName': 'DZD',
        'longName': 'Algerian Dinar',
        'symbol': 'DZD',
        'localLongName': 'Algerian Dinar'
    }, {
        'shortName': 'PAB',
        'longName': 'Panamanian Balboa',
        'symbol': 'PAB',
        'localLongName': 'Panamanian Balboa'
    }, {
        'shortName': 'SGD',
        'longName': 'Singapore Dollar',
        'symbol': 'SGD',
        'localLongName': 'Singapore Dollar'
    }, {
        'shortName': 'ETB',
        'longName': 'Ethiopian Birr',
        'symbol': 'ETB',
        'localLongName': 'Ethiopian Birr'
    }, {
        'shortName': 'VEF',
        'longName': 'Venezuelan Bolívar',
        'symbol': 'VEF',
        'localLongName': 'Venezuelan Bolívar'
    }, {
        'shortName': 'KGS',
        'longName': 'Kyrgystani Som',
        'symbol': 'KGS',
        'localLongName': 'Kyrgystani Som'
    }, {
        'shortName': 'SOS',
        'longName': 'Somali Shilling',
        'symbol': 'SOS',
        'localLongName': 'Somali Shilling'
    }, {
        'shortName': 'VUV',
        'longName': 'Vanuatu Vatu',
        'symbol': 'VUV',
        'localLongName': 'Vanuatu Vatu'
    }, {
        'shortName': 'LAK',
        'longName': 'Lao Kip',
        'symbol': 'LAK',
        'localLongName': 'Lao Kip'
    }, {
        'shortName': 'BND',
        'longName': 'Brunei Dollar',
        'symbol': 'BND',
        'localLongName': 'Brunei Dollar'
    }, {
        'shortName': 'ZMK',
        'longName': 'Zambian Kwacha',
        'symbol': 'ZMK',
        'localLongName': 'Zambian Kwacha'
    }, {
        'shortName': 'XAF',
        'longName': 'CFA Franc BEAC',
        'symbol': 'XAF',
        'localLongName': 'CFA Franc BEAC'
    }, {
        'shortName': 'LRD',
        'longName': 'Liberian Dollar',
        'symbol': 'LRD',
        'localLongName': 'Liberian Dollar'
    }, {
        'shortName': 'XAG',
        'longName': 'Silver',
        'symbol': 'XAG',
        'localLongName': 'Silver'
    }, {
        'shortName': 'CHF',
        'longName': 'Swiss Franc',
        'symbol': 'CHF',
        'localLongName': 'Swiss Franc'
    }, {
        'shortName': 'ITL',
        'longName': 'Italian Lira',
        'symbol': 'ITL',
        'localLongName': 'Italian Lira'
    }, {
        'shortName': 'HRK',
        'longName': 'Kuna',
        'symbol': 'HRK',
        'localLongName': 'Kuna'
    }, {
        'shortName': 'ALL',
        'longName': 'Albanian Lek',
        'symbol': 'ALL',
        'localLongName': 'Albanian Lek'
    }, {
        'shortName': 'DJF',
        'longName': 'Djiboutian Franc',
        'symbol': 'DJF',
        'localLongName': 'Djiboutian Franc'
    }, {
        'shortName': 'ZMW',
        'longName': 'ZMW',
        'symbol': 'ZMW',
        'localLongName': 'ZMW'
    }, {
        'shortName': 'VES',
        'longName': 'Venezuelan Bolívar Soberano',
        'symbol': 'VES',
        'localLongName': 'Venezuelan Bolívar Soberano'
    }, {
        'shortName': 'TZS',
        'longName': 'Tanzanian Shilling',
        'symbol': 'TZS',
        'localLongName': 'Tanzanian Shilling'
    }, {
        'shortName': 'XAU',
        'longName': 'Gold',
        'symbol': 'XAU',
        'localLongName': 'Gold'
    }, {
        'shortName': 'VND',
        'longName': 'Vietnamese Dong',
        'symbol': 'VND',
        'localLongName': 'Vietnamese Dong'
    }, {
        'shortName': 'AUD',
        'longName': 'Australian Dollar',
        'symbol': 'AUD',
        'localLongName': 'Australian Dollar'
    }, {
        'shortName': 'ILS',
        'longName': 'Israeli New Sheqel',
        'symbol': 'ILS',
        'localLongName': 'Israeli New Sheqel'
    }, {
        'shortName': 'KPW',
        'longName': 'North Korean Won',
        'symbol': 'KPW',
        'localLongName': 'North Korean Won'
    }, {
        'shortName': 'GYD',
        'longName': 'Guyanaese Dollar',
        'symbol': 'GYD',
        'localLongName': 'Guyanaese Dollar'
    }, {
        'shortName': 'GHS',
        'longName': 'Ghanaian Cedi',
        'symbol': 'GHS',
        'localLongName': 'Ghanaian Cedi'
    }, {
        'shortName': 'KHR',
        'longName': 'Cambodian Riel',
        'symbol': 'KHR',
        'localLongName': 'Cambodian Riel'
    }, {
        'shortName': 'MDL',
        'longName': 'Moldovan Leu',
        'symbol': 'MDL',
        'localLongName': 'Moldovan Leu'
    }, {
        'shortName': 'BOB',
        'longName': 'Bolivian Boliviano',
        'symbol': 'BOB',
        'localLongName': 'Bolivian Boliviano'
    }, {
        'shortName': 'IDR',
        'longName': 'Indonesian Rupiah',
        'symbol': 'IDR',
        'localLongName': 'Indonesian Rupiah'
    }, {
        'shortName': 'KYD',
        'longName': 'Cayman Islands Dollar',
        'symbol': 'KYD',
        'localLongName': 'Cayman Islands Dollar'
    }, {
        'shortName': 'AMD',
        'longName': 'Armenian Dram',
        'symbol': 'AMD',
        'localLongName': 'Armenian Dram'
    }, {
        'shortName': 'SHP',
        'longName': 'Saint Helena Pound',
        'symbol': 'SHP',
        'localLongName': 'Saint Helena Pound'
    }, {
        'shortName': 'BWP',
        'longName': 'Botswanan Pula',
        'symbol': 'BWP',
        'localLongName': 'Botswanan Pula'
    }, {
        'shortName': 'TRY',
        'longName': 'Turkish Lira',
        'symbol': 'TRY',
        'localLongName': 'Turkish Lira'
    }, {
        'shortName': 'LBP',
        'longName': 'Lebanese Pound',
        'symbol': 'LBP',
        'localLongName': 'Lebanese Pound'
    }, {
        'shortName': 'CYP',
        'longName': 'Cypriot Pound',
        'symbol': 'CYP',
        'localLongName': 'Cypriot Pound'
    }, {
        'shortName': 'TJS',
        'longName': 'Tajikistani Somoni',
        'symbol': 'TJS',
        'localLongName': 'Tajikistani Somoni'
    }, {
        'shortName': 'JOD',
        'longName': 'Jordanian Dinar',
        'symbol': 'JOD',
        'localLongName': 'Jordanian Dinar'
    }, {
        'shortName': 'AED',
        'longName': 'United Arab Emirates Dirham',
        'symbol': 'AED',
        'localLongName': 'United Arab Emirates Dirham'
    }, {
        'shortName': 'HKD',
        'longName': 'Hong Kong Dollar',
        'symbol': 'HKD',
        'localLongName': 'Hong Kong Dollar'
    }, {
        'shortName': 'RWF',
        'longName': 'Rwandan Franc',
        'symbol': 'RWF',
        'localLongName': 'Rwandan Franc'
    }, {
        'shortName': 'EUR',
        'longName': 'Euro',
        'symbol': 'EUR',
        'localLongName': 'Euro'
    }, {
        'shortName': 'LSL',
        'longName': 'Lesotho Loti',
        'symbol': 'LSL',
        'localLongName': 'Lesotho Loti'
    }, {
        'shortName': 'DKK',
        'longName': 'Danish Krone',
        'symbol': 'DKK',
        'localLongName': 'Danish Krone'
    }, {
        'shortName': 'CAD',
        'longName': 'Canadian Dollar',
        'symbol': 'CAD',
        'localLongName': 'Canadian Dollar'
    }, {
        'shortName': 'BGN',
        'longName': 'Bulgarian Lev',
        'symbol': 'BGN',
        'localLongName': 'Bulgarian Lev'
    }, {
        'shortName': 'MMK',
        'longName': 'Myanma Kyat',
        'symbol': 'MMK',
        'localLongName': 'Myanma Kyat'
    }, {
        'shortName': 'NOK',
        'longName': 'Norwegian Krone',
        'symbol': 'NOK',
        'localLongName': 'Norwegian Krone'
    }, {
        'shortName': 'SYP',
        'longName': 'Syrian Pound',
        'symbol': 'SYP',
        'localLongName': 'Syrian Pound'
    }, {
        'shortName': 'MUR',
        'longName': 'Mauritian Rupee',
        'symbol': 'MUR',
        'localLongName': 'Mauritian Rupee'
    }, {
        'shortName': 'ZWL',
        'longName': 'Zimbabwean Dollar (2009)',
        'symbol': 'ZWL',
        'localLongName': 'Zimbabwean Dollar (2009)'
    }, {
        'shortName': 'GIP',
        'longName': 'Gibraltar Pound',
        'symbol': 'GIP',
        'localLongName': 'Gibraltar Pound'
    }, {
        'shortName': 'RON',
        'longName': 'Romanian Leu',
        'symbol': 'RON',
        'localLongName': 'Romanian Leu'
    }, {
        'shortName': 'LKR',
        'longName': 'Sri Lankan Rupee',
        'symbol': 'LKR',
        'localLongName': 'Sri Lankan Rupee'
    }, {
        'shortName': 'NGN',
        'longName': 'Nigerian Naira',
        'symbol': 'NGN',
        'localLongName': 'Nigerian Naira'
    }, {
        'shortName': 'IEP',
        'longName': 'Irish Pound',
        'symbol': 'IEP',
        'localLongName': 'Irish Pound'
    }, {
        'shortName': 'CZK',
        'longName': 'Czech Republic Koruna',
        'symbol': 'CZK',
        'localLongName': 'Czech Republic Koruna'
    }, {
        'shortName': 'CRC',
        'longName': 'Costa Rican Colón',
        'symbol': 'CRC',
        'localLongName': 'Costa Rican Colón'
    }, {
        'shortName': 'PKR',
        'longName': 'Pakistani Rupee',
        'symbol': 'PKR',
        'localLongName': 'Pakistani Rupee'
    }, {
        'shortName': 'XCD',
        'longName': 'East Caribbean Dollar',
        'symbol': 'XCD',
        'localLongName': 'East Caribbean Dollar'
    }, {
        'shortName': 'ANG',
        'longName': 'Netherlands Antillean Guilder',
        'symbol': 'ANG',
        'localLongName': 'Netherlands Antillean Guilder'
    }, {
        'shortName': 'HTG',
        'longName': 'Haitian Gourde',
        'symbol': 'HTG',
        'localLongName': 'Haitian Gourde'
    }, {
        'shortName': 'BHD',
        'longName': 'Bahraini Dinar',
        'symbol': 'BHD',
        'localLongName': 'Bahraini Dinar'
    }, {
        'shortName': 'SIT',
        'longName': 'Slovenian Tolar',
        'symbol': 'SIT',
        'localLongName': 'Slovenian Tolar'
    }, {
        'shortName': 'SZL',
        'longName': 'Swazi Lilangeni',
        'symbol': 'SZL',
        'localLongName': 'Swazi Lilangeni'
    }, {
        'shortName': 'SRD',
        'longName': 'Surinamese Dollar',
        'symbol': 'SRD',
        'localLongName': 'Surinamese Dollar'
    }, {
        'shortName': 'KZT',
        'longName': 'Kazakhstani Tenge',
        'symbol': 'KZT',
        'localLongName': 'Kazakhstani Tenge'
    }, {
        'shortName': 'SAR',
        'longName': 'Saudi Riyal',
        'symbol': 'SAR',
        'localLongName': 'Saudi Riyal'
    }, {
        'shortName': 'LTL',
        'longName': 'Lithuanian Litas',
        'symbol': 'LTL',
        'localLongName': 'Lithuanian Litas'
    }, {
        'shortName': 'TTD',
        'longName': 'Trinidad and Tobago Dollar',
        'symbol': 'TTD',
        'localLongName': 'Trinidad and Tobago Dollar'
    }, {
        'shortName': 'YER',
        'longName': 'Yemeni Rial',
        'symbol': 'YER',
        'localLongName': 'Yemeni Rial'
    }, {
        'shortName': 'MVR',
        'longName': 'Maldivian Rufiyaa',
        'symbol': 'MVR',
        'localLongName': 'Maldivian Rufiyaa'
    }, {
        'shortName': 'AFN',
        'longName': 'Afghan Afghani',
        'symbol': 'AFN',
        'localLongName': 'Afghan Afghani'
    }, {
        'shortName': 'INR',
        'longName': 'Indian Rupee',
        'symbol': 'INR',
        'localLongName': 'Indian Rupee'
    }, {
        'shortName': 'NPR',
        'longName': 'Nepalese Rupee',
        'symbol': 'NPR',
        'localLongName': 'Nepalese Rupee'
    }, {
        'shortName': 'KRW',
        'longName': 'South Korean Won',
        'symbol': 'KRW',
        'localLongName': 'South Korean Won'
    }, {
        'shortName': 'AWG',
        'longName': 'Aruban Florin',
        'symbol': 'AWG',
        'localLongName': 'Aruban Florin'
    }, {
        'shortName': 'MNT',
        'longName': 'Mongolian Tugrik',
        'symbol': 'MNT',
        'localLongName': 'Mongolian Tugrik'
    }, {
        'shortName': 'JPY',
        'longName': 'Japanese Yen',
        'symbol': 'JPY',
        'localLongName': 'Japanese Yen'
    }, {
        'shortName': 'AOA',
        'longName': 'Angolan Kwanza',
        'symbol': 'AOA',
        'localLongName': 'Angolan Kwanza'
    }, {
        'shortName': 'PLN',
        'longName': 'Polish Zloty',
        'symbol': 'PLN',
        'localLongName': 'Polish Zloty'
    }, {
        'shortName': 'SBD',
        'longName': 'Solomon Islands Dollar',
        'symbol': 'SBD',
        'localLongName': 'Solomon Islands Dollar'
    }, {
        'shortName': 'GBP',
        'longName': 'British Pound Sterling',
        'symbol': 'GBP',
        'localLongName': 'British Pound Sterling'
    }, {
        'shortName': 'BYN',
        'longName': 'Belarusian Ruble',
        'symbol': 'BYN',
        'localLongName': 'Belarusian Ruble'
    }, {
        'shortName': 'HUF',
        'longName': 'Hungarian Forint',
        'symbol': 'HUF',
        'localLongName': 'Hungarian Forint'
    }, {
        'shortName': 'BYR',
        'longName': 'Belarusian Ruble (2000-2016)',
        'symbol': 'BYR',
        'localLongName': 'Belarusian Ruble (2000-2016)'
    }, {
        'shortName': 'BIF',
        'longName': 'Burundian Franc',
        'symbol': 'BIF',
        'localLongName': 'Burundian Franc'
    }, {
        'shortName': 'MWK',
        'longName': 'Malawian Malawi Kwacha',
        'symbol': 'MWK',
        'localLongName': 'Malawian Malawi Kwacha'
    }, {
        'shortName': 'MGA',
        'longName': 'Malagasy Ariary',
        'symbol': 'MGA',
        'localLongName': 'Malagasy Ariary'
    }, {
        'shortName': 'XDR',
        'longName': 'Special Drawing Rights',
        'symbol': 'XDR',
        'localLongName': 'Special Drawing Rights'
    }, {
        'shortName': 'BZD',
        'longName': 'Belize Dollar',
        'symbol': 'BZD',
        'localLongName': 'Belize Dollar'
    }, {
        'shortName': 'DEM',
        'longName': 'German Mark',
        'symbol': 'DEM',
        'localLongName': 'German Mark'
    }, {
        'shortName': 'BAM',
        'longName': 'Bosnia-Herzegovina Convertible Mark',
        'symbol': 'BAM',
        'localLongName': 'Bosnia-Herzegovina Convertible Mark'
    }, {
        'shortName': 'MOP',
        'longName': 'Macanese Pataca',
        'symbol': 'MOP',
        'localLongName': 'Macanese Pataca'
    }, {
        'shortName': 'EGP',
        'longName': 'Egyptian Pound',
        'symbol': 'EGP',
        'localLongName': 'Egyptian Pound'
    }, {
        'shortName': 'NAD',
        'longName': 'Namibian Dollar',
        'symbol': 'NAD',
        'localLongName': 'Namibian Dollar'
    }, {
        'shortName': 'NIO',
        'longName': 'Nicaraguan Córdoba',
        'symbol': 'NIO',
        'localLongName': 'Nicaraguan Córdoba'
    }, {
        'shortName': 'PEN',
        'longName': 'Peruvian Sol',
        'symbol': 'PEN',
        'localLongName': 'Peruvian Sol'
    }, {
        'shortName': 'NZD',
        'longName': 'New Zealand Dollar',
        'symbol': 'NZD',
        'localLongName': 'New Zealand Dollar'
    }, {
        'shortName': 'WST',
        'longName': 'Samoan Tala',
        'symbol': 'WST',
        'localLongName': 'Samoan Tala'
    }, {
        'shortName': 'TMT',
        'longName': 'Turkmenistani Manat',
        'symbol': 'TMT',
        'localLongName': 'Turkmenistani Manat'
    }, {
        'shortName': 'FRF',
        'longName': 'French Franc',
        'symbol': 'FRF',
        'localLongName': 'French Franc'
    }, {
        'shortName': 'CLF',
        'longName': 'Chilean Unit of Account (UF)',
        'symbol': 'CLF',
        'localLongName': 'Chilean Unit of Account (UF)'
    }, {
        'shortName': 'BRL',
        'longName': 'Brazilian Real',
        'symbol': 'BRL',
        'localLongName': 'Brazilian Real'
    }]
    ```

### get_exchanges

=== "Details"

    - *Description*: List of exchanges and suffixes to use to to retrieve data on various exchanges
    - *Returns*: `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    import yahooquery as yq
    df = yq.get_exchanges()
    df.head()
    ```

=== "Data"

    |    | Country                  | Market, or Index                  | Suffix   | Delay     | Data Provider     |
    |---:|:-------------------------|:----------------------------------|:---------|:----------|:------------------|
    |  0 | United States of America | Chicago Board of Trade (CBOT)     | .CBT     | 10 min    | ICE Data Services |
    |  1 | United States of America | Chicago Mercantile Exchange (CME) | .CME     | 10 min    | ICE Data Services |
    |  2 | United States of America | Dow Jones Indexes                 | nan      | Real-time | ICE Data Services |
    |  3 | United States of America | Nasdaq Stock Exchange             | nan      | Real-time | ICE Data Services |
    |  4 | United States of America | ICE Futures US                    | .NYB     | 30 min    | ICE Data Services |

### get_market_summary

=== "Details"

    - *Description*: List of relevant exchanges for specific country
    - *Returns*: `list`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | country  | Name of country | `str`  | `United States`       | optional   | See below |

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

    ```python hl_lines="2"
    import yahooquery as yq
    yq.get_market_summary(country='hong kong')
    ```

=== "Data"

    ```python
    [{
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'SNP',
        'symbol': '^GSPC',
        'regularMarketChange': {
            'raw': 24.900146,
            'fmt': '24.90'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': -1325583000000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596229659,
            'fmt': '5:07PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': 0.7670505,
            'fmt': '0.77%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 3271.12,
            'fmt': '3,271.12'
        },
        'market': 'us_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'SNP',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'S&P 500',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 3246.22,
            'fmt': '3,246.22'
        }
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'DJI',
        'symbol': '^DJI',
        'regularMarketChange': {
            'raw': 114.66992,
            'fmt': '114.67'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 475857000000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596229659,
            'fmt': '5:07PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': 0.43578112,
            'fmt': '0.44%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 26428.32,
            'fmt': '26,428.32'
        },
        'market': 'us_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'DJI',
        'sourceInterval': 120,
        'region': 'US',
        'shortName': 'Dow 30',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 26313.65,
            'fmt': '26,313.65'
        }
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'Nasdaq GIDS',
        'symbol': '^IXIC',
        'regularMarketChange': {
            'raw': 157.46094,
            'fmt': '157.46'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 34612200000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596230159,
            'fmt': '5:15PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': 1.4871904,
            'fmt': '1.49%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 10745.274,
            'fmt': '10,745.27'
        },
        'market': 'us_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'NIM',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'Nasdaq',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 10587.8,
            'fmt': '10,587.80'
        }
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'Chicago Options',
        'symbol': '^RUT',
        'regularMarketChange': {
            'raw': -14.674194,
            'fmt': '-14.67'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 20,
        'firstTradeDateMilliseconds': 558279000000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596227407,
            'fmt': '4:30PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': -0.981485,
            'fmt': '-0.98%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 1480.427,
            'fmt': '1,480.43'
        },
        'market': 'us_market',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'WCB',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'Russell 2000',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 1495.1012,
            'fmt': '1,495.10'
        }
    }, {
        'fullExchangeName': 'NY Mercantile',
        'symbol': 'CL=F',
        'gmtOffSetMilliseconds': -14400000,
        'headSymbolAsString': 'CL=F',
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596229198,
            'fmt': '4:59PM EDT'
        },
        'regularMarketChangePercent': {
            'raw': 1.2775606,
            'fmt': '1.28%'
        },
        'quoteType': 'FUTURE',
        'headSymbol': True,
        'contractSymbol': False,
        'tradeable': False,
        'regularMarketPreviousClose': {
            'raw': 39.92,
            'fmt': '39.92'
        },
        'exchangeTimezoneName': 'America/New_York',
        'regularMarketChange': {
            'raw': 0.51000214,
            'fmt': '0.51'
        },
        'firstTradeDateMilliseconds': 953701200000,
        'exchangeDataDelayedBy': 30,
        'exchangeTimezoneShortName': 'EDT',
        'marketState': 'REGULAR',
        'regularMarketPrice': {
            'raw': 40.43,
            'fmt': '40.43'
        },
        'market': 'us24_market',
        'sourceInterval': 30,
        'exchange': 'NYM',
        'shortName': 'Crude Oil',
        'region': 'US',
        'triggerable': False
    }, {
        'fullExchangeName': 'COMEX',
        'symbol': 'GC=F',
        'gmtOffSetMilliseconds': -14400000,
        'headSymbolAsString': 'GC=F',
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596229198,
            'fmt': '4:59PM EDT'
        },
        'regularMarketChangePercent': {
            'raw': 1.5960459,
            'fmt': '1.60%'
        },
        'quoteType': 'FUTURE',
        'headSymbol': True,
        'contractSymbol': False,
        'tradeable': False,
        'regularMarketPreviousClose': {
            'raw': 1942.3,
            'fmt': '1,942.30'
        },
        'exchangeTimezoneName': 'America/New_York',
        'regularMarketChange': {
            'raw': 31.0,
            'fmt': '31.00'
        },
        'firstTradeDateMilliseconds': 951714000000,
        'exchangeDataDelayedBy': 30,
        'exchangeTimezoneShortName': 'EDT',
        'marketState': 'REGULAR',
        'regularMarketPrice': {
            'raw': 1973.3,
            'fmt': '1,973.30'
        },
        'market': 'us24_market',
        'sourceInterval': 15,
        'exchange': 'CMX',
        'shortName': 'Gold',
        'region': 'US',
        'triggerable': False
    }, {
        'fullExchangeName': 'COMEX',
        'symbol': 'SI=F',
        'gmtOffSetMilliseconds': -14400000,
        'headSymbolAsString': 'SI=F',
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596229200,
            'fmt': '5:00PM EDT'
        },
        'regularMarketChangePercent': {
            'raw': 5.427616,
            'fmt': '5.43%'
        },
        'quoteType': 'FUTURE',
        'headSymbol': True,
        'contractSymbol': False,
        'tradeable': False,
        'regularMarketPreviousClose': {
            'raw': 23.362,
            'fmt': '23.36'
        },
        'exchangeTimezoneName': 'America/New_York',
        'regularMarketChange': {
            'raw': 1.2679996,
            'fmt': '1.27'
        },
        'firstTradeDateMilliseconds': 951714000000,
        'exchangeDataDelayedBy': 30,
        'exchangeTimezoneShortName': 'EDT',
        'marketState': 'REGULAR',
        'regularMarketPrice': {
            'raw': 24.63,
            'fmt': '24.63'
        },
        'market': 'us24_market',
        'sourceInterval': 15,
        'exchange': 'CMX',
        'shortName': 'Silver',
        'region': 'US',
        'triggerable': False
    }, {
        'fullExchangeName': 'CCY',
        'symbol': 'EURUSD=X',
        'gmtOffSetMilliseconds': 3600000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596234582,
            'fmt': '11:29PM BST'
        },
        'regularMarketChangePercent': {
            'raw': -0.58878887,
            'fmt': '-0.59%'
        },
        'quoteType': 'CURRENCY',
        'tradeable': False,
        'currency': 'USD',
        'regularMarketPreviousClose': {
            'raw': 1.1845534,
            'fmt': '1.1846'
        },
        'exchangeTimezoneName': 'Europe/London',
        'regularMarketChange': {
            'raw': -0.0069744587,
            'fmt': '-0.0070'
        },
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 1070236800000,
        'exchangeTimezoneShortName': 'BST',
        'regularMarketPrice': {
            'raw': 1.1775789,
            'fmt': '1.1776'
        },
        'marketState': 'CLOSED',
        'market': 'ccy_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 4,
        'exchange': 'CCY',
        'sourceInterval': 15,
        'shortName': 'EUR/USD',
        'region': 'US',
        'triggerable': False
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'NYBOT',
        'symbol': '^TNX',
        'regularMarketChange': {
            'raw': -0.004999995,
            'fmt': '-0.0050'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 30,
        'firstTradeDateMilliseconds': -252356400000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596221996,
            'fmt': '2:59PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': -0.9242135,
            'fmt': '-0.92%'
        },
        'quoteType': 'INDEX',
        'marketState': 'REGULAR',
        'regularMarketPrice': {
            'raw': 0.536,
            'fmt': '0.5360'
        },
        'market': 'us24_market',
        'priceHint': 4,
        'tradeable': False,
        'exchange': 'NYB',
        'sourceInterval': 30,
        'region': 'US',
        'shortName': '10-Yr Bond',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 0.541,
            'fmt': '0.5410'
        },
        'longName': 'Treasury Yield 10 Years'
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'Chicago Options',
        'symbol': '^VIX',
        'regularMarketChange': {
            'raw': -0.30000114,
            'fmt': '-0.30'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 20,
        'firstTradeDateMilliseconds': 631290600000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596226490,
            'fmt': '4:14PM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': -1.2116362,
            'fmt': '-1.21%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 24.46,
            'fmt': '24.46'
        },
        'market': 'us_market',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'WCB',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'Vix',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 24.76,
            'fmt': '24.76'
        }
    }, {
        'fullExchangeName': 'CCY',
        'symbol': 'GBPUSD=X',
        'gmtOffSetMilliseconds': 3600000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596234582,
            'fmt': '11:29PM BST'
        },
        'regularMarketChangePercent': {
            'raw': -0.06541982,
            'fmt': '-0.07%'
        },
        'quoteType': 'CURRENCY',
        'tradeable': False,
        'currency': 'USD',
        'regularMarketPreviousClose': {
            'raw': 1.3091918,
            'fmt': '1.3092'
        },
        'exchangeTimezoneName': 'Europe/London',
        'regularMarketChange': {
            'raw': -0.00085651875,
            'fmt': '-0.0009'
        },
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 1070236800000,
        'exchangeTimezoneShortName': 'BST',
        'regularMarketPrice': {
            'raw': 1.3083353,
            'fmt': '1.3083'
        },
        'marketState': 'CLOSED',
        'market': 'ccy_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 4,
        'exchange': 'CCY',
        'sourceInterval': 15,
        'shortName': 'GBP/USD',
        'region': 'US',
        'triggerable': False
    }, {
        'fullExchangeName': 'CCY',
        'symbol': 'JPY=X',
        'gmtOffSetMilliseconds': 3600000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596232799,
            'fmt': '10:59PM BST'
        },
        'regularMarketChangePercent': {
            'raw': 1.078324,
            'fmt': '1.08%'
        },
        'quoteType': 'CURRENCY',
        'tradeable': False,
        'currency': 'JPY',
        'regularMarketPreviousClose': {
            'raw': 104.792,
            'fmt': '104.7920'
        },
        'exchangeTimezoneName': 'Europe/London',
        'regularMarketChange': {
            'raw': 1.1299973,
            'fmt': '1.1300'
        },
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 846633600000,
        'exchangeTimezoneShortName': 'BST',
        'regularMarketPrice': {
            'raw': 105.922,
            'fmt': '105.9220'
        },
        'marketState': 'CLOSED',
        'market': 'ccy_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 4,
        'exchange': 'CCY',
        'sourceInterval': 15,
        'shortName': 'USD/JPY',
        'region': 'US',
        'triggerable': False
    }, {
        'exchangeTimezoneName': 'Europe/London',
        'fullExchangeName': 'CCC',
        'symbol': 'BTC-USD',
        'regularMarketChange': {
            'raw': -2.7011719,
            'fmt': '-2.70'
        },
        'gmtOffSetMilliseconds': 3600000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 1410908400000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596253293,
            'fmt': '4:41AM BST'
        },
        'exchangeTimezoneShortName': 'BST',
        'regularMarketChangePercent': {
            'raw': -0.023798062,
            'fmt': '-0.02%'
        },
        'quoteType': 'CRYPTOCURRENCY',
        'marketState': 'REGULAR',
        'regularMarketPrice': {
            'raw': 11347.686,
            'fmt': '11,347.69'
        },
        'market': 'ccc_market',
        'quoteSourceName': 'CryptoCompare',
        'tradeable': True,
        'exchange': 'CCC',
        'sourceInterval': 15,
        'region': 'US',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 11350.387,
            'fmt': '11,350.39'
        }
    }, {
        'exchangeTimezoneName': 'America/New_York',
        'fullExchangeName': 'Nasdaq GIDS',
        'symbol': '^CMC200',
        'regularMarketChange': {
            'raw': 0.0,
            'fmt': '0.00'
        },
        'gmtOffSetMilliseconds': -14400000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': 1546266600000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1594647950,
            'fmt': '9:45AM EDT'
        },
        'exchangeTimezoneShortName': 'EDT',
        'regularMarketChangePercent': {
            'raw': 0.0,
            'fmt': '0.00%'
        },
        'quoteType': 'INDEX',
        'marketState': 'POSTPOST',
        'regularMarketPrice': {
            'raw': 156.7543,
            'fmt': '156.75'
        },
        'market': 'us_market',
        'quoteSourceName': 'Delayed Quote',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'NIM',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'CMC Crypto 200',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 156.7543,
            'fmt': '156.75'
        }
    }, {
        'exchangeTimezoneName': 'Europe/London',
        'fullExchangeName': 'FTSE Index',
        'symbol': '^FTSE',
        'regularMarketChange': {
            'raw': -92.23047,
            'fmt': '-92.23'
        },
        'gmtOffSetMilliseconds': 3600000,
        'exchangeDataDelayedBy': 15,
        'firstTradeDateMilliseconds': 441964800000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596210339,
            'fmt': '4:45PM BST'
        },
        'exchangeTimezoneShortName': 'BST',
        'regularMarketChangePercent': {
            'raw': -1.5397432,
            'fmt': '-1.54%'
        },
        'quoteType': 'INDEX',
        'marketState': 'CLOSED',
        'regularMarketPrice': {
            'raw': 5897.76,
            'fmt': '5,897.76'
        },
        'market': 'gb_market',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'FGI',
        'sourceInterval': 15,
        'region': 'US',
        'shortName': 'FTSE 100',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 5989.99,
            'fmt': '5,989.99'
        }
    }, {
        'exchangeTimezoneName': 'Asia/Tokyo',
        'fullExchangeName': 'Osaka',
        'symbol': '^N225',
        'regularMarketChange': {
            'raw': -629.23047,
            'fmt': '-629.23'
        },
        'gmtOffSetMilliseconds': 32400000,
        'exchangeDataDelayedBy': 0,
        'firstTradeDateMilliseconds': -157420800000,
        'language': 'en-US',
        'regularMarketTime': {
            'raw': 1596176103,
            'fmt': '3:15PM JST'
        },
        'exchangeTimezoneShortName': 'JST',
        'regularMarketChangePercent': {
            'raw': -2.8167062,
            'fmt': '-2.82%'
        },
        'quoteType': 'INDEX',
        'marketState': 'CLOSED',
        'regularMarketPrice': {
            'raw': 21710.0,
            'fmt': '21,710.00'
        },
        'market': 'jp_market',
        'priceHint': 2,
        'tradeable': False,
        'exchange': 'OSA',
        'sourceInterval': 20,
        'region': 'US',
        'shortName': 'Nikkei 225',
        'triggerable': False,
        'regularMarketPreviousClose': {
            'raw': 22339.23,
            'fmt': '22,339.23'
        }
    }]
    ```

### get_trending

=== "Details"

    - *Description*: List of trending securities for specific country
    - *Returns*: `list`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | country  | Name of country | `str`  | `united states`       | optional   | See below |

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

    ```python hl_lines="2"
    import yahooquery as yq
    data = yq.get_trending()
    ```

=== "Data"

    ```python
    {
        'count': 20,
        'quotes': [{
            'symbol': 'PINS'
        }, {
            'symbol': 'MARA'
        }, {
            'symbol': '^DJI'
        }, {
            'symbol': '^GSPC'
        }, {
            'symbol': '^IXIC'
        }, {
            'symbol': 'MSFT'
        }, {
            'symbol': 'SNY'
        }, {
            'symbol': 'JWN'
        }, {
            'symbol': 'AC.TO'
        }, {
            'symbol': 'CRUS'
        }, {
            'symbol': 'GSK'
        }, {
            'symbol': 'IZEA'
        }, {
            'symbol': 'SONN'
        }, {
            'symbol': 'TLSA'
        }, {
            'symbol': '^RUT'
        }, {
            'symbol': 'RVVTF'
        }, {
            'symbol': 'CLX'
        }, {
            'symbol': 'FLDM'
        }, {
            'symbol': 'KSU'
        }, {
            'symbol': 'BTC-USD'
        }],
        'jobTimestamp': 1596251351296,
        'startInterval': 202008010200
    }
    ```

### search

=== "Details"

    - *Description*: Query Yahoo Finance for anything:  companies, ticker symbols, cusips, news, etc.
    - *Returns*: `dict`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | query  | What you'd like to query from Yahoo Finance | `str`  | None     | **required**   | N/A |
    | quotes_count  | Maximum number of quotes to return | `int`  | 10     | optional   | N/A |
    | news_count  | Maximum number of news items to return | `int`  | 10     | optional   | N/A |
    | first_quote  | Return only the first quote result | `bool`  | `False`     | optional   | `True`, `False` |
    | country  | Name of country | `str`  | `United States`       | optional   | See below |

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

    ```python hl_lines="2"
    import yahooquery as yq
    data = yq.search("38141G104", first_quote=True)
    ```

=== "Data"

    ```python
    {
        'exchange': 'NYQ',
        'quoteType': 'EQUITY',
        'symbol': 'GS',
        'index': 'quotes',
        'score': 33156.0,
        'typeDisp': 'Equity',
        'longname': 'The Goldman Sachs Group, Inc.',
        'isYahooFinance': True
    }
    ```
