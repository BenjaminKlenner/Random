class Person:
  def __init__(self,name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def myfunc(self):
    print("Hello my name is {}, I am a {} year old {}".format(self.name,self.age,self.gender))

p1 = "John"
p2 = input("How old are you?")
p3 = "male"
p4 = Person(p1, p2, p3)
p4.myfunc(p1, p2, p3)
