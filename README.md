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

* The color-reduced image computed when choosing K-Means as method
![alt
tag](https://github.com/neocortex/paletti/blob/master/images/kmeans_image.png)
