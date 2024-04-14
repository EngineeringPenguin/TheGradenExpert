from taipy.gui import Gui
import pandas as pd

value = 10

page = """

#   GARDENEXPERT

# Scatterplot of all Nodes
<|{data_all}|chart|mode=markers|x=Time|y[1]=Temperature|y[2]=Humidity|y[3]=Temperature2|y[4]=Humidity2|>

# Node 1 Temperature vs Humidity
<|{data_one}|chart|mode=none|x=Time|y[1]=Temperature|y[2]=Humidity|options={options}|>

# Node 2 Temperature vs Humidity
<|{data_two}|chart|mode=none|x=Time|y[1]=Temperature|y[2]=Humidity|options={options}|>

# Senario Sudden Change
<|{bad_data}|chart|mode=none|x=Time|y[1]=Humidity|y[2]=Temperature|options={options}|>
"""

humidityVal=4;

def get_data(path: str):

    dataset= pd.read_csv(path)
    return dataset

data_one = get_data("temp_vals1.csv")
data_all = get_data ("temp_valsA.csv")
data_two = get_data ("temp_vals3.csv")
bad_data = get_data ("val_overlap.csv")


options = [
    # For items
    {"fill": "tozeroy"},
    # For price
    # Using "tonexty" not to cover the first trace
    {"fill": "tonexty"},
]


Gui(page).run(use_reloader=True,debug=True, port=5001)