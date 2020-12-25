from Drives.main import Drives
from Searching.main import Searching
from Database.main import Database


def main():
    search_object=Searching()
    print('enter file to be searched')
    file_input=input();
    # ans1=search_object.find_file_in_all_drives(file_input)
    # dbs=Database()
    # dbs.insert(ans1,file_input)
    #print(ans1)
    dbs=Database()
    database_search_result=dbs.query(file_input)
    if(database_search_result<=0):
        #ans1=search_object.find_file_in_all_drives(file_input)
        ans2=search_object.create_thread(file_input)
        dbs=Database()
        dbs.insert(ans2,file_input)


    drive_obj=Drives()
    available_Drives=drive_obj.get_drives()
    print('total drives in the system')
    for i in available_Drives:
        print(i)


if __name__ == '__main__':
    main()
