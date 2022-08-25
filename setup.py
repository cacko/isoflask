from setuptools import setup, find_packages
from setuptools.dist import Distribution as _Distribution
from isoflask.version import __version__
from pathlib import Path
import semver
from isoflask import __name__


def inc_version():
    init = Path(__file__).parent / __name__ / "version.py"
    _, v = init.read_text().split(' = ')
    cv = semver.VersionInfo.parse(v.strip('"'))
    init.write_text(f'__version__ = "{cv.bump_patch()}"')

class Distribution(_Distribution):
    def is_pure(self): return True

setup(
    name=__name__,
    version=__version__,
    author='cacko',
    author_email='alex@cacko.net',
    distclass=Distribution,
    url=f'http://pypi.cacko.net/simple/{__name__}/',
    description='whatever',
    install_requires=[
        "flask>=2.2.2",
        "orjson>=3.7.12"
    ],
    setup_requires=['wheel'],
    python_requires=">=3.8",
    packages=find_packages(include=[__name__]),
)
