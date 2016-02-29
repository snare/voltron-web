# voltron-web

This package provides a simple web interface for [Voltron](https://github.com/snare/voltron). It's mostly used by @snare for debugging, and was split out into another package to keep the web front end clutter out of the main Voltron package. It also provides links to any installed web view plugins (the plugins are still available without the `voltron-web` package, it just provides a list of links).

![web interface](http://i.imgur.com/c8XZ0Oc.png)

## Installation

There is a pre-packed version on PyPI. Install with `pip`:

    $ pip install voltron-web

## Building

Building requires [npm](https://www.npmjs.com/).

Change into the static directory, install the dependencies, and build with [webpack](https://webpack.github.io/):

    $ cd voltron-web/voltron_web/static
    $ npm install
    $ npm install -g webpack
    $ webpack
    $ cd -

Install:

    $ python setup.py install

