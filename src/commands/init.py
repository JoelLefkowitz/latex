import logging
import os
from ..templates import TEMPLATE_PATH
from shutil import copyfile

logger = logging.getLogger(__name__)


def init() -> None:
    for filename in os.listdir(TEMPLATE_PATH):
        _, extension = os.path.splitext(filename)

        if extension in [".j2", ".json"]:
            copyfile(os.path.join(TEMPLATE_PATH, filename), filename)
            logger.info('Copied "%s"', filename)
