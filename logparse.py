import argparse
import logging
from dotenv import load_dotenv
import os

# Refactored for testing: takes arguments directly
def parse_log(logfile, errors_only):
    try:
        error_count = 0
        warning_count = 0
        
        with open(logfile, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                elif not errors_only and "WARNING" in line:
                    warning_count += 1
        
        if errors_only:
            logging.info(f"Found {error_count} errors in '{logfile}'.")
        else:
            logging.info(f"Found {error_count} errors and {warning_count} warnings in '{logfile}'.")

    except FileNotFoundError:
        logging.error(f"The file '{logfile}' was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Original main function, now a simple entry point
def main():
    parser = argparse.ArgumentParser(description="A tool to parse log files.")
    parser.add_argument("logfile", help="The path to the log file to parse.")
    parser.add_argument("--errors-only", action="store_true", help="Only count errors, ignore warnings.")
    args = parser.parse_args()

    # Get log level from environment variable and configure logging
    load_dotenv()
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    numeric_log_level = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(level=numeric_log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Call the new parse_log function
    parse_log(args.logfile, args.errors_only)

if __name__ == "__main__":
    main()