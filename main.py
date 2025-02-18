import pandas as pd
from all_to_number import all_to_number
from format_sheet import format_sheet


def main():
    file_path: str = "airport_choice.csv"
    output_file_path: str = "formatted_airport_choice.xlsx"
    df: pd.DataFrame = pd.read_csv(file_path)
    df = all_to_number(df)
    df.to_excel(output_file_path, index=False)
    format_sheet(output_file_path)


if __name__ == "__main__":
    main()
