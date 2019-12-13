class YahooQueryError(Exception):
    """
    This error is thrown when an error occurs with the query to Yahoo,
    be it a network problem or invalid query.
    """
    def __init__(self, code=None, description=None):
        self.code = code
        self.description = description
        print(self.code, self.description)

    def __str__(self):
        if not self.code and not self.description:
            return "An error occured while making the query."
        return f"Code:  {self.code}; Description:  {self.description}"
