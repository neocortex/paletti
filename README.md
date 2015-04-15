# paletti
A library for extracting color palettes from images.

paletti provides four different ways for automatic color palette extraction
from images.

* A wrapper around PIL's adaptive palette conversion
* A wrapper for the [pictaculous](http://www.pictaculous.com/) API
* A wrapper for the [colorific](https://github.com/99designs/colorific) palette extraction library (Copyright (c) 2012, 99designs)
* A k-means color palette extraction using [scikit-learn](http://scikit-learn.org)

### Installation

Requirements: ``numpy``

``python setup.py install``

### Usage

``paletti -m pil -k 5 -o <IMAGE_FILE>``

Type ``paletti --help`` for all available options.

### Example outputs

* Input image

![alt tag](https://github.com/neocortex/paletti/blob/master/images/test_img.jpg)

The extracted colors are print as a pretty table to stdout:

Color palette of images/test_img.jpg using pil:

+-------------------------+-----------------+--------------------+
|           rgb           |       hex       |     proportion     |
+-------------------------+-----------------+--------------------+
|     (251, 212, 164)     |     #fbd4a4     |        0.15        |
|     (243, 192, 128)     |     #f3c080     |        0.14        |
|     (236, 158,  79)     |     #ec9e4f     |        0.22        |
|     (213, 101,  45)     |     #d5652d     |        0.24        |
|     (177,  29,  15)     |     #b11d0f     |        0.25        |
+-------------------------+-----------------+--------------------+

If the output tag is set, the palette is save as an image:

* PIL palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/pil_palette.png)

* Colorific palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/colorific_palette.png)

* Pictaculous palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/kmeans_palette.png)
