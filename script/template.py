""" # noqa: E501
Author: Your Name
Created on: YYYY-MM-DD
Email:
GitHub username:

Description:

Example usage:
python script/template.py \
    --input path/to/input/file.txt \
    --output path/to/output/folder \
    --tag "" \

"""
import argparse
import sys
from datetime import datetime
from pathlib import Path


parser = argparse.ArgumentParser(
    description="Template script for demonstration purposes.")

parser.add_argument(
    '--input', type=str,
    required=True,
    help='Input file path')
parser.add_argument(
    '--output', type=str,
    required=True,
    help='Output folder path')
parser.add_argument(
    '--tag', type=str,
    default="",
    help='Tag for the script')

args = parser.parse_args()


def main(args):
    print("Parsed arguments:")
    for key, value in vars(args).items():
        print(f"  {key}: {value}")
    print("*" * 50)

    """
    Define main logic here.
    """
    return


class DualOutput:
    """Redirect output to both terminal and log file."""

    def __init__(self, log_file):
        self.terminal = sys.stdout
        self.log_file = open(log_file, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log_file.write(message)
        self.log_file.flush()

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

    def close(self):
        self.log_file.close()


if __name__ == "__main__":
    script_name = Path(__file__).stem

    # Create output folder
    output_folder = Path(args.output)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Create log file inside output folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = output_folder / f"{script_name}_{args.tag}.log"

    # Redirect all stdout to both terminal and log file
    original_stdout = sys.stdout
    dual_output = DualOutput(log_file)
    sys.stdout = dual_output

    try:
        print("Timestamp: ", timestamp)
        print("=" * 50)
        print(f"Running script: {script_name}")
        print("=" * 50)
        print()

        print(f"Output folder: {output_folder}")
        print(f"Log file: {log_file}")
        print("*" * 50)

        main(args)

        print()
        print("=" * 50)
        print("Script execution completed.")

    finally:
        # Restore original stdout and close log file
        sys.stdout = original_stdout
        dual_output.close()
