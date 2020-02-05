import logging
import sys


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    root.setLevel(lvl)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(funcName)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    if logfile is None:
        handler = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        handler = logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    root.addHandler(handler)



