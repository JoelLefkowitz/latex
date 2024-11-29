import json
import logging
import os
import subprocess
from ..services.paths import output_segments
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile
from subprocess import DEVNULL
from tempfile import TemporaryDirectory

logger = logging.getLogger(__name__)


def build(template: str, inputs: str, output: str) -> None:
    tail, head = output_segments(output, ".pdf")
    target = os.path.join(tail, head)
    logger.debug('Selected the output path "%s"', target)

    if not os.path.isdir(tail):
        logger.error('"%s" is not a directory', tail)

    elif not os.path.isfile(template):
        logger.error('"%s" is not a file', template)

    elif not os.path.isfile(inputs):
        logger.error('"%s" is not a file', inputs)

    else:
        with open(inputs, "r", encoding="utf8") as stream:
            context = json.load(stream)
            logger.info('Loaded inputs from "%s"', inputs)

        with TemporaryDirectory() as staging:
            logger.debug('Created a temporary directory "%s"', staging)

            staged = os.path.join(staging, head)
            logger.debug('Selected the jinja output path "%s"', staged)

            env = Environment(loader=FileSystemLoader(os.path.dirname(template)))
            loaded = env.get_template(os.path.basename(template))
            logger.debug('Loaded the template "%s"', loaded.name)

            loaded.stream(context).dump(staged)
            logger.info('Rendered the template "%s"', template)

            command = ["pdflatex", f"-output-directory={staging}", staged]
            logger.debug('Assembled the pdflatex command: "%s"', " ".join(command))

            subprocess.run(command, stdout=DEVNULL, check=False)
            logger.debug('Ran pdflatex on "%s"', staged)

            copyfile(staged, target)
            logger.info('Created "%s"', head)
