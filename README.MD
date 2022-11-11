# Project RPA with Python

This is a Robotic Process Automation project with Python. The main goal, keep the download workspace free and organised automatically using a stack data structure with stack sorting algorithm or using a BST data structure.

## Virtual environment

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Please check this post [.venv](https://www.linkedin.com/pulse/python-venv-qu%25C3%25A9-son-para-sirven-jorge-armando-blanquicett-matos/?trackingId=9MTYA26VFBImOjkwaXsSag%3D%3D) 
 if you don't know how python virtual environments works. 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Import usage in main.py

```python
import pyautogui
# PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

import os
# This module provides a portable way of using operating system dependent functionality

os.getenv
# Return the value of the environment variable key as a string if it exists, or default if it doesn’t.

from os import listdir
# Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries
```

## Knowing the position of things on the screen

```python
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
```

## .env file
All real projects use an .env variable with information that you would not be willing to have exposed, don't lag behind, but if this becomes a problem, hardcode the main.py.

```env
BASE_PATH=/YOUR/PATH/TO/DOWNLOAD/STAGE
```
## Stack option -> List files in your chosen bucket

```python
import os
from os import listdir


BASE_PATH = os.getenv('BASE_PATH')
print(BASE_PATH)
onlyfiles = [f for f in listdir(BASE_PATH) 
if os.path.isfile(os.path.join(BASE_PATH, f))]

print(onlyfiles)

for i in onlyfiles:
    print(i, os.path.getsize(BASE_PATH+'/'+i))
```

```bash
python test_stack.py
```

```bash
/Users/jorgeabm/Downloads/buckets
['.DS_Store', 'f1.txt', 'f2.txt']
.DS_Store 6148
f1.txt 96775
f2.txt 12096
```

## BST option tested in windows 10

this is an alternative to view the results using a binary tree data structure.

```bash
python main.py
```
## References to the original respository 
Most of respository code was taken from the repository of Prof. Jorge Blanquicett. if you want to see it, you can use the link below:
[JORGE BLANQUICETT](https://github.com/JBlanquicettAcademlo/python_algorithms)

## License
[MIT](https://choosealicense.com/licenses/mit/)