import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt

def ft_load(path: str) -> pd.DataFrame | None:
    """
    It loads a CSV file and returns a pandas DataFrame.

    Args:
        1. The path to the CSV file.
    Returns:
        A pandas DataFrame or None if an error occurs.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: File is not in CSV format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Create a program that calls the load function from the first exercise, loads the files "income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and "life_expectancy_years.csv",
# and displays the projection of life expectancy in relation to the gross national product of
# the year 1900 for each country.
# Your graph must have a title, a legend for each axis and a legend for each graph.
# You must display the year 1900.
def main():
    df1 = ft_load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = ft_load("life_expectancy_years.csv")
    if df1 is None or df2 is None:
        return


if __name__ == "__main__":
    main()