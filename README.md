# Spiral #

This app delivers a generated Ulam spiral using the Google Maps API and Flask using RESTful concepts.


The script calculates the number at (x,y) in a [Ulam Spiral](http://en.wikipedia.org/wiki/Ulam_spiral)

GET /api/zoomlevel/xcoord/ycoord returns
{"result":{"prime":"boolean","position":int}}

### To Do ###

* Always expand tests
* Make RESTful
* Expose slices
* Make it database driven
* document document document document
* explore moving calculation to client side
* would make RESTful server irrelevant
