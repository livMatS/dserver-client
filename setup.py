from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.rst').read()

setup(
    name="dtool_lookup_client",
    packages=["dtool_lookup_client"],
    version=version,
    description="Dtool plugin for interacting with dtool lookup server",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
