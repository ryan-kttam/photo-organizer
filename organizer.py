import zipfile
# import rarfile
import os
import time
import datetime
import pytz


def photo_organizer(file):
    zf = zipfile.ZipFile(file)
    for f in zf.infolist():
        get_date = zf.getinfo(f.filename).date_time
        access_dt = time.time()
        modified_dt = datetime.datetime(*get_date)
        modified_dt = modified_dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Pacific'))
        folder_name = datetime.datetime.strftime(modified_dt, '%Y-%m-%d')
        file_path = folder_name + '/' + f.filename
        if folder_name not in os.listdir():
            print ('Creating ', folder_name, 'folder.')
        zf.extract(f.filename, path=folder_name)
        os.utime(file_path, (access_dt, modified_dt.timestamp()))
    print ('All the files has been unzipped.')

photo_organizer('Photos (4).zip')