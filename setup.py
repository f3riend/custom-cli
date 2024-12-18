from setuptools import setup, find_packages

setup(
    name="selful-packages",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "selful-packages=selful_packages.cli:cli",  # İsim ve yol burada uyarlanmalı
        ],
    },
    author="f3riend",
    description="Basit bir CLI uygulaması",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/f3riend/selful-packages",  # URL'yi de uyarladım
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
