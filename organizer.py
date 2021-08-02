import zipfile
# import rarfile
import os
import time
import datetime
import pytz


class photoOrganizer:
    def __init__(self, path):
        self.zf = zipfile.ZipFile(path)

    def get_date(self, file):
        get_date = self.zf.getinfo(file.filename).date_time
        #access_dt = time.time()
        modified_dt = datetime.datetime(*get_date)
        modified_dt = modified_dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Pacific'))
        return modified_dt

    def get_folder_name(self, date):
        folder_name = datetime.datetime.strftime(date, '%Y-%m-%d')
        return folder_name

    def get_file_path(self, folder_name, file):
        file_path = folder_name + '/' + file.filename
        if folder_name not in os.listdir():
            print('Creating ', folder_name, 'folder.')
        self.file_path = file_path
        return file_path

    def organize(self):

        for f in self.zf.infolist():
            modified_dt = self.get_date(f)

            folder_name = self.get_folder_name(modified_dt)
            file_path = self.get_file_path(folder_name, f)

            self.zf.extract(f.filename, path=folder_name)
            os.utime(file_path, (time.time(), modified_dt.timestamp()))

        print ('All the files has been unzipped.')

p = photoOrganizer('C:\Github\photo-organizer\sample_photos.zip')
p.organize()
