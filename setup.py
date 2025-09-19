import io
import os
import re

import setuptools


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "yolov7", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


setuptools.setup(
    name="yolov7detect",
    version=get_version(),
    author="kadirnar",
    license="MIT",
    description="Packaged version of the Yolov7 repository",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/kadirnar/yolov7-pip",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=get_requirements(),
    keywords="machine-learning, deep-learning, pytorch, vision, image-classification, object-detection, yolov7, detector, yolov5",
)
