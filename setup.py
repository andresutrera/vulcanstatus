from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vulcanStatus",
    version="0.0.1",
    author="Andrés Utrera",
    author_email="andres.utrera@usach.cl",
    description="Vulcan Online Monitoring Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andresutrera/vulcanStatus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3',
    data_files=[
    ('/usr/lib/systemd/system', ['scripts/vulcanStatus.service'])],
    install_requires=["mysql-connector-python",'configparser'],
    scripts=['scripts/vulcanStatus.pyc']
)
