import win32api


class Drives:

    def __init__(self):
        self.drives = []

    def get_drives(self):
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self.drives.append(drive)
        return self.drives
