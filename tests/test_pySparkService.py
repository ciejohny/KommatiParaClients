# test_pySparkService

from pyspark.sql import SparkSession
import pytest
import chispa.dataframe_comparer as comp_mod
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
import KommatiParaClients.pySparkService as pySparkService
import KommatiParaClients.utils as utils

spark = utils.get_spark()


def test_filter_dataframe(df_cli_det: DataFrame) -> None:
    expected_data = [
        (1, "a1", "b1", "a1.b1@zzz.com", "Netherlands"),
        (2, "a2", "b2", "a2.b2@zzz.com", "Netherlands"),
        (6, "a6", "b6", "a6.b6@zzz.com", "Netherlands")
    ]
    expected_df = spark.createDataFrame(
        expected_data,
        ["id", "first_name", "last_name", "email", "country"]
        )
    comp_mod.assert_df_equality(
        pySparkService.filter_dataframe(df_cli_det, 'Netherlands'),
        expected_df,
        ignore_row_order=True
        )


def test_join_dataframe(df_cli_det: DataFrame, df_cli_trn: DataFrame) -> None:
    expected_data = [
        (1, "a1.b1@zzz.com", "sdasd1", "visa"),
        (1, "a1.b1@zzz.com", "asd098", "visa"),
        (2, "a2.b2@zzz.com", "2dasas", "mastercard"),
        (3, "a3.b3@zzz.com", "4asdas", "san"),
        (4, "a4.b5@zzz.com", "5gfbfg", "mastercard"),
    ]
    expected_df = spark.createDataFrame(
        expected_data,
        ["id", "email", "btc_a", "cc_t"]
        )
    comp_mod.assert_df_equality(
        pySparkService.join_dataframe(
            df_cli_det,
            df_cli_trn,
            'id',
            'inner',
            ["id", "email", "btc_a", "cc_t"]),
        expected_df,
        ignore_row_order=True,
        ignore_column_order=True
        )


def test_rename_columns(df_cli_trn: DataFrame) -> None:
    expected_data = [
        (1, "sdasd1", "visa", 123),
        (1, "asd098", "visa", 345),
        (2, "2dasas", "mastercard", 565),
        (3, "4asdas", "san", 765),
        (4, "5gfbfg", "mastercard", 222),
        (7, "sfsd54", "mastercard", 987)
    ]
    expected_df = spark.createDataFrame(
        expected_data,
        ["id", "bitcoin_address", "credit_card_type", "cc_n"]
        )
    comp_mod.assert_df_equality(
        pySparkService.rename_columns(
            df_cli_trn,
            {'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'}
            ),
        expected_df,
        ignore_row_order=True,
        ignore_column_order=True
        )
