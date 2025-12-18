import os 
path = "temp_directory"
if not os.path.exists(path):
    os.makedirs(path)
for i in range(20):
    inner_path = os.path.join(path,"dir_"+ str(i))
    if not os.path.exists(inner_path):
        os.makedirs(inner_path)
        
        
        
        
                
def  create_folder(path):
  if not os.path.exists(path):
      os.makedirs(path)
  for i in range(20):
      inner_path = os.path.join(path,"dir_"+ str(i))
      if not os.path.exists(inner_path):
        os.makedirs(inner_path)
create_folder(path)
from create_folder import create_folder
create_folder(path)        