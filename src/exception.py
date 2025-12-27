import sys
from typing import Tuple

def error_message_detail(error: Exception, error_detail: sys.SysExcInfoType) -> str:
    """
    Constructs detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno  # ✅ Fixed typo
    error_message = "Error occurred in script name: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys.SysExcInfoType):
        """
        Custom exception with detailed error information.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
