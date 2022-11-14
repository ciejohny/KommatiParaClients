import configparser


def get_config() -> configparser:
    """
    This function generates config for logging
    """
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config
