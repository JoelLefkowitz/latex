import os
import subprocess
from jinja2 import Template
from shutil import copyfile
from typing import Any


def render_template(
    build: str,
    template: Template,
    inputs: dict[str, Any],
    output: str = "main.tex",
) -> None:
    template.stream(inputs).dump(os.path.join(build, output))


def render_pdf(
    build: str,
    dist: str,
    template: str = "main.tex",
    output: str = "main.pdf",
) -> None:
    subprocess.run(["pdflatex", f"-output-directory={build}", template], check=False)

    if not os.path.exists(dist):
        os.mkdir(dist)

    copyfile(os.path.join(build, output), os.path.join(dist, output))
