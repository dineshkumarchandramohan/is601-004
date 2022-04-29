import pytest
import AdvCalc
import pandas as pd

d = pd.read_csv("/Users/cmdin/OneDrive/Desktop/github/is601-004/M4/TestCSVFiles/Unit_Test_Square.csv")

val1 = d["Value 1"]
res = d["Result"]

advCalc = AdvCalc.AdvCalc()
input_data = []
for i in range(len(val1)):
    input_data.append((val1[i], res[i]))

@pytest.mark.parametrize("val1,result", input_data)
def test_AdvCalc_square(val1, result):
    assert advCalc.square(val1) == result
