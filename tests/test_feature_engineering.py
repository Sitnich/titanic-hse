import copy
import os

import numpy as np
import pandas as pd
import pytest

import src.features.feature_engineering as fe


@pytest.fixture
def load_actual():
    root_dir_raw = os.path.abspath(os.curdir) + r"\data\processed"
    train_df = pd.read_csv(os.path.join(root_dir_raw, 'train.csv'),
                           index_col=0)
    test_df = pd.read_csv(os.path.join(root_dir_raw, 'test.csv'),
                          index_col=0)
    return train_df, test_df


def sample_pay():
    lst = np.random.randint(-1, 1000, size=300)
    return lst


pays = sample_pay()


def sample_family():
    lst = np.random.randint(0, 10, size=300)
    return lst


families = sample_pay()


def sample_age():
    lst = np.random.randint(-1, 100, size=300)
    return lst


ages = sample_age()


@pytest.mark.parametrize("samples", families)
def test_family_group(samples):
    pres = ['loner']
    not_pres = ['small', 'big']
    if samples == 1:
        res = pres
        return fe.family_group(samples) in res
    if samples > 1:
        res = not_pres
        return fe.family_group(samples) in res
    assert False


@pytest.mark.parametrize("samples", ages)
def test_age_group_fun(samples):
    res = None
    young = ['infant', 'toddler', 'child', 'teenager', 'Young_Adult']
    old = ['adult', 'middle_aged', 'senior_citizen', 'old']
    if samples > 0 and samples <= 35:
        res = young
        return fe.age_group_fun(samples) in res
    if samples > 35:
        res = old
        return fe.age_group_fun(samples) in res
    assert False


@pytest.mark.parametrize("samples", pays)
def test_fare_group(samples):
    res = None
    cheap = ['Very_low', 'low', 'mid']
    exp = ['high', 'very_high']
    if samples > 0 and samples <= 20:
        res = cheap
        return fe.fare_group(samples) in res
    if samples > 20:
        res = exp
        return fe.fare_group(samples) in res
    assert False


def test_new_features(load_actual):
    temp = copy.deepcopy(load_actual)
    new = fe.new_features(*load_actual)
    new[0].to_csv(os.path.abspath(os.curdir) + r"\data\test/train.csv")
    new[1].to_csv(os.path.abspath(os.curdir) + r"\data\test/test.csv")
    assert temp[0].shape[1] + 12 == new[0].shape[1]
