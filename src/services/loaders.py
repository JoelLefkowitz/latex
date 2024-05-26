import json
import os
from jinja2 import Environment, FileSystemLoader, Template
from typing import Any


def load_inputs(templates: str) -> dict[str, Any]:
    with open(os.path.join(templates, "inputs.json"), "r", encoding="utf8") as stream:
        return json.load(stream)


def load_template(templates: str, name: str = "main.tex.j2") -> Template:
    loader = FileSystemLoader(templates)
    env = Environment(loader=loader)
    return env.get_template(name)
