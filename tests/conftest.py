# conftest.py
import KommatiParaClients.utils as utils
from pyspark.sql import DataFrame
import pytest

spark = utils.get_spark()


@pytest.fixture
def df_cli_det() -> DataFrame:
    data_cl = [
        (1, "a1", "b1", "a1.b1@zzz.com", "Netherlands"),
        (2, "a2", "b2", "a2.b2@zzz.com", "Netherlands"),
        (3, "a3", "b3", "a3.b3@zzz.com", "France"),
        (4, "a4", "b4", "a4.b5@zzz.com", "United Kingdom"),
        (5, "a5", "b5", "a5.b6@zzz.com", "Poland"),
        (6, "a6", "b6", "a6.b6@zzz.com", "Netherlands")
    ]
    return spark.createDataFrame(
        data_cl,
        ["id", "first_name", "last_name", "email", "country"]
        )


@pytest.fixture
def df_cli_trn() -> DataFrame:
    data_cl = [
        (1, "sdasd1", "visa", 123),
        (1, "asd098", "visa", 345),
        (2, "2dasas", "mastercard", 565),
        (3, "4asdas", "san", 765),
        (4, "5gfbfg", "mastercard", 222),
        (7, "sfsd54", "mastercard", 987)
    ]
    return spark.createDataFrame(
        data_cl,
        ["id", "btc_a", "cc_t", "cc_n"]
        )
