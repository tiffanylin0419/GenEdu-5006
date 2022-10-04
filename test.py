class Demo:
	def __init__(self):
		self.name = "Python" 
	def hello(self):
		print("hello",self.name)
d = Demo() 
print(type(Demo)) 
print(type(d))
print("d.name: %s"%d.name) 
d.hello()
