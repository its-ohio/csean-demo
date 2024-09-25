import os
import sys
import logging
from dotenv import load_dotenv

__all__ = [
    "logger"
]

# ENVIRONMENT VARIABLES SETUP
load_dotenv(".env.local")

# LOGGER SETUP
logging.basicConfig(
    format='{"level": "%(levelname)s", "time": "%(asctime)s", "message": %(message)s"}',
    level=os.getenv("LOGLEVEL", "INFO"),
    force=True,
    handlers=[
        logging.StreamHandler(sys.stdout),
    ]
)
# Remove httpx logs (INFO logs every time a request is made - annoying):
logging.getLogger("httpx").setLevel("WARNING")
# Instantiate new logger
logger = logging.getLogger(__name__)
