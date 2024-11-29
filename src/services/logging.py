import logging
from logging import DEBUG, INFO, WARNING
from rich.logging import RichHandler

root_logger = logging.getLogger()


def set_log_format() -> None:
    logging.basicConfig(
        level=INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()],
    )


def set_log_level(quiet: bool, debug: bool) -> None:
    if debug:
        root_logger.setLevel(DEBUG)

    if quiet:
        root_logger.setLevel(WARNING)
