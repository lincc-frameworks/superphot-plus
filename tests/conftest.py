import os
import os.path

from jax import random

import pytest

TEST_DIR = os.path.dirname(__file__)

DATA_DIR_NAME = "data"

# pylint: disable=missing-function-docstring, redefined-outer-name


@pytest.fixture
def test_data_dir():
    return os.path.join(TEST_DIR, DATA_DIR_NAME)


@pytest.fixture
def single_ztf_lightcurve(test_data_dir):
    return os.path.join(test_data_dir, "ZTF22abvdwik.csv")


@pytest.fixture
def single_ztf_lightcurve_compressed(test_data_dir):
    return os.path.join(test_data_dir, "ZTF22abvdwik.npz")


@pytest.fixture
def single_ztf_eqwt_compressed(test_data_dir):
    return os.path.join(test_data_dir, "ZTF22abvdwik_eqwt.npz")


@pytest.fixture
def single_ztf_sn_id():
    return "ZTF22abvdwik"


@pytest.fixture
def jax_key():
    return random.PRNGKey(4)


@pytest.fixture
def class_probs_csv(test_data_dir):
    return os.path.join(test_data_dir, "probs.csv")

