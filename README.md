# many_mimetypes_to_one_suffix
Serving files with the suffix where is linked more than one mimetype in `mime-db.json`

If we want to use official github pages database for mimetype [mime-db](https://github.com/jshttp/mime-db/blob/master/db.json), we find out that some file suffix can be define with more than just one mimetype.

This repo creates files with suffix, where is not determined the exact one mimetype. So we can study which certain headers are sent by github pages server.

This repo contains two script.

* python script to find suffixes which has more mimetypes
* shell script which create files with these suffixes

# List of conflict extensions to 17.3.2022

```
bdoc     {'application/x-bdoc', 'application/bdoc'}
mpp      {'application/dash-patch+xml', 'application/vnd.ms-project'}
exe      {'application/x-msdos-program', 'application/octet-stream', 'application/x-msdownload'}
dll      {'application/octet-stream', 'application/x-msdownload'}
deb      {'application/octet-stream', 'application/x-debian-package'}
dmg      {'application/octet-stream', 'application/x-apple-diskimage'}
iso      {'application/octet-stream', 'application/x-iso9660-image'}
msi      {'application/octet-stream', 'application/x-msdownload'}
asc      {'application/pgp-keys', 'application/pgp-signature'}
ac       {'application/vnd.nokia.n-gage.ac+xml', 'application/pkix-attr-cert'}
rtf      {'application/rtf', 'text/rtf'}
key      {'application/vnd.apple.keynote', 'application/x-iwork-keynote-sffkey'}
numbers  {'application/vnd.apple.numbers', 'application/x-iwork-numbers-sffnumbers'}
pages    {'application/x-iwork-pages-sffpages', 'application/vnd.apple.pages'}
org      {'application/vnd.lotus-organizer', 'text/x-org'}
stl      {'model/stl', 'application/vnd.ms-pki.stl'}
pdb      {'application/x-pilot', 'application/vnd.palm'}
rar      {'application/vnd.rar', 'application/x-rar-compressed'}
prc      {'application/x-pilot', 'application/x-mobipocket-ebook', 'model/prc'}
wmz      {'application/x-ms-wmz', 'application/x-msmetafile'}
wmf      {'image/wmf', 'application/x-msmetafile'}
emf      {'image/emf', 'application/x-msmetafile'}
obj      {'model/obj', 'application/x-tgif'}
xlf      {'application/xliff+xml', 'application/x-xliff+xml'}
xml      {'text/xml', 'application/xml'}
xsl      {'application/xslt+xml', 'application/xml'}
3gpp     {'audio/3gpp', 'video/3gpp'}
mp3      {'audio/mp3', 'audio/mpeg'}
m4a      {'audio/mp4', 'audio/x-m4a'}
wav      {'audio/wave', 'audio/x-wav', 'audio/wav'}
ra       {'audio/x-realaudio', 'audio/x-pn-realaudio'}
bmp      {'image/bmp', 'image/x-ms-bmp'}
jpm      {'image/jpm', 'video/jpm'}
sub      {'text/vnd.dvb.subtitle', 'image/vnd.dvb.subtitle'}
ico      {'image/x-icon', 'image/vnd.microsoft.icon'}
pcx      {'image/vnd.zbrush.pcx', 'image/x-pcx'}
x3db     {'model/x3d+fastinfoset', 'model/x3d+binary'}
x3dv     {'model/x3d-vrml', 'model/x3d+vrml'}
```
