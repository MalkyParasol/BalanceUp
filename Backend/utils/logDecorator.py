"""
logDecorator.py

This module defines a decorator function for logging API requests to a file.

"""
from functools import wraps
from fastapi import HTTPException
from datetime import datetime


def log_to_file():
    """
        Decorator function for logging API requests to a file.

        Returns:
            function: Decorator function that logs API requests.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get the current timestamp
            timestamp = datetime.now().isoformat()

            # Determine the type of call (e.g., GET, POST, PUT, DELETE)
            request_method = func.__name__.split("_")[0].upper()

            # Execute the function and capture the result
            try:
                result = func(*args, **kwargs)
                status = "Succeeded"
            except HTTPException as e:
                status = f"Failed with status code {e.status_code}"
                result = None

            # Log the information to the file
            with open('./log.txt', "a") as file:
                file.write(f"{timestamp} - {request_method} - {func.__name__} - {status}\n")

            return result

        return wrapper

    return decorator
