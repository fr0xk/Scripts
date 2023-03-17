import os

import subprocess

import pylint.lint

def main():

    # get all .py files in current directory

    files = [f for f in os.listdir() if f.endswith('.py')]

    for file in files:

        try:

            # use various linters to check for errors

            subprocess.run(['flake8', file], check=True)

            subprocess.run(['pycodestyle', file], check=True)

            pylint_output = pylint.lint.Run([file], exit=False)

            pylint_output.reporters.append(MyReporter())

            pylint_output._do_exit()

        except Exception as e:

            print(f"{file}: {e}")

class MyReporter(pylint.reporters.BaseReporter):

    # custom reporter that outputs linting results in a human-readable format

    def __init__(self):

        super().__init__()

        self.lint_messages = []

    def _display(self, layout):

        for message in self.lint_messages:

            print(message)

    def handle_message(self, msg):

        # ignore messages about missing docstrings

        if msg.msg_id == 'C0114':

            return

        # format message with line number, severity, description, and suggestion

        line = msg.line or '?'

        col = msg.column or '?'

        severity = msg.category[0].upper()

        description = msg.msg

        suggestion = msg.symbol

        message = f"{msg.path}:{line}:{col}: {severity}: {description} ({suggestion})"

        self.lint_messages.append(message)

if __name__ == '__main__':

    main()

