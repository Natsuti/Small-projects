import datetime, time, logging, calendar
from ASCII import *

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")

grid_c = {"x": 102, "y": 27, "cx": 17, "cy": 7}
DATES = {
    "DAYS": (
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ),
    "MONTHS": (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}
