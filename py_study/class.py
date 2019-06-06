# -*- coding: utf-8 -*-
class Animal:        # 定义父类
		def __init__(self):
			print "调用父类构造函数"
 
		def animalMethod(self):
			print '调用父类动物方法'
 
		def setAttr(self, attr):
			Animal.animalAttr = attr
 
		def getAttr(self):
			print "父类动物属性 :", Animal.animalAttr
		def run(self):
			print "动物跑"
 
class Wolf(Animal): # 定义子类
		def __init__(self):
			print "调用子类构造方法"
 		def wolfMethod(self):
			print '调用子类方法'
		def run(self):
			print "狼翘着尾巴跑"
class Fish(Animal):
	"""docstring for Fish"""
	def __init__(self, arg):
		super Fish, self).__init__()
		self.arg = arg
		
class People():
	pass
class Hybrid(Animal,People):
		def __init__(self):
			print "Hybrid的多继承"
 		pass
a = Animal()        #实例化父类
c = Wolf()          # 实例化子类
a.run()
c.run()
'''c.wolfMethod()      # 调用子类的方法
c.animalMethod()     # 调用父类方法
c.setAttr(400)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值
'''
'''print issubclass(Hybrid,Animal)
print issubclass(Hybrid,People)
print issubclass(Hybrid,Wolf)'''