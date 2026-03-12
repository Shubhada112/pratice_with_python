

# #write in file 
 
# #  file = open("sample.txt" , "w")
# # file.write("Hi , I am Shubhada ")
# # file.close()

# #read  file 
# # file = open('sample.txt' , "r")
# # content = file.read()
# # file.close()
# # print(f"---->Content of sample.txt file :     {content}")



# import os 

# def create_file(filename):
#     try:
#         with open(filename , 'x') as f :
#             print(f"File Name {filename} : Created successfully!")
    
#     except FileExistsError:
#         print(f"File Name {filename} already exists")

#     except Exception as E: 
#         print("an error occured")


# # def view_all_files():
# #     files = os.listdir()
# #     if not files:
# #         print("No file found")
# #     else:
# #         print("file is directoey")
# #         for file in files:
# #             if os.path.isfile(file):
# #                 print("file")


# def view_all_files():
#     files = os.listdir()  # list all files and folders
#     if not files:
#         print("No file found")
#     else:
#         print("Files in directory:")
#         for file in files:
#             if os.path.isfile(file):  # ✅ colon here
#                 print(file)           # print actual file name

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print(f"{filename} file has deleted")
#     except FileExistsError:
#         print(f"{filename}  file not found")
#     except  Exception as e :
#         print("en error occurred!")

# def read_file(filename): 
#     try:
#         with open(filename ,'r') as f :
#             content = f.read()
#             print(f"Content of {filename}-->\n {content}") 
#     except FileNotFoundError:
#         print(f"{filename}  file not found")
#     except Exception as e :
#         print("en error occurred!")


# def edit_file(filename):
#     try:
#         with open(filename, 'a') as file:
#             content = input("Enter data to add: ")
#             file.write(content + "\n")
#             print(f"Content added to {filename} successfully")
#     except FileNotFoundError:
#         print(f"{filename} file not found")
#     except Exception as e:
#         print("An error occurred!")

# def main():
#     while True:
#         print(' File Management app')
#         print("1) create file")
#         print("2) view all file")
#         print("3)delete file")
#         print("4)read file")
#         print("5)edit file")
#         print("6) exit")

#         choice = input(" enter your choice betwenn 1-6 = ")

#         if choice=="1":
#             filename = input(" enter  file name : ")
#             create_file(filename)
#         elif choice =="2":
#             view_all_files()
#         elif choice =="3":
#             filename = input(" enter file name you want to delete:")
#             delete_file(filename)
#         elif choice =="4":
#             filename = input("enter you want to read: ")
#             read_file(filename)
#         elif choice =="5":
#             filename = input("enter file you want to edit")
#             edit_file(filename)
#         elif choice =="6":
#             print("close the app")
#             break
#         else:
#             print("invalid syntax")

# if __name__ == "__main__":
#     main()

import os

# ---------------- AUTHENTICATION ----------------
def login():
    USERNAME = "admin"
    PASSWORD = "1234"

    print("---- Login Required ----")
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password!")
        return False


# ----------- CHECK FILE TYPE ----------------
def valid_file(filename):
    if not filename.endswith(".txt"):
        print("Only .txt files are allowed!")
        return False
    return True


# ----------- CREATE FILE ----------------
def create_file(filename):
    if not valid_file(filename):
        return
    try:
        with open(filename, 'x'):
            print(f"File {filename} created successfully!")
    except FileExistsError:
        print(f"{filename} already exists!")
    except Exception:
        print("An error occurred!")


# ----------- VIEW FILES ----------------
def view_all_files():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files:
        print("No .txt files found")
    else:
        print("Files in directory:")
        for file in files:
            print(file)


# ----------- DELETE FILE ----------------
def delete_file(filename):
    if not valid_file(filename):
        return
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print(f"{filename} file not found!")
    except Exception:
        print("An error occurred!")


# ----------- READ FILE ----------------
def read_file(filename):
    if not valid_file(filename):
        return
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nContent of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"{filename} file not found!")
    except Exception:
        print("An error occurred!")


# ----------- APPEND / EDIT FILE ----------------
def edit_file(filename):
    if not valid_file(filename):
        return
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print(f"{filename} file not found!")
    except Exception:
        print("An error occurred!")




# ----------- MAIN PROGRAM ----------------
def main():

    if not login():
        return

    while True:
        print("\nFile Management App")
        print("1) Create file")
        print("2) View all files")
        print("3) Delete file")
        print("4) Read file")
        print("5) Edit file (append)")
    
        print("6) Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            filename = input("Enter file name: ")
            create_file(filename)

        elif choice == "2":
            view_all_files()

        elif choice == "3":
            filename = input("Enter file name to delete: ")
            delete_file(filename)

        elif choice == "4":
            filename = input("Enter file name to read: ")
            read_file(filename)

        elif choice == "5":
            filename = input("Enter file name to edit: ")
            edit_file(filename)

        elif choice == "6":
            print("Closing the app...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()