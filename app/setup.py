from setuptools import setup

setup(name='app', version='0.1.0', packages=['app'],
      entry_points=['console_scripts':['app = app.__main__:run_application']]
)
