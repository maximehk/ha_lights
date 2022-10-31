import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
        name='home assistant lights',  
        version='0.0.1',
        author="Maxime",
        author_email="",
        description="Simple python library to control lights and switches in Home Assistant..",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/maximehk/ha_lights",
        packages=setuptools.find_packages(),
        python_requires=">=3.6",
        install_requires=[
            'homeassistant_api>=4.0.0.post2',
            ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )

