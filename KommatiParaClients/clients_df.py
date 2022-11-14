# clients_df

from pyspark.sql import SparkSession
from KommatiParaClients.pySparkService import *
from KommatiParaClients.args import args
from KommatiParaClients.log import *


def clients_df(input_params: dict) -> None:

    # logger = log_init()
    # logger = logger.info('Input parameters: ' + input_params['country'])

    # load clients data
    df1 = load_data_frame(
        str(input_params['client_details'])
        )

    # load transations data
    df2 = load_data_frame(
        input_params['client_transactions']
        )

    # applying data filter
    filtered_df = filter_dataframe(df1, input_params['country'])

    # select only required columns
    joined_df = join_dataframe(
        filtered_df, df2, 'on: id', 'inner',
        ['id', 'email', 'btc_a', 'cc_t']
        )

    # rename column names
    rencol_df = rename_columns(
        joined_df, {'id': 'client_identifier', 'btc_a': 'bitcoin_address'}
        )

    # unload to file
    unload_data_frame(
        rencol_df,
        'client_data'
        )
