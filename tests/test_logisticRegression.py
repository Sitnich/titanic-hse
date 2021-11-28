import os

import numpy as np
import pandas as pd
import pytest

import src.models.logisticRegression as lR

@pytest.fixture
def load_res():
    ROOT_DIR_RAW = os.path.abspath(os.curdir) + r"\..\data\test"
    train_df = pd.read_csv(os.path.join(ROOT_DIR_RAW, 'train.csv'),index_col=0)
    test_df = pd.read_csv(os.path.join(ROOT_DIR_RAW, 'test.csv'),index_col=0)
    return train_df, test_df

def test_build_log_reg(load_res):
    assert lR.build_logReg(*load_res).shape


def test_submit():
    created=os.path.exists(os.path.abspath(os.curdir) +r"\..\data\result\res.csv")
    assert created
