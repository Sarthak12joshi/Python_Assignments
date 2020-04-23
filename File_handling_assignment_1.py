# Using context management
files_lst = []
path = 'F:\python_assignments\home_work\python-batch2\Data'
with open(path + 'masterfile.txt','r') as file_names:
  for lines in file_names:
    name = lines.strip()
    files_lst.append(name)
print(files_lst)
#for file_name in files_lst:
'''
with open('F:\python_assignments\home_work\python-batch2\Data\' + 'files_lst[0]','r') as Data:
  details = Data.readlines()
  print(details)
'''