# YomiLogger
(WRITTEN BY AI)
## Overview

YomiLogger is a simple logging utility written in Python that allows you to log messages to both the console and a specified log file. This README will guide you through the installation process, usage of the logging functions, and customization options.

## Installation

To use YomiLogger, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

1. **Clone the repository** (or download the Python file):
   ```bash
   git clone https://github.com/Brick2030/YomiLogger.git
   cd YomiLogger
   ```
   Place it inside of your project.

2. **Ensure you have the required libraries** (if any). For this logger, the standard libraries are sufficient, so no additional installations are needed.

## Usage

### Importing the Logger

To use the YomiLogger in your Python script, you need to import the functions from the external Python file. Assuming the file is named `yomi_logger.py`, you can do the following:

```python
from yomi_logger import say, whisper
```

### Functions

YomiLogger provides two main functions: `say` and `whisper`.

#### 1. `say`

The `say` function logs a message with detailed information about the calling function, including the filename, function name, and line number.

**Function Signature:**
```python
say(WriteToFile: bool = False, message: str = "YomiLogger!", return_code: int = 0)
```

- **Parameters:**
  - `WriteToFile` (bool): If `True`, the message will be written to the log file. Default is `False`.
  - `message` (str): The message you want to log. Default is `"YomiLogger!"`.
  - `return_code` (int): An optional return code to include in the log. Default is `0`.

**Example Usage:**
```python
say(True, "This is a test message.", 1)
```

#### 2. `whisper`

The `whisper` function logs a simpler message without detailed caller information.

**Function Signature:**
```python
whisper(WriteToFile: bool = False, message: str = "YomiLogger!", return_code: int = 0)
```

- **Parameters:**
  - `WriteToFile` (bool): If `True`, the message will be written to the log file. Default is `False`.
  - `message` (str): The message you want to log. Default is `"YomiLogger!"`.
  - `return_code` (int): An optional return code to include in the log. Default is `0`.

**Example Usage:**
```python
whisper(False, "This is a simple log message.", 0)
```

### Customization

- **Log File Name:** You can change the log file name by modifying the `filename` variable in the `yomi_logger.py` file.
- **Date Format:** You can customize the date format by changing the `dateformat` variable in the `yomi_logger.py` file.

## Example

Here’s a complete example of how to use YomiLogger in a Python script:

```python
from yomi_logger import say, whisper

def main():
    say(True, "Starting the application.", 0)
    whisper(False, "This is a simple log message.", 0)
    say(True, "Application finished successfully.", 0)

if __name__ == "__main__":
    main()
```

## Conclusion

YomiLogger is a lightweight and easy-to-use logging utility that can help you keep track of important events in your Python applications. Feel free to customize it to suit your needs, and happy coding!
