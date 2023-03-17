import os

import subprocess

def main():

    # get all .py files in current directory

    files = [f for f in os.listdir() if f.endswith('.py')]

    for file in files:

        try:

            # use various linters to check for errors

            subprocess.run(['flake8', file], check=True)

            subprocess.run(['pycodestyle', file], check=True)

            subprocess.run(['pylint', '--disable=all', '--enable=F,E,W,C,R', file], check=True)

        except subprocess.CalledProcessError as e:

            print(f"{file}: {e}")

if __name__ == '__main__':

    main()

