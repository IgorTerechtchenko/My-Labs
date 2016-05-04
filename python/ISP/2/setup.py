from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name="myawesomelab",
    version="1.0",
    packages=find_packages(),
    long_description=open(join(dirname(__file__), "README.txt")).read(),
    entry_points={
        "console_scripts":
            ["myawesomelab_logger = myawesomelab.logger:main",
             "myawesomelab_dict = myawesomelab.my_dict:main",
             "myawesomelab_xrange = myawesomelab.my_xrange:main",
             "myawesomelab_sequence = myawesomelab.sequence:main",
             "myawesomelab_to_json = myawesomelab.to_json:main",
             "myawesomelab_bigsort = myawesomelab.bigsort.bin.sort:main",
             "myawesomelab_generate = myawesomelab.bigsort.bin.generate:main",
             "myawesomelab_cahced = myawesomelab.cached:main",
             "myawesomelab_vector = myawesomelab.vector:main"]
    }
)
