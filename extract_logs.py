import sys
import os
import time
from src.utils import validate_date, extract_logs_for_date


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date = sys.argv[1]
    if not validate_date(target_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    input_file = "logs_2024.log"
    if not os.path.exists(input_file):
        print(
            f"Input log file '{input_file}' does not exist. Please ensure it is available."
        )
        sys.exit(1)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    print(f"Extracting logs for {target_date} from {input_file}...")
    start_time = time.time()
    extract_logs_for_date(target_date, input_file, output_file)
    print(f"Extraction complete. Logs saved to: {output_file}")
    end_time = time.time()

    print(f"Total time elapsed: {end_time-start_time}")


if __name__ == "__main__":
    main()
