import logging
import os

def get_logger(name):
    """Create and return a logger that writes to console and a log file."""
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        #Console handler - prints to terminal
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        #File handler - writes to a logs/test.log
        file_handler = logging.FileHandler(f"{log_folder}/test.log")
        file_handler.setLevel(logging.INFO)

        formatter  = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)
    return logger