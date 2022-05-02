import os
#enter file path
path = '/home/rdp/rajput/railway/EngDAta/Data_ENG_MOdel/0-70'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
