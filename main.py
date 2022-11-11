import os
from os import listdir
import pyautogui as pygui
from src.utils.new_file import New_file
from src.utils.binary_tree import Tree
from time import sleep

#? Constants
PATH = 'D:\\2022\Academlo\Algoritmos - Python\RPA\\'
DIRS = ['5Kbits\\', '100kbits\\', 'Mbits\\']

#? Go to Path folder in windows 10
pygui.hotkey('win','e', interval=0.5)
pygui.hotkey('alt','d', interval=0.5)
pygui.write('D:\\2022\Academlo\Algoritmos - Python\RPA', interval=0.1)
pygui.press('enter', interval=0.5)

#? Read files from my folder
files = [file for file in listdir(PATH) 
            if os.path.isfile(os.path.join(PATH, file))]
print(files)

#? Create a binaryTree with data File
for i in range(0, len(files)):
  name = files[i]
  size = os.path.getsize(PATH + '/' + files[i])
  path = PATH + name
  file = New_file(name, size, path)

  if not i:
    list = Tree(file)
  else:
    list.insert(file)

#? Create directories for save each file
for dir in DIRS:
  if not os.path.exists(PATH + dir):
    sleep(0.5)
    os.mkdir(PATH + dir)

#? Move files to their directories for size
for file in list.inorder([]):
  print(file.name)
  sleep(0.5)
  if file.size < 5000:
    os.rename(file.path, PATH + DIRS[0] + file.name)
  elif file.size < 100000:
    os.rename(file.path, PATH + DIRS[1] + file.name)
  else:
    os.rename(file.path, PATH + DIRS[2] + file.name)
