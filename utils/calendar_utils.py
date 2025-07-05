import calendar
from config import config

# Define weekdays_map once
WEEKDAYS_MAP = {
    "MONDAY": calendar.MONDAY,
    "TUESDAY": calendar.TUESDAY,
    "WEDNESDAY": calendar.WEDNESDAY,
    "THURSDAY": calendar.THURSDAY,
    "FRIDAY": calendar.FRIDAY,
    "SATURDAY": calendar.SATURDAY,
    "SUNDAY": calendar.SUNDAY,
}

def get_calendar(year: int, month: int):
    """
    Returns a list of weeks for the given month.
    Days outside the month are represented as 0.
    """
    weekday_str = getattr(config, "CALENDAR_FIRST_WEEKDAY", "MONDAY").upper()
    first_day = WEEKDAYS_MAP.get(weekday_str, calendar.MONDAY)
    calendar.setfirstweekday(first_day)
    return calendar.monthcalendar(year, month)

def get_weekday_labels():
    weekday_str = getattr(config, "CALENDAR_FIRST_WEEKDAY", "MONDAY").upper()
    first_day = WEEKDAYS_MAP.get(weekday_str, calendar.MONDAY)
    weekdays = list(calendar.day_name)
    return weekdays[first_day:] + weekdays[:first_day]
