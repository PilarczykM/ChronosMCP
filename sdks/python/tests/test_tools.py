from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

import src.tools as tools


def test_now_valid_timezone():
    zone = "Europe/London"
    current_time = tools.now(zone)
    assert isinstance(current_time, datetime)
    assert current_time.tzinfo == ZoneInfo(zone)

def test_now_invalid_timezone():
    zone = "Invalid/Timezone"
    with pytest.raises(ValueError) as excinfo:
        tools.now(zone)
    assert "Unable to create ZoneInfo from Invalid/Timezone" in str(excinfo.value)

def test_now_without_timezone():
    current_time = tools.now()
    assert isinstance(current_time, datetime)
    assert current_time.tzinfo == ZoneInfo("Europe/London")
