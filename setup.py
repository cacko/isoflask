from setuptools import setup, find_packages
from setuptools.dist import Distribution as _Distribution
from pathlib import Path
import semver
from isoflask import __name__
import sys



def version():
    if len(sys.argv) > 1 and sys.argv[1] >= "bdist_wheel":
        init = Path(__file__).parent / __name__ / "version.py"
        _, v = init.read_text().split(' = ')
        cv = semver.VersionInfo.parse(v.strip('"'))
        nv = f"{cv.bump_patch()}"
        init.write_text(f'__version__ = "{nv}"')
        print(nv)
        return nv
    from isoflask.version import __version__
    return __version__


class Distribution(_Distribution):
    def is_pure(self): return True

setup(
    name=__name__,
    version=version(),
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
