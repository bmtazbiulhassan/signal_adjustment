import pandas as pd
import sys

from src.exception import CustomException
from src.logger import logging


def target_summary(df: pd.DataFrame):
    """
    Summarizes the red light running flags in the DataFrame.

    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame containing features and red light running flags.

    Returns:
    --------
    pd.DataFrame
        A summary DataFrame showing the count of 'Red Run (1)' and 'Not Red Run (0)' for each flag.

    Raises:
    -------
    CustomException: If an error occurs during the summarization process.
    """
    try:
        logging.info("Starting the target summary process.")

        # Initialize a dictionary to store summary data
        dict_target = {"featureName": [], "Not Red Run (0)": [], "Red Run (1)": []}

        # Iterate through each column in the DataFrame
        for column in df.columns:
            if "RunningFlag" in column:
                logging.info(f"Processing column: {column}")
                
                # Add column name and count values
                dict_target["featureName"].append(column)
                values = df[column].values.tolist()
                dict_target["Not Red Run (0)"].append(values.count(0))
                dict_target["Red Run (1)"].append(values.count(1))

        # Convert the dictionary to a DataFrame
        df_target = pd.DataFrame(dict_target)

        logging.info("Target summary process completed successfully.")
        return df_target

    except Exception as e:
        logging.error(f"Error summarizing target flags: {e}")
        raise CustomException(
            custom_message="An error occurred while summarizing target flags.",
            sys_module=sys
        )
