import os
from .services.loaders import load_inputs, load_template
from .services.renderers import render_pdf, render_template
from tempfile import TemporaryDirectory

root = os.path.normpath(os.path.join(__file__, "../.."))

dist = os.path.join(root, "dist")
templates = os.path.join(root, "src/templates")

if __name__ == "__main__":
    inputs = load_inputs(templates)
    template = load_template(templates)

    with TemporaryDirectory() as build:
        render_template(build, template, inputs)
        render_pdf(build, dist)
