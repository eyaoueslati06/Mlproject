import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #extracts information about the exception traceback
    file_name=exc_tb.tb_frame.f_code.co_filename #This line retrieves the filename where the exception occurred from the traceback.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) # This line formats the error message string using the extracted information about the error.

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    #This line generates a detailed error message using the error_message_detail function and assigns it to the error_message attribute of the CustomException instance.
    def __str__(self):
        return self.error_message
    

  