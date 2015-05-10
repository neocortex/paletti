# paletti
A library for extracting color palettes from images.

paletti provides four different ways for automatic color palette extraction
from images and image URLs.

* A wrapper around PIL's adaptive palette conversion.
* A wrapper for the [pictaculous](http://www.pictaculous.com/) API.
* A wrapper for the [colorific](https://github.com/99designs/colorific) palette extraction library (Copyright (c) 2012, 99designs).
* A k-means color palette extraction using [scikit-learn](http://scikit-learn.org). Additionally creates a color-reduced image with the palette colors.

### Installation

Requirements: ``numpy``

``python setup.py install``

### Usage examples

Extract a 5-color palette from a local image using the PIL method:

    ``paletti -m pil -k 5 -o <IMAGE_FILE>``

Extract a 3-color palette from an image URL using k-means:

    ``paletti -m k-means -k 3 -o -u <IMAGE_URL>

Type ``paletti --help`` for all available options.

### Example outputs

* Input image

![alt tag](https://github.com/neocortex/paletti/blob/master/images/test_img.jpg)

The extracted colors are print as a pretty table to stdout:

![alt tag](https://github.com/neocortex/paletti/blob/master/images/stdout.png)


If the output tag is set, the palette is save as an image:

* PIL palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/pil_palette.png)

* Colorific palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/colorific_palette.png)

* Pictaculous palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/pictaculous_palette.png)

* K-Means palette

![alt tag](https://github.com/neocortex/paletti/blob/master/images/kmeans_palette.png)

* The color-reduced image (k=5) computed when choosing k-means as method
![alt
tag](https://github.com/neocortex/paletti/blob/master/images/kmeans_image.png)
