class Response:
    """Represents a response with a specified type, text content, and error status.

    Parameters
    ----------
    type : str
        The type of the response (e.g., "text").
    text : str
        The actual content of the response.
    is_error : bool, optional
        Indicates if the response is an error (default is False).

    """

    def __init__(self, type: str, text: str, is_error: bool = False):
        self.type = type
        self.text = text
        self.is_error = is_error

    def to_dict(self):
        """Convert the Response object to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the response, including its type, text, and error status.
        """
        return {"type": self.type, "text": self.text, "is_error": self.is_error}
