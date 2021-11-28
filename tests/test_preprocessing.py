import os
from itertools import combinations_with_replacement

import numpy as np
import pandas as pd
import pytest

import src.data.preprocessing as pp


@pytest.fixture
def load_actual_raw():
    root_dir_raw = os.path.abspath(os.curdir) + r"\data\raw"
    train_df = pd.read_csv(os.path.join(root_dir_raw, 'train.csv'))
    test_df = pd.read_csv(os.path.join(root_dir_raw, 'test.csv'))
    return train_df, test_df


def sample_df():
    df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                      columns=['a', 'b', 'c'])
    lst = []
    for i in range(20):
        lst.append(df.sample(n=np.random.randint(1, 10), replace=True))
    return lst


samples_list = sample_df()


@pytest.mark.parametrize("a,b", list(combinations_with_replacement([
    str(i) for i in range(20)], 2)))
def test_loading(a, b):
    root_dir = os.path.abspath(os.curdir) + r"\data\test"

    def f(x):
        return root_dir + '\\' + x + '.csv'

    assert isinstance(pp.loading(f(a), f(b))[0], type(pd.DataFrame()))


@pytest.mark.parametrize("samples", samples_list)
def test_print_info(samples):
    result = pp.print_info(samples)
    assert result == 'printed'


def test_preparing(load_actual_raw):
    assert len(pp.preparing(*load_actual_raw)) == 3


def test_hasattr(load_actual_raw):
    assert 'Sex' in load_actual_raw[0].columns


def test_bool(load_actual_raw):
    assert np.issubdtype(pp.bool_sex(load_actual_raw[0]), np.integer)
