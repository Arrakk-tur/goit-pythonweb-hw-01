import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
my_logger = logging.getLogger(__name__)