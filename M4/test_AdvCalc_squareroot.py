import pytest
import AdvCalc
import pandas as pd

d = pd.read_csv("C:/Users/cmdin/OneDrive/Desktop/github/is601-004/M4/TestCSVFiles/Unit_Test_Square_Root.csv")

val1 = d["Value 1"]
res = d["Result"]

advCalc = AdvCalc.MyCalc()
input_data = []
for i in range(len(val1)):
    input_data.append((val1[i], res[i]))

@pytest.mark.parametrize("val1,result", input_data)
def test_AdvCalc_sroot(val1, result):
    assert advCalc.sroot(val1) == result
