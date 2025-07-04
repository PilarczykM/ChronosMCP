import logging

from mcp.server.fastmcp import FastMCP

import tools
from models import Response

mcp = FastMCP("ChronosMCP")


@mcp.tool()
def now(zone: str = None):
    """Get current time for a specified timezone.

    Parameters
    ----------
    zone : str, optional
        The timezone string (e.g., "Europe/London", "America/NewYork").
        If None, the default timezone is "Europe/London".

    Returns
    -------
    dict
        A dictionary containing either the current time or an error message.
        If successful:
            `{'result': {'type': 'text', 'text': str(current_time)}}`
        If an error occurs:
            `{'error': {'type': 'text', 'text': str(exception), 'isError': True}}`

    """
    try:
        current_time = tools.now(zone)
    except ValueError as e:
        logging.error(f"Error in function now: {e}")
        return {"error": Response(type="text", text=str(e), is_error=True).to_dict()}
    return {"result": Response(type="text", text=str(current_time)).to_dict()}


if __name__ == "__main__":
    mcp.run("stdio")
