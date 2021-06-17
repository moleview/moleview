import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moleview", # Replace with your own username
    version="1.1",
    author="Rangsiman Ketkaew",
    author_email="rangsiman1993@gmail.com",
    description="MoleView: view your molecule anywhere and anytime.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moleview/moleview",
    download_url="https://github.com/moleview/moleview/releases",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=[
        "chemistry",
        "computational chemistry",
        "crystallography",
        "Molecular visualization",
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "moleview=moleview.src.moleview:main"
        ]
    },
)