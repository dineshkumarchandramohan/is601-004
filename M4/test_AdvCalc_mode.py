import pytest
import AdvCalc
import pandas as pd


advCalc = AdvCalc.AdvCalc()

input_data= pd.read_csv("/Users/chandanamurala/Documents/IS601/is601-004/M4/TestCSVFiles/stats_numbers.csv")

input_list = []
for i in range(len(input_data)):
    input_list.append(input_data["Input|Numbers"][i])

val1 = [input_list]
@pytest.mark.parametrize("val1", val1)
def test_AdvCalc_mode(val1):
    assert advCalc.mode(val1) == input_data["Mode|Positive Case"][0]
