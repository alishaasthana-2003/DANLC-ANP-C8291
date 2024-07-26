#Exception Handling with Logging
#- Write a function `read_and_log` that reads a file and logs any exceptions that occur to a separate log file. Use exception handling to manage:
#- File not found.
#- Permission denied.
#- Any other error.
#- Ensure the function writes detailed error messages to the log file and test it with various scenarios.

import logging
logging.basicConfig(filename='error_log.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def read_and_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        error_message = f"File not found: {file_path}"
        logging.error(error_message)
        return error_message
    except PermissionError:
        error_message = f"Permission denied: {file_path}"
        logging.error(error_message)
        return error_message
    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        return error_message

