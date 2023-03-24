import os
import subprocess
import sys
import glob

# Basic Bash feature: Variables
name = "John"
age = 30
print("My name is", name, "and I am", age, "years old.")

# Basic Bash feature: Pipes
p1 = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "txt"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output, err = p2.communicate()
print(output.decode())

# Basic Bash feature: Command substitution
files = subprocess.check_output(["ls"]).decode().split("\n")
print(files)

# Basic Bash feature: Redirecting input and output
with open("file.txt", "r") as f:
    sys.stdout = open("output.txt", "w")
    print(f.read())

# Basic Bash feature: Conditional statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Basic Bash feature: Loops
for i in range(5):
    print(i)

# Basic Bash feature: Functions
def greet(name):
    print("Hello,", name)

greet("John")

# Advanced Bash feature: Command-line arguments
args = sys.argv[1:]
print("Command-line arguments:", args)

# Advanced Bash feature: Exit codes
try:
    os.remove("file.txt")
except OSError as e:
    print(e)
    sys.exit(1)

# Advanced Bash feature: Brace expansion
for i in range(1, 4):
    subprocess.run(f"touch file{i}.txt")

# Advanced Bash feature: Process management
p = subprocess.Popen(["ls", "-l"])
p.wait()
print("Process returned", p.returncode)

# Advanced Bash feature: Environment variables
print("HOME:", os.environ["HOME"])

# Advanced Bash feature: Job control
p1 = subprocess.Popen(["sleep", "10"])
p2 = subprocess.Popen(["echo", "Done"])
p2.wait()

# Advanced Bash feature: Signals
import signal

def signal_handler(sig, frame):
    print("Signal received:", sig)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Advanced Bash feature: Process substitution
p1 = subprocess.Popen(["sort", "file1.txt"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["sort", "file2.txt"], stdout=subprocess.PIPE)
diff = subprocess.check_output(["diff", "-"], stdin=subprocess.PIPE, args=(p1.stdout, p2.stdout))
print(diff.decode())

# Advanced Bash feature: Globbing
for file in glob.glob("*.txt"):
    print(file)

# Advanced Bash feature: Redirection and piping
with open("file.txt", "w") as f:
    f.write("Hello, world!")
subprocess.run(["cat", "<", "file.txt", "|", "grep", "world"])

