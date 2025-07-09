from datetime import datetime

def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    """
    return datetime.today().strftime("%Y-%m-%d")
