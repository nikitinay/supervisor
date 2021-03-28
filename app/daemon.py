import os
import json
import logging
import sys
import logging.handlers as handlers

logging.getLogger('schedule').propagate = False

logging.basicConfig(
    stream=sys.stdout,
    level="DEBUG",
    format="%(asctime)s:%(levelname)s:%(message)s"
)

logger = logging.getLogger(__name__)
