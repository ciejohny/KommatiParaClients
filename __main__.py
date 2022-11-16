# __main__.py
import argparse
from KommatiParaClients.args import args
from KommatiParaClients.clients_df import clients_df

if __name__ == "__main__":
    clients_df(args())
