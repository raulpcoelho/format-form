import pandas as pd
import re


def all_to_number(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns[1:]:
        df[col] = df[col].apply(lambda x: extract_value(str(x)))
    return df


def extract_value(string) -> float | None:
    match = re.search(r"\((.*?)\)", string)
    if not match:
        return None
    fraction: str = match.group(1).split()[-1]
    try:
        return float(fraction)
    except ValueError:
        numerator, denominator = fraction.split("/")
        return float(numerator) / float(denominator)
