class YahooQueryError(Exception):
    """
    This error is thrown when an error occurs with the query to Yahoo,
    be it a network problem or invalid query.
    """
    def __init__(self, description=None):
        self.description = description

    def __str__(self):
        if not self.description:
            return "An error occured while making the query."
        return self.description
