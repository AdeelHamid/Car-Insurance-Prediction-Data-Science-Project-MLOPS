import sys
import logging

def error_message(error: Exception, error_detail: sys) -> str:
    """Generates a detailed error message including the file name and line number.
    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback information.
    :return: A formatted string with error details.
    """
    # Extract the traceback information
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the line number where the exception occurred
    line_number = exc_tb.tb_lineno
    # Generate the error message
    error_message = f"Error occurred in file: {file_name} at line: {line_number} with message: {str(error)}"
    # Log the error message
    logging.error(error_message)
    return error_message

class MyException(Exception):
    """Custom exception class that extends the base Exception class."""
    def __init__(self, error_message: Exception, error_detail: sys):
        # Generate a detailed error message
        
        super().__init__(self.error_message)

        self.error_message = error_message(error_message, error_detail)

    def __str__(self) -> str:
        """ Returns the string representation of the error message."""
        return self.error_message