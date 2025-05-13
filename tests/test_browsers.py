from curl_cffi import requests
from curl_cffi.requests.exceptions import ImpersonateError

from yahooquery.constants import BROWSERS


def test_browser_headers():
    """Test that each browser in BROWSERS dictionary can successfully make a request."""
    test_url = "https://google.com"
    errors = []

    for browser_name in BROWSERS.keys():
        try:
            session = requests.Session(
                impersonate=browser_name, headers=BROWSERS[browser_name]
            )
            response = session.get(test_url)
            if response.status_code != 200:
                errors.append(
                    f"{browser_name}: Failed with status code {response.status_code}"
                )
        except ImpersonateError as e:
            errors.append(f"{browser_name}: {str(e)}")
        except Exception as e:
            errors.append(f"{browser_name}: Unexpected error - {str(e)}")

    # Only fail if we collected any errors
    if errors:
        raise AssertionError("\n".join(errors))
