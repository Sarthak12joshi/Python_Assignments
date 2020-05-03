import os
type_files = {
  'docx' :'Documents',
  'pdf' :'PDF_Docs',
  'xlsx' :'Excel',
  'jpg' :'images',
  'others' :'others'
}
path = 'D:\\Downloads_Backup'
os.chdir(path)
try:
  for i in type_files.values():
    os.mkdir(i)
except:
  print('The Directory already exists')


lstdir = os.listdir()
for i in lstdir:
  if os.path.isfile(i):
    extension = i.split('.')[-1]
    directory = 'others'
    if extension in type_files.keys():
      directory = type_files[extension]
      f_source = open(i,'rb')
      file_data = f_source.read()
      f_destination = open(directory + '/' + i,'wb')
      f_destination.write(file_data)
      f_source.close()
      f_destination.close()
    else:
      f_source = open(i,'rb')
      file_data = f_source.read()
      f_destination = open(directory + '/' + i,'wb')
      f_destination.write(file_data)
      f_source.close()
      f_destination.close()

      
    '''
    dirf = 'others'
    if extension in type_files.keys():
      dirf = type_files[extension]
    fp = open(i,'rb')
    file_data = fp.read()
    fd = open('D:\\Downloads_Backup\\'+ dirf + '\\' + i,'wb')
    fd.write(file_data)
    fp.close()
    fd.close()
    #os.remove(i)
    '''



#print(lstdir)