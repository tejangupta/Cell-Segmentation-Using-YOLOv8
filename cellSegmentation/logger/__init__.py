from datetime import datetime
import os
from from_root import from_root
import logging

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


log_path = os.path.join(from_root(), 'log', os.path.splitext(LOG_FILE)[0])
os.makedirs(log_path, exist_ok=True)
lOG_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=lOG_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
