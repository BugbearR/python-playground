import argparse
import logging

# python3 logging-exp.py --log=debug

parser = argparse.ArgumentParser()
parser.add_argument('--log', dest='loglevel', default='INFO', help='set log level')
args = parser.parse_args()

numeric_level = getattr(logging, args.loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.loglevel)

logging.basicConfig(level=numeric_level)

logger = logging.getLogger(__name__)

logger.debug("logger.debug hello")
logger.info("logger.info hello")
logger.warning("logger.warning hello")
logger.critical("logger.critical hello")
logger.fatal("logger.fatal hello")
logger.exception("logger.exception hello")
logger.log(logging.DEBUG, "logger.log(logging.DEBUG, hello")
logger.error("logger.error hello")
