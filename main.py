import pandas as pd
import os
from all_to_number import all_to_number
from format_sheet import format_sheet


def main():
    file_path: str = None
    files_in_directory = os.listdir()
    for file in files_in_directory:
        if file.endswith('.csv'):
            file_path = file
            break
    print(f"CSV file found: {file_path}")

    output_file_path: str = "formatted_airport_choice.xlsx"
    df: pd.DataFrame = pd.read_csv(file_path)
    df = all_to_number(df)
    print("Converting to spreadsheet and formatting cells")
    df.to_excel(output_file_path, index=False)
    format_sheet(output_file_path)
    print(f"File saved as {output_file_path}")


if __name__ == "__main__":
    main()
