"""Script for setting PYTHONPATH in an already-created virtualenv"""


import os
import sys


venv_dir = sys.argv[1] if len(sys.argv) == 2 else 'env/'
if not os.path.isdir(venv_dir):
    print(f"Python's venv directory '{os.path.abspath(venv_dir)}' doesn't exist!")
    sys.exit(-1)


with open(venv_dir+'bin/activate', 'a') as f:
    f.write('\n\n')
    f.write("export OLD_PYTHONPATH='$PYTHONPATH'\n")
    f.write("export PYTHONPATH='.'")


with open(venv_dir+'bin/postdeactivate', 'w') as f:
    f.write("export PYTHONPATH='$OLD_PYTHONPATH$'")


if not os.path.isdir('src/'):
    os.mkdir('src/')

