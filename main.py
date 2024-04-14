from taipy.gui import Gui
import pandas as pd

value = 10

page = """

#   GARDENEXPERT

# All Location Visulaization
<|{data}|chart|mode=markers|x=Time|y[1]=Temperature|y[2]=Humidity|y[3]=Temperature2|y[4]=Humidity2|>

# Side By Side Overlay
<|{data}|chart|mode=none|x=Time|y[1]=Temperature|y[2]=Humidity|options={options}|>

# Side By Side Overlay
<|{data_one}|chart|mode=none|x=Time|y[1]=Temperature|y[2]=Humidity|options={options}|>
"""

humidityVal=4;

def get_data(path: str):

    dataset= pd.read_csv(path)
    return dataset

data = get_data("temp_vals.csv")
data_one = get_data("temp_vals2.csv")


options = [
    # For items
    {"fill": "tozeroy"},
    # For price
    # Using "tonexty" not to cover the first trace
    {"fill": "tonexty"},
]


Gui(page).run(use_reloader=True,debug=True, port=5001)