import os

import shutil

# List of programming languages and their corresponding file extensions

languages = {

    'Python': ['.py'],

    'Java': ['.java'],

    'JavaScript': ['.js'],

    'C++': ['.cpp', '.c', '.h', '.hpp'],
    
    'Bash': ['.bash', '.sh'],

    'HTML': ['.html'],

    'CSS': ['.css'],

    'PHP': ['.php'],

    'Ruby': ['.rb'],

    'Swift': ['.swift'],

    'Go': ['.go'],

    'Perl': ['.pl'],

    'Lua': ['.lua'],

    'SQL': ['.sql'],

    'XML': ['.xml'],

    'JSON': ['.json'],

    'YAML': ['.yaml', '.yml']

}

try:

    # Get the root directory of the repository

    root_dir = os.getcwd()

    # Create language folders in the repository root directory if they don't exist

    for lang in languages:

        lang_dir = os.path.join(root_dir, lang)

        os.makedirs(lang_dir, exist_ok=True)

    # Move files to corresponding language folders

    for root, dirs, files in os.walk(root_dir):

        for file in files:

            for lang, exts in languages.items():

                if any(file.endswith(ext) for ext in exts):

                    lang_dir = os.path.join(root_dir, lang)

                    if os.path.dirname(root) != lang_dir:

                        shutil.move(os.path.join(root, file), os.path.join(lang_dir, file))

except Exception as e:

    print(f"Error: {e}")

