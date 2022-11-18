# clients_df

from pyspark.sql import SparkSession
import KommatiParaClients.pySparkService as pySparkService
from KommatiParaClients.args import args
from KommatiParaClients.log import log_init


def clients_df(input_params: dict) -> None:
    # logger = log_init()
    # logger = logger.info('Input parameters: ' + input_params['country'])

    # load clients data
    df_cl_det = pySparkService.load_data_frame(
        str(input_params['client_details'])
        )

    # load transations data
    df_cl_tran = pySparkService.load_data_frame(
        input_params['client_transactions']
        )

    # applying data filter
    filtered_df = pySparkService.filter_dataframe(
        df_cl_det,
        input_params['country']
        )

    # select only required columns
    joined_df = pySparkService.join_dataframe(
        filtered_df, df_cl_tran, 'id', 'inner',
        ['id', 'email', 'btc_a', 'cc_t']
        )

    # rename column names
    rencol_df = pySparkService.rename_columns(
        joined_df,
        {'id': 'client_identifier',
            'btc_a': 'bitcoin_address',
            'cc_t': 'credit_card_type'}
        )

    # unload to file
    pySparkService.unload_data_frame(
        rencol_df,
        'client_data'
        )
