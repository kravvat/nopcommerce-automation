import os
import logging


class LogMaker:
    @staticmethod
    def generate_log():
        log_path = ".\\logs\\nopcommerce.log"
        # if os.path.exists(log_path):
            # os.remove(log_path)
        
        logging.basicConfig(
            filename = log_path,
            format = "%(asctime)s:%(levelname)s:%(message)s",
            datefmt = "%d-%m-%Y %H:%M:%S",
            force = True,
            )
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
