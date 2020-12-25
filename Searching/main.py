import os
import re
from threading import Thread

import win32api
from Drives.main import Drives
from Database.main import Database


class Searching:
    global data
    data = []

    def __init__(self):
        pass

    def find_file_in_all_drives(self, file_name):
        rex = re.compile(file_name)
        drive_obj = Drives()
        drives = drive_obj.get_drives()
        for i in drives:
            self.find_file(i, rex)
        return data

    def find_file(self, root_folder, rex):
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print("data from searching")
                    print(os.path.join(root, f))
                    data.append(os.path.join(root, f))
                    break

    def create_thread(self,file_name):
        threads_list=[]
        drive_obj=Drives()
        drives=drive_obj.get_drives()
        for each in range(len(drives)):
            process=Thread(target=self.find_file_in_all_drives,args=(file_name,))
            process.start()
            threads_list.append(process)
        for t in threads_list:
            t.join()
        return data;