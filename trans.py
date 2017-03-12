import os
from zhtools import simple2tradition

FOLDER_PATH = r'C:\Users\Curry\Desktop\liaoxuefeng'
EXTENSION = ('.html', '.css', '.dat', 'xml', '.txt', '.ncx', '.opf','.xhtml')
filePathList = [FOLDER_PATH + '\\' + each for each in os.listdir(FOLDER_PATH) if each.endswith(EXTENSION)]

NEW_FOLDER_PATH = '_new'
directory = FOLDER_PATH + NEW_FOLDER_PATH
if not os.path.exists(directory):
    os.makedirs(directory)

for filePath in filePathList:
    with open(filePath, 'r', encoding='utf-8') as f:
        test_cn = f.read()
    test_tw = simple2tradition(test_cn)
    new_filePath = filePath.replace(FOLDER_PATH, directory)
    with open(new_filePath, 'w', encoding='utf-8') as f:
        print('save', new_filePath)
        f.write(test_tw)
