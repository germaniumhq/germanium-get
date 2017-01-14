from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='germanium-get',
    version='1.10.5',
    description='The germanium project: Selenium WebDriver testing API that doesn\'t disappoint.',
    long_description = readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    install_requires=[
        'germaniumdrivers==1.10.5'
    ],
    packages=['germaniumget'],
    package_data={
        'germanium-get': ['*.js'],
    }
)

