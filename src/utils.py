import sys
import datetime


def validate_date(date_str):

    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def extract_logs_for_date(target_date, input_file, output_file):

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(
            output_file, "w", encoding="utf-8"
        ) as outfile:
            for line in infile:
                if line.startswith(target_date):
                    outfile.write(line)
    except Exception as e:
        print(f"Error processing files: {e}")
        sys.exit(1)
