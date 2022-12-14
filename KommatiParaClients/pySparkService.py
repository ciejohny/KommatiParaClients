# pySparkService.py

import sys
import logging
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from KommatiParaClients.log import log_init
import KommatiParaClients.utils as utils


""" log_file = "application.log"
create_log(log_file)
logger = logging.getLogger('ApplicationLog')
"""
logger = log_init()
spark = utils.get_spark()


def load_data_frame(data_location: str) -> DataFrame:
    """
    This function loads provided file into dataframe
    with csv assumption
    """
    try:
        df = spark.read.csv(
            data_location,
            sep=',',
            inferSchema=True,
            header=True
            )
        logger.info("Data loaded to DataFrame from "+data_location)
        return df
    except Exception as e:
        # to implement dedicated error for IO
        logger.error("Data not loaded from " + data_location)
        logger.error(str(e))
        raise


def unload_data_frame(df: DataFrame, data_location: str) -> None:
    """
    This function unloads dataframe to provided file path
    """
    try:
        df.write.option("header", True).\
            option("delimiter", ",").mode('overwrite').csv(data_location)
        logger.info(
            "Data unloaded (" + str(df.count()) + " rows) to "
            + data_location + " folder"
            )
    except Exception as e:
        logger.error("Data not unloaded to " + data_location)
        logger.error(str(e))
        raise


def drop_columns(data_location: str) -> DataFrame:
    """
    This function drops columns from datarame
    Not implemented because for exercise purpose dataset deleivered
    without need of such operation
    """
    raise NotImplementedError


def rename_columns(df: DataFrame, col_mapping: dict) -> DataFrame:
    """
    This function renames column/s based on provided mapping
    """
    for key, value in col_mapping.items():
        df = df.withColumnRenamed(key, value)
    logger.info("Columns renamed based on mapping "+str(col_mapping))
    return df
    # return df.toDF(*cols)


def join_dataframe(
        driver_df: DataFrame,
        joined_df: DataFrame,
        join_key: str,
        join_type: str,
        col_list: list = None
        ) -> DataFrame:
    """
    This function joins dataframes and provides selected columns
    """
    logger.info("DataFrames "+join_type+" joining based on: "+join_key)
    if col_list:
        logger.info("Limiting joined DataFrame to column list"+str(col_list))
        return driver_df.join(joined_df, on=join_key, how=join_type) \
            .select(col_list)
    else:
        return driver_df.join(joined_df, on=join_key, how=join_type)


def filter_dataframe(
        df: DataFrame,
        filter_val: str,
        filter_col_name: str = 'country'
        ) -> DataFrame:
    """
    This function filters data in dataframe
    """
    logger.info(
        "DataFrame filtered based on column: " + filter_col_name +
        " with value '" + filter_val + "'"
        )
    return df.filter(df[filter_col_name] == filter_val)
