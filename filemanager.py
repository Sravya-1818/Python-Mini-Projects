import os
def create_file(filename):
    try:
        with open(filename,'x') as file:
            print(f"File name {filename} created successfully")
    except FileExistsError:
        print("file name already exits")
    except Exception as E:
        print("an error has occured")
def view_all_files():
    files=os.listdir()
    if not files:
        print("files does not exist")
    else:
        print("files exist")
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} succesfully deleted")
    except FileNotFoundError:
        print("file not found")
    except Exception as E:
        print("an error has occured")
def read_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read
            print(f"content of file {filename} is {content}")
    except FileNotFoundError:
        print("file not found")
    except Exception as E:
        print("an error has occured")
def edit_file(filename):
    try:
        with open(filename,'a') as file:
            content=input("Enter data to add")
            file.write(content+"\n")
            print("File updated succesfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as E:
        print("an error has occured")
def main():
    while True:
        print("--------------FILE MANAGEMENT APP-------------")
        print("""1.Create  File
                 2.View All Files
                 3.Delete File
                 4.Read File
                 5.Edit File
                 6.Exit App""")
        choice=input("enter your choice(1-6)")
        if choice=='1':
            filename=input("ENTER FILENAME TO CREATE")
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input("ENTER FILENAME TO DELETE")
            delete_file(filename)
        elif choice=='4':
            filename=input("ENTER FILENAME TO READ")
            read_file(filename)
        elif choice=='5':
            filename=input("ENTER FILENAME TO EDIT")
            edit_file(filename)
        elif choice=='6':
            print("Closing the app............")
            break
        else:
            print("Enter the choice in range 1-6")
if __name__=="__main__":
    main()
