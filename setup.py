from setuptools import setup, find_packages

setup(
    name="voltron-web",
    version="0.1",
    author="snare",
    author_email="snare@ho.ax",
    description=("Voltron web interface"),
    license="MIT",
    keywords="voltron voltron-web debugger ui gdb lldb vdb",
    url="https://github.com/snare/voltron-web",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_restful'
    ],
    zip_safe=False,
    package_data={
        'voltron_web': ['static/js/bundle.js'],
    },
)