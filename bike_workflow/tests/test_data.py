from bike_workflow.data import get_data
import pandas as pd
import numpy as np


def test_data():
    data = get_data()

    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)



