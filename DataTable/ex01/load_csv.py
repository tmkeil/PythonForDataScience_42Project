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


def main():
    df = ft_load("life_expectancy_years.csv")
    if df is None:
        return
    plt.figure(figsize=(10, 6))
    plt.title('Life Expectancy in Germany')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.plot(data=df[df['Country'] == 'Germany'], x='Year', y='Life expectancy', label='Germany', color='blue')
    plt.show()


if __name__ == "__main__":
    main()