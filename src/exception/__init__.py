import sys
import logging
from typing import Any


def error_message_detail(error: Exception, error_detail: Any) -> str:
    """
    Returns a detailed error message including the filename,
    line number, and original exception message.
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in Python script: [{file_name}] "
        f"at line number [{line_number}] "
        f"Error message: {error}"
    )

    logging.error(error_message)

    return error_message


class MyException(Exception):
    """
    Custom exception class that provides detailed error information.
    """

    def __init__(self, error: Exception, error_detail: Any):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self) -> str:
        return self.error_message