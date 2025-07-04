from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def now(zone: str = "Europe/London") -> datetime:
    """Get current time.

    Parameters
    ----------
    zone: str
        Example "Europe/London", "America/NewYork"

    Return
    ------
    datetime: datetime

    """
    try:
        tzinfo = ZoneInfo(zone)
    except ZoneInfoNotFoundError as e:
        raise ValueError(f"Unable to create ZoneInfo from {zone}. Error: {e}")

    return datetime.now(tzinfo)
