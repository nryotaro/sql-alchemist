from setuptools import setup, find_packages


setup(name='sql-alchemist',
        version="0.0.1",
        packages=find_packages(),
        install_requires=[
            ],
        extras_require={
            'test': [
                'pytest'
                ],
            'dev': [
                'ipython',
                'python-language-server[all]'
                ],
            'doc': [             
                'sphinx',
                'sphinx_rtd_theme'
                ]})
