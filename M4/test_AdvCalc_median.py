import pytest
import AdvCalc
import pandas as pd


advCalc = AdvCalc.AdvCalc()

input_data= pd.read_csv("/Users/chandanamurala/Documents/IS601/is601-004/M4/TestCSVFiles/stats_numbers.csv")
advCalc = AdvCalc.AdvCalc()

input_list = []
for i in range(len(input_data)):
    input_list.append(input_data["Input|Numbers"][i])

val1 = [input_list]
@pytest.mark.parametrize("val1", val1)
def test_AdvCalc_median(val1):
    assert advCalc.median(val1) == input_data["Median|Positive Case|"][0]
