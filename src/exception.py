import sys
import logging

# Whenever an error is raised this will push...it
def error_message_detail(error,error_detail:sys):

    # This will give u 3 imp information
    # 1,2 --> No need
    # 3-->It gives on which file, which line exception is occured...
    _,_,exc_tb = error_detail.exc_info()

    # This will give file name
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    # Whenever i raise this it inherit above function
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail = error_detail)
    def __str__(self):
        return self.error_message
        
'''if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys) '''
