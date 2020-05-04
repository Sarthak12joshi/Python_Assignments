class Student:
  def __init__(self,fee = 0):
    self.fee = fee
    print('The fee is {}'.format(self.fee))
  def pay_fee(self,amount):
    self.fee = self.fee + amount
  def get_fee(self):
    return self.fee
  def name(self,name = 'ENTER THE NAME'):
    self.name = name
    print('The name of student is {}'.format(self.name))
  def clas(self,clas):
    self.clas = clas
    print('{} is in {} class'.format(self.name,self.clas))
  def dob(self,dd,mm,yy):
    self.dd = str(dd)
    self.mm = str(mm)
    self.yy = str(yy)
    print('The Date of birth of student {} is '.format(self.name) + self.dd + '/' + self.mm + '/' + self.yy)

student_1 = Student(1000)
student_1.pay_fee(5000)
print(student_1.get_fee())
student_1.name('Sarthak')
student_1.clas('Python')
student_1.dob(12,1,1997)
#student_1.dob(12,01,1997)