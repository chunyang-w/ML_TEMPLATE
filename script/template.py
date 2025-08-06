""" # noqa: E501
Author: Your Name
Created on: YYYY-MM-DD
Email:
GitHub username:

Description:

Example usage:
python script/template.py \
    --input path/to/input/file.txt \
    --output path/to/output/file.txt
    
"""

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Template script for demonstration purposes.")

    parser.add_argument(
        '--input', type=str,
        required=True,
        help='Input file path')
    parser.add_argument(
        '--output', type=str,
        required=True,
        help='Output file path')

    args = parser.parse_args()

    print()
    print("*" * 50)
    print("Parsed arguments:")
    for key, value in vars(args).items():
        print(f"  {key}: {value}")
    print("*" * 50)

    


if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print("" + "=" * 50)
    print(f"Running script: {script_name}")
    print("=" * 50)
    print()
    main()
    print()
    print("" + "=" * 50)
    print("Script execution completed.")
