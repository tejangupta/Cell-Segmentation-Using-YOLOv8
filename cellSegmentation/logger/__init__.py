from datetime import datetime
import os
import logging

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


log_path = os.path.join(os.getcwd(), 'log', os.path.splitext(LOG_FILE)[0])
os.makedirs(log_path, exist_ok=True)
log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
