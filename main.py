import time
from datetime import datetime


def say(message : str = "Message...", return_code : int = 0, who : str = "Unknown_function:"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # Getting current time and formatting its output
    print(current_time, "<", return_code, ">", who, "-", message)
    return return_code