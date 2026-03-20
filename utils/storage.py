import json
import os

def load_data(file_path: str) -> list:
    '''
    Arguments:
    - file_path: File path

    Returns data from list (empty if error occurs)
    '''

    # end early if no file found
    if not os.path.exists(file_path):
        return []
    
    # try to return file contents
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

def save_data(
    file_path: str, 
    data: list
) -> None:
    '''
    Arguments:
    - file_path: File path
    - data: Data to write to file path
    '''
    # create directory if not exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # write data
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except OSError as e:
        raise OSError(f"Error writing to file: {e}")