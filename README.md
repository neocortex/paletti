# paletti
A library for extracting color palettes from images.

paletti provides four different ways for automatic color palette extraction
from images.

* A wrapper around PIL's adaptive palette conversion
* A wrapper for the [pictaculous](http://www.pictaculous.com/) API
* A wrapper for the [colorific](https://github.com/99designs/colorific) palette extraction library (Copyright (c) 2012, 99designs)
* A k-means color palette extraction using [scikit-learn](http://scikit-learn.org)

### Installation

Requirements ``numpy``

``python setup.py install``

### Usage

``paletti -m pil -k 5 -o``

Type ``paletti --help`` for all available options.
