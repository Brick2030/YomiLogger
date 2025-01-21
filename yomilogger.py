import time
from datetime import datetime
import inspect

filename : str = "log.txt" # Feel free to change to anything
dateformat : str = "%d.%m.%Y - %H:%M:%S"

def say(WriteToFile : bool = False, message : str = "YomiLogger!", return_code : int = 0):
    
    # Extracting time
    now = datetime.now()
    current_time = now.strftime(dateformat)

    # Getting info about current frame in the stack
    frame = inspect.currentframe()
    try:
        # Information about function that call
        caller_frame = frame.f_back
        caller_info = inspect.getframeinfo(caller_frame)
        
        # Getting name of the file and function
        callername = caller_info.filename
        function_name = caller_info.function
        line_number = caller_info.lineno

        if (function_name== "<module>"): function_name = "CORE FUNCTION OF THE FILE"
        else: function_name = function_name + "()"
        
        output : str = f"{current_time} <{return_code}> - {callername} -> {function_name} : Line {line_number} ---> {message} "
        if (not WriteToFile): 
            print(output)
        else: 
            print(output, f"> {filename}")
            with open(filename, 'a') as file:  # Using 'a' for appending data
                file.write(output + '\n')

    finally:
        del frame # Deleting link to the frame to avoid memory leak

    return return_code

def whisper(WriteToFile : bool = False, message : str = "YomiLogger!", return_code : int = 0):
        # Extracting time
    now = datetime.now()
    current_time = now.strftime(dateformat)

    output : str = f"{current_time} <{return_code}> ---> {message} "
    if (not WriteToFile): 
        print(output)
    else: 
        print(output, f"> {filename}")
        with open(filename, 'a') as file:  # Using 'a' for appending data
            file.write(output + '\n')

    return return_code
