from setuptools import setup, find_packages

setup(
    name="taky",
    python_requires=">=3.6",
    use_scm_version=True,
    author="Tim K",
    author_email="tpkuester@gmail.com",
    tests_require=["mock"],
    setup_requires=["setuptools_scm"],
    install_requires=[
        "lxml>=4.4.0",
        "dateutils",
        "Flask",
        "pyopenssl",
        "gunicorn",
        "redis",
    ],
    description="A simple TAK server and COT router",
    url="https://github.com/DistributedSpectrum/taky",
    packages=find_packages(),
    test_suite="tests",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Topic :: Communications",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "taky = taky.cot.__main__:main",
            "taky_dps = taky.dps.__main__:main",
            "takyctl = taky.cli.__main__:main",
        ]
    },
)
