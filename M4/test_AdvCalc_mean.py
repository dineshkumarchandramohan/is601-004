import pytest
import AdvCalc
import pandas as pd

input_data= pd.read_csv("/Users/chandanamurala/Documents/IS601/is601-004/M4/TestCSVFiles/stats_numbers.csv")
advCalc = AdvCalc.AdvCalc()

input_string = ""
for i in range(len(input_data)):
    if not (i == (len(input_data) - 1) ):
        input_string = input_string + str(input_data["Input|Numbers"][i]) + ","
    else:
        input_string = input_string + str(input_data["Input|Numbers"][i])

val1 = [input_string]
@pytest.mark.parametrize("val1", val1)
def test_AdvCalc_mean(val1):
    assert advCalc.mean(val1) == float(input_data["Mean|Negative Case"][0])
