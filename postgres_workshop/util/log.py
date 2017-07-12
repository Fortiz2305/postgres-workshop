import logging


def get_logger(name):
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=logging.DEBUG)
    return logging.getLogger(name)
