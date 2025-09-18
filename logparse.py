import argparse

def main():
    # 1. Create the parser
    parser = argparse.ArgumentParser(description="A tool to parse log files.")

    # 2. Add an argument for the log file
    parser.add_argument("logfile", help="The path to the log file to parse.")

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Print the value of the argument
    print(f"Parsing log file at: {args.logfile}")

if __name__ == "__main__":
    main()