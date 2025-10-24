import logging


class LogMaker:
    @staticmethod
    def generate_log():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",
            format="%(asctime)s:%(levelname)s:%(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            force=True,
            )
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger