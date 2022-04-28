import pytest
import AdvCalc
import pandas as pd


advCalc = AdvCalc.AdvCalc()

input_data= pd.read_csv("/Users/chandanamurala/Documents/IS601/is601-004/M4/TestCSVFiles/stats_numbers.csv")

input_string = ""
input_list = []
for i in range(len(input_data)):
    input_list.append(input_data["Input|Numbers"][i])

val1 = [input_list]

@pytest.mark.parametrize("val1", val1)
def test_AdvCalc_stdev(val1):
    assert advCalc.stdev(val1) == input_data["Population Standard Deviation|Positive Case "][0]
