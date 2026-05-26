import sys
from src.logger import logging

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() ## Get the exception information
    file_name = exc_tb.tb_frame.f_code.co_filename ## Get the file name where the error occurred
    line_number = exc_tb.tb_lineno ## Get the line number where the error occurred
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message) ## Call the parent class constructor
        self.error_message = error_message_details(error_message, error_detail=error_detail) ## Get the error message details
    
    def __str__(self):
        return self.error_message ## Return the error message when the exception is printed