import logging
from .commands.build import build
from .commands.init import init
from .services.logging import set_log_format, set_log_level
from docopt import docopt
from importlib import metadata
from rich.pretty import pretty_repr
from textwrap import dedent

logger = logging.getLogger(__name__)

cli = dedent(
    """
    Usage:
        latex init  [options]
        latex build [options]
        
    Options:
        -t --template ...  Template file [default: template.tex.j2]
        -i --inputs ...    Context variables file [default: inputs.json]
        -o --output ...    Output file [default: article.pdf]
        -h --help          Display the help screen
        -d --debug         Enable debug logging
        -q --quiet         Reduce logging output
        -v --version       Print the package version
    """
)

if __name__ == "__main__":
    set_log_format()
    inputs = docopt(cli, version=metadata.version("latex"))

    set_log_level(inputs["--quiet"], inputs["--debug"])
    logger.debug("Parsed the CLI inputs: %s", pretty_repr(inputs.copy()))

    if inputs["init"]:
        init()

    if inputs["build"]:
        build(inputs["--template"], inputs["--inputs"], inputs["--output"])
