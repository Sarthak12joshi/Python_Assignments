class Student:
  def __init__(self,name,gender,marks):
    self.name = name 
    self.gender = gender
    self.marks = marks
  def getName(self):
    return self.name
  def setName(self,name):
    self.name = name
  def getGender(self):
    return self.gender
  def setGender(self,gender):
    self.gender = gender
  def getMarks(self):
    return self.marks
  def setMarks(self,marks):
    self.marks = marks

student_data = []
File_1 = open('File1.csv','r')
for line in File_1:
  data = line.strip().split(',')
  st = Student(data[0],data[1],data[2])
  student_data.append(st)
print(len(student_data))
for i in range(0,10):
  print(student_data[i].getName())
print('-'*15)
student_data.sort(key = Student.getMarks)
for i in range(0,10):
  print(student_data[i].getName() +"  " + str(student_data[i].getMarks()))



