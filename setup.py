from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="git_latest_tag_plugin",
    version="0.1.0",
    packages=find_packages(),
    description='MkDocs plugin to display the latest version based on git tags.',
    url='https://github.com/agarthetiger/git_latest_tag_plugin/',
    license='GPL v3',
    long_description='README.md',
    long_description_content_type="text/markdown",
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'GitPython',
        'jinja2'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'mkdocs.plugins': [
            'git-latest-tag = git_latest_tag_plugin.plugin:GitLatestTagPlugin'
        ]
    }
)
