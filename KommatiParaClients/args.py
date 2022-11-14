import argparse


def args() -> dict:
    parser = argparse.ArgumentParser(
        description='Clients data output creation'
        )
    parser.add_argument(
        '-cl_det',
        '--client_details',
        help='Full path to data file with client mails',
        required=True
        )
    parser.add_argument(
        '-cl_trn',
        '--client_transactions',
        help='Full path to data file with client transactions',
        required=True
        )
    parser.add_argument(
        '-cntry',
        '--country',
        help='Country name for client output',
        required=True
        )
    return vars(parser.parse_args())
