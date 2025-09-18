import os
import argparse
import logging
from dotenv import load_dotenv # NEW: Import load_dotenv

# NEW: Load environment variables from .env file
load_dotenv()

# Get the log level from the environment variable
log_level = os.getenv('LOG_LEVEL', 'INFO')
numeric_log_level = getattr(logging, log_level.upper(), logging.INFO)

# Configure logging
logging.basicConfig(level=numeric_log_level, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="A tool to parse log files.")
    parser.add_argument("logfile", help="The path to the log file to parse.")
    parser.add_argument("--errors-only", action="store_true", help="Only count errors, ignore warnings.")
    args = parser.parse_args()

    try:
        error_count = 0
        warning_count = 0

        with open(args.logfile, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                elif not args.errors_only and "WARNING" in line:
                    warning_count += 1

        if args.errors_only:
            logging.info(f"Found {error_count} errors in '{args.logfile}'.")
        else:
            logging.info(f"Found {error_count} errors and {warning_count} warnings in '{args.logfile}'.")

    except FileNotFoundError:
        logging.error(f"The file '{args.logfile}' was not found.")

if __name__ == "__main__":
    main()