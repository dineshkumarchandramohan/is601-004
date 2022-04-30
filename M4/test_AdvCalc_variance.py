import pytest
import AdvCalc
import pandas as pd


advCalc = AdvCalc.MyCalc()

input_data= pd.read_csv("C:/Users/cmdin/OneDrive/Desktop/github/is601-004/M4/TestCSVFiles/stats_numbers (1).csv")

input_string = ""
input_list = []
for i in range(len(input_data)):
    input_list.append(input_data["Input|Numbers"][i])

val1 = [input_list]

@pytest.mark.parametrize("val1", val1)
def test_AdvCalc_variance(val1):
    assert round(advCalc.variance(val1),4) == round(float(input_data["Positive Test Case| Variance"][0]),4)
