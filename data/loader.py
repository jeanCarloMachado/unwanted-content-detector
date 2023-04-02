
import pandas as pd
def load_data():
    return pd.read_csv("data/data.csv", on_bad_lines='skip', sep='|')
