from setuptools import setup, find_packages

setup(
    name='book2jsonofnlp',
    version='2.0.0',
    packages=find_packages(),
    py_modules=['book2jsonofnlp'],
    url="https://github.com/scruffynerf/book2jsonofnlp",
    author="Scruffy Nerf",
    author_email="scruffynerf@duck.com",
    include_package_data=True,
    license="MIT",
    install_requires=[
        'torch>=1.7.1',
        'tensorflow>=1.15',
        'spacy>=3',
        'transformers>=4.11.3'
    ],
)
