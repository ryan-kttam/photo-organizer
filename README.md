# photo-organizer

This program is intended to help users organize their photos and videos. This program automatically creates folders/ directories by last modified date and add the photos/ videos in the folder. It takes a .zip file as the input, which is a format where Google Photos export photos. 

For example. If the image was taken in April 28th, 2020, it would create a folder called "2020-04-28" and would place all the images taken in that date. 

You will need python 3 to run this program. Additionally, the following packages will need to be installed for python as well.

## pytz
pytz is for converting the time to your timezone. Default is PST.
## zipfile
It is used to unzip the photos.

This program is not limited to photos/ videos. In fact, any format would work. Further testing is required for .rar format. 
