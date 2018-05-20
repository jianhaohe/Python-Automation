#coding=utf-8
# '''homework:定义一个函数：
#    函数的功能：将list中元素长度为奇数的元素，最中间的字母大写
# def middile_upper(list):
#     函数体
#
# 例如：list1=['hello','python','testing','where']
# 调用该函数时：print middle_upper(list1)  会打印出 list1=['heLlo','python','tesTing','whEre']
# 用到的知识点：for len()  // %  切片 函数的参数，返回值
# 提示：替换list1中某个元素写法：list1[下标]='替换后的值'；
# '''
#
# ''''''
# list1=['hello','python','testing','where']
# '''第一种方法，
#    1.for循环list中每个元素，
#    2.将把中间字母大写的元素
#    3.定义一个空的list，再用append方法，将每个元素添加到一个新的list去'''
#
# newlist = []
# def middle_upper(list):
# 	for temp in list:
# 		'''判断元素长度是否是奇数，将中间字母大写后再添加到新list'''
# 		if len(temp)%2==1:
# 			midstr=len(temp)//2
# 			newstr=temp[:midstr]+temp[midstr:midstr+1].upper()+temp[midstr+1:]
# 			newlist.append(newstr)
# 		else:
# 			newlist.append(temp)   #将不需要大写的元素，直接添加到新list
# 	return newlist
# print(middle_upper(list1))
#
#
#
# '''第二种方法
# 	1.先循环这个list的长度，用for in range
# 	2.再讲需要大写的元素直接替换：用list[下标]='中间字母大写后的值'
# '''
# def middle_upper(list):
# 	'''list中的每个元素用list[下标]来表示'''
# 	for i in range(len(list)):
# 		mid=len(list[i])//2
# 		if len(list[i])%2==1:
# 			newstr=list[i][:mid]+list[i][mid:mid+1].upper()+list[i][mid+1:]
# 			list[i]=newstr
# 	return list
# print(middle_upper(list1))
#
#
#
# '''面象对象编程
# '''
#
# '''
# 背景：为什么要学类
# 	 1.当我们写了很多用例，我们需要组织用例以及测试执行获取测试报告，需要用到标准库unittest（其实就是一个库里面的类）；
#      2.自动化常用的 driver.find_elements_by_xpath(''),其实也是去调用selenium里面一个类的方法
# '''
#
#
#
# '''
# 面象对象俩个重要的概念：类（class）和实例（instance）
# 类是抽象的：用来描述具有相同属性和相同方法的对象的集合;
# 		  比如说人类；student类;员工类：
# 		            相同的属性：比如都有眼睛，鼻子。
# 		            相同的方法（功能）：吃饭睡觉，说话
# 实例：是根据类创建出来的具体的对象；
# 	   比如某一个人小明，某一个学生，高三班的张三；
# 		            每个对象有相同的属性和方法，但是属性的值都不一样。
# 实例化：创建一个类的实例，类的具体的对象;
#
#
# '''
#
# #创建一个员工类：class +类的名称，首字母一般大写
# class Employee:
# 	pass  #类体
# Employee
#
#
# #创建一个类的实例对象:实例化类其他编程语言中一般用关键字 new，在python中类似函数调用方式
# '''创建员工类的第一个实例化对象'''
# Emp1=Employee()
# '''创建员工类的第二个实例化对象'''
# Emp2=Employee()
# print(Emp1,Emp2)  #打印出来的结果说明，emp1，emp2是Employee类里面的一个对象
#
#
# #可以自由的给实例绑定一个属性
# Emp1.name='张三'
# Emp1.age='18'
#
# Emp2.name='李四'
# Emp2.age='20'
# print(Emp1.name,Emp1.age,Emp2.name,Emp2.age)  #打印出刚刚新增的属性的值
#
# '''
# 背景：由于类（具有相同属性的对象的集合）可以起到模板的作用；我们可以把实例对象具有相同的或必要的属性绑定在类中（例如：name，age，salary）
# 	 通过特殊的__init__方法，创建实例的时候，就把属性自动绑定上去了。
# 						 列如：创建了一个员工C的实例对象，它就用有name，age等属性了
#
# 概念：
# 类方法：类中定义的函数。（第一个参数是self外，其他和普通函数一样）
# self:代表的就是实例本身（比如Emp1）.
# __init__方法：
# 	1.类中的特殊的方法，第一个参数永远是self，所以在init方法内部，可以将各种属性绑定到self上（因为self所指向的就是所创建的实例本身）
# 	2.******每当你创建了一个类的实例，就会自动去调用这个方法;
# 	4.在init方法内部，通过self将每个对象相同的属性绑定上去，例如：self.name=name
#
# '''
#
# #如何理解，self代表实例对象
# class Test1:
# 	def test(self):
# 		print ('self代表的是%s'%self)
#
# a=Test1()
# print('实例对象a：%s'%a)   #打印实例对象a
# a.test()                 #调用Test1里面的test方法，打印self。
# #上面2行打印出来的结果完全一样，说明了self代表的就是这个实例对象本身
#
#
# #理解__init__ :比如绑定属性name，age
#
# class Employee2:
# 	def __init__(self,name,age,years):
# 		self.name=name
# 		self.age=age
# 		self.years=years
# 	def display_info(self):
# 		'''展示员工基本信息方法'''
# 		print('名字为%s;年龄为%s,工作年限%d'%(self.name,self.age,self.years))
#
#
# #创建2个实例对象，员工3和员工4
# Emp3=Employee2('wangwu','28',3) # 注意：有了init方法后，创建实例的时候需要传入和init方法同样的参数，self参数不用传，python解释器会把实例变量传进去
# Emp4=Employee2('xiaoliu','30',5)
#
#
#
# #上面讲对象的属性绑定之后，类中定义的方法可以共用这几个变量（name，age），下面调用Employee2里面的展示员工基本信息的方法
# Emp3.display_info()   #打印员工3的名字，年龄，工作年限
# Emp4.display_info()   #打印员工4的名字，年龄，工作年限
#
#
#
#
#
# '''实例：写一个员工类，统计员工的总人数，展示员工的基本信息，根据员工的工作年限评判员工等级
# 1.定义一个类变量,统计员工的人数
# 	类变量:在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。
# 2.增加类的方法；评判员工等级
# '''
#
# class Employee3:
# 	'''第一步：新建一个员工类'''
# 	empCount=0   #定义一个类变量，初始值为0
# 	def __init__(self,name,age,years):
# 		''''''
# 		self.name=name
# 		self.age=age
# 		self.years=years
# 		Employee3.empCount+=1   #上面所讲，因为每次实例化一个对象，会自动调用init方法，所以，员工数量+1的语句需要写在init方法里面
#
# 	def display_info(self):
# 		'''展示员工基本信息方法'''
# 		print('员工%s;年龄为%s,工作年限%d'%(self.name,self.age,self.years))
#
# 	def displaycount(self):
# 		'''统计员工人数'''
# 		print("员工总数 %d" % Employee3.empCount)
#
# 	def EmpRank(self):
# 		'''评定员工等级'''
# 		if self.years>10:
# 			print ('P1')
# 		elif self.years>5:
# 			print  ('p2')
# 		elif self.years>2:
# 			print  ('p3')
# 		else:
# 			print  ('p4')
#
# '''第二步，创建三个实例化对象'''
# A=Employee3('zhangsan','26',3)
# B=Employee3('lisi','26',2)
# C=Employee3('lisi','26',8)
#
#
# '''
# 调用类的属性和方法
# '''
# A.display_info(),A.EmpRank()    #调用类中的俩个方法，会打印员工的基本信息，和等级
# B.display_info(),B.EmpRank()
# C.display_info(),C.EmpRank()
# A.displaycount()                #打印统计员工总数的值，这里是3
#
#
#
#
# '''
#  继承 ：代码的重用
#  class+类名+（继承的类名）：
# 比如 class  Test(object):
#       默认为object类，这是所有类最终都会继承的类，所以我们上面新增的类，类名称后面没有写括号（）
# '''
#
# '''写一个父类，再写一个子类，去继承父类中间的方法'''
#
# class Parent():    #定义一个父类
# 	parentattr=100
# 	def __init__(self):
# 		print('这是父类的init方法')
# 	def parentmethon(self):
# 		print('这是父类的普通方法')
#
#
# class Child(Parent):   #定义一个子类
# 	def __init__(self):
# 		print('这是子类的init方法')
# 	def childmethon(self):
# 		print('这是子类的方法')
#
# #实例化(子类)对象
# chi=Child()
#
# #子类去调用父类的方法
# chi.parentmethon()


'''
总结：
函数式编程：各函数相互独立，无共用数据
面象对象编程：
1.将数据和逻辑封装起来（增强安全性和简化编程）
2.方便调用，不需要知道具体的实现细节
		练习：本文件写一个类，其它文件来调用这个类里面的方法
3.代码重用，通过继承机制

'''




'''操作txt文件
   open：打开一个文件
   read：读文件
   write：写入数据
   close：关闭文件
'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式。
'''
'''例如打开一个以写的模式打开txt文件'''
file=open('test.txt','w')   #打开一个文件，如果文件不存在，会自动去创建，如果有这个文件，会覆盖
print(file.name)             #查看文件名
print(file.closed)           #查看文件是否关闭，关闭（True），打开（False）
print(file.mode)             #查看文件的读写模式，这里会打印 'w'

#写入write
file.write('helloworld')    #在test1.txt 写入数据，如果需要换行：\n表示换行

#关闭文件
file.close()                #关闭文件
'''
读文件的数据：需要先close，再open，在read
例如：读文件数据，'''
file=open('test.txt','r')  #以读的模式，打开上面写入的文件
print(file.read())          #再读数据，会打印出 helloword
file.close()                #读完之后再关闭

'''
追加模式：a
	1.如果每次用w模式去写同一个txt文件，会覆盖改文件里面已有的数据
	2.所以想在上面的test1.txt文件后面增加新的数据，用a模式

'''
file=open('test.txt','a')
file.write('\n这是第二行')   #此时你再去看test.txt文件，第二行新增了数据'这是第二行'
file.close()



'''
以上写文件的方式，先打开open，再write写数据，再关闭该文件close，在去open，再去读数据read
保证无论是否出错都能正确地关闭文件:用with open
'''
with open('test.txt','a+') as f:
	f.write('\n这是第三行')  #此时你再去看test.txt文件，第三行新增了数据'这是第三行'
print(f.closed)   #此时查看文件的关闭状态，打印True，文件自动关闭



'''
操作excel
xlwt:写入excel表格 ,用这个之前需要先导入模块 xlwt: import xlwt
xlrd:读取excel,用这个之前需要先导入模块 xlwt:import xlrd
'''

'''注意：excel表中取值也是用索引，也是从0开

   比如：(行的索引，列的索引)
        (0,0)表示第一行，第一个空格
       （0，3）表示第一行的第4个空格里面的值
       （3，0）表示第4列，第一个空格里面的值
'''

import  xlwt,xlrd

'''excel写数据'''
execel=xlwt.Workbook()                  #新建一个excle表格
sheet=execel.add_sheet('sheet1')        #创建一个sheet
#在sheet中写入数据，0，0，表示excel表格中的第一行，第一列
sheet.write(0,0,'username')
execel.save('0519.xls')                #保存这个excel文件，名称叫0529.xls,此时打开文件第一行第一列写入了数据'username'

'''

'''

'''练习
将一个数组中的每个元素依次写入excel表格的第一行
'''
list=['username','password','15902127953']


execel =xlwt.Workbook()             # 新建一个excle表格
sheet = execel.add_sheet('sheet1')  # 创建一个sheet
for i in range(len(list)):
	'''list中的元素用list[下标]表示'''
	sheet.write(0, i,list[i])       # 循环list，依次写入数据
execel.save('0519.xlsx')            #循环结束之后，再保存excel。此时打开excel，第一行数据就是list中的每个元素



'''将list中的值依次写入第一列'''
excel=xlwt.Workbook()
sheet=excel.add_sheet('test')
for i in range(len(list)):
	sheet.write(i,0,list[i])
excel.save('0519.xls')



'''
xlrd:读取excle中的数据
'''
excel=xlrd.open_workbook('0519.xls')     #先打开一个已有的excel文件
sheet=excel.sheet_by_index(0)            #获得第一个sheet的数据

print(sheet.nrows)                       #打印excle的行数
print(sheet.ncols)                       #打印excle的列数

print(sheet.row_values(0,1,2))           #获取行的数据，结果应该是空格

#上面的0表示第一行，1，2表示从第几格取到第几格(类似切片，包含开始，不包含结尾)
				#所以上面取的值应该是第一行的，第二格里面的值

print(sheet.col_values(0,1,2))           #或取列的数据，结果应该是第一列，第二个空格里的值'password'




'''excel表格写入测试数据，自动化用例再分别去读取这些数据的实例，没讲完，下节课再讲解'''


'''homework
还是写一个简单的类吧，理解一下类
写一个"测试登录"的类
1.类中写一个登录方法，
2.创建实例去调用里面的登录方法（登录我发给大家的本地网站，或者快递100的网站）
      
'''
from selenium import webdriver
class Logintest:
	'''这是类变量，打开浏览器，我已经帮你定义好了，下面的你们补充'''
	driver=webdriver.Chrome()




'''       
实现效果
每创建一个实例化对象就等于执行了一个具体的登录测试用例，
只是每个测试用例的测试数据用户名和密码不一样，
'''
#下面就是一个测试用例1
case1=Logintest(传入数据)   #创建一个实例化用例
case1.你写的登录方法名称      #调用你写的登录方法

#测试用例2
case2=Logintest(传入数据)   #创建第二个实例化用例
case2.你写的登录方法名称      #调用你写的登录方法