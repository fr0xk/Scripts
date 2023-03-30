import os

# Define a function for displaying the contents of a directory

def list_directory(path):

    print("Contents of directory", path, ":")

    for item in os.listdir(path):

        print(item)

# Define a function for creating a new file

def create_file(path, name):

    full_path = os.path.join(path, name)

    with open(full_path, "w") as file:

        file.write("This is a new file.")

# Define a function for deleting a file

def delete_file(path, name):

    full_path = os.path.join(path, name)

    os.remove(full_path)

# Define the main function for the file manager

def main():

    path = "." # Start in the current directory

    while True:

        # Display a prompt and read the user's input

        command = input(f"{path}> ")

        # Handle the "ls" command to list the directory

        if command == "ls":

            list_directory(path)

        # Handle the "cd" command to change the directory

        elif command.startswith("cd "):

            new_path = command[3:]

            if os.path.isdir(new_path):

                path = new_path

            else:

                print(f"{new_path} is not a directory.")

        # Handle the "touch" command to create a new file

        elif command.startswith("touch "):

            name = command[6:]

            create_file(path, name)

            print(f"Created file {name} in {path}.")

        # Handle the "rm" command to delete a file

        elif command.startswith("rm "):

            name = command[3:]

            delete_file(path, name)

            print(f"Deleted file {name} from {path}.")

        # Handle the "exit" command to quit the file manager

        elif command == "exit":

            break

        # Handle an unrecognized command

        else:

            print(f"Unrecognized command: {command}")

# Call the main function

main()

