import sys
file_list = []
gender = {}
with open('masterfile.txt','r') as source:
  for line in source :
    name = line.strip()
    file_list.append(name)
  print(file_list)
count = 0
for name in file_list:
  with open(name,'r') as student_file:
    for line in student_file:
      data = line.strip().split(',')
      count = count + 1 
      if data[1] in gender:
        gender[data[1]][0] = gender[data[1]][0] + 1
        gender[data[1]][1].write(line) 
      else:
        fp = open(data[1] + '.csv','w')
        gender[data[1]] = [1,fp]
        gender[data[1]][1].write(line)
file_st = sys.stdout
for i,v in gender.items():
  print(i,v[0],file=file_st)
  v[1].close()
print(count)