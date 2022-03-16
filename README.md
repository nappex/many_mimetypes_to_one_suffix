# many_mimetypes_to_one_suffix
Serving files with the suffix where is linked more than one mimetype in `mime-db.json`

If we want to use official github pages database for mimetype [mime-db](https://github.com/jshttp/mime-db/blob/master/db.json), we find out that some file suffix can be define with more than just one mimetype.

This repo creates files with suffix, where is not determined the exact one mimetype. So we can study which certain headers are sent by github pages server.

This repo contains two script.

* python script to find suffixes which has more mimetypes
* shell script which create files with these suffixes
