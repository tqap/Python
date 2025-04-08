import os

def file_checker(file_name):

    current_directory = os.getcwd()
    parent_directory = "nothing"
    file_found = False

    while True:

        for root, dirs, files in os.walk(current_directory):
            if file_name in files:
                print(f"File found at : {os.path.join(root, file_name)}")
                file_found = True
                break
        
        if file_found:
            break
        
        parent_directory = os.path.dirname(current_directory)

        if current_directory == parent_directory:
            print(f"The file named {file_name} is not found in {os.getcwd()}")
            break

        current_directory = parent_directory

if __name__ == "__main__":
    file_name = input("Please enter the name of the file (q to exit) : ")
    while file_name != "q":
        file_checker(file_name)
        file_name = input("Please enter the name of the file (q to exit) : ")