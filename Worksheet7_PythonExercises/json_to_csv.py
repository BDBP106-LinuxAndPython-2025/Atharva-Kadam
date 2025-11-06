import pandas as pd

def json_to_csv_pandas(json_filepath, csv_filepath):
    """
    Converts a JSON file to a CSV file using the pandas library.
    Handles nested JSON by flattening it.
    """
    try:
        # Read the JSON file into a pandas DataFrame
        df = pd.read_json(json_filepath)

        # For nested JSON, you might need to flatten it using json_normalize
        # from pandas.io.json import json_normalize
        # df = json_normalize(data_from_json_load) if needed

        # Write the DataFrame to a CSV file
        # index=False prevents writing the DataFrame index as a column in the CSV
        df.to_csv(csv_filepath, index=False)
        print(f"Successfully converted '{json_filepath}' to '{csv_filepath}'")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

# Example usage:
json_to_csv_pandas('ODI-Batting_Cricket_Analytics.json', 'ODI_Cricket_Analytics.csv')