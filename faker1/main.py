from faker import Faker
import logging


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("pika")
logger_handler = logging.StreamHandler()
logger.addHandler(logger_handler)
log_format = (
    LOG_FORMAT
) = "[%(asctime)-15s] (%(filename)s:%(lineno)d) %(name)s:%(levelname)s - %(message)s"
logger_handler.setFormatter(logging.Formatter(log_format))

fake = Faker()
while 1:
    test_data = [(fake.name(), fake.address(), fake.postcode(), fake.country(), fake.company(), fake.job())  for i in range(30)]
    print(test_data)
    logger.debug(test_data)
