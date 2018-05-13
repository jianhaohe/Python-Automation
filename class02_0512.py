from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random,time,re,datetime
'''
上节课介绍了python的输入输出，数据类型：字符串、整数、浮点数、列表、元组、字典；type();len();

'''

'''
使用Python的计算:
表达式的语法是直接的：+-*/; 圆括号（()）可用于分组
具有混合类型操作数的运算符将整型操作数转换为浮点型：
'''

#例如
print(10-8*2/3-2)


#先定义一下各种数据类型的变量；
#str1='automation';str2='python';str3='nice';str4='10'
#int1=10;int2=8
#float1=17.0;float2=3.0
#list1=['1','2','3','4'];list2=['one','two']
#tuple1=(1,2) ;tuple2=(3,4)
#dict1={'hunan':'changs','hubei':'wuhan'};dict2={'sichuan':'chengdu'}  #字典没有加减乘除


#加减法，相同的数据类型(int,str,float;list);直接用表达式'+'，
#c=str1+str3+str2  #字符串相加
#c=list1+list2     #list相加
#c=int1+str4       #字符串和整数相加先用str() 或者int()转换
#c=int1+float1     #整数和浮点可以直接相加，
#print (type(c),c)



#乘法*；**运算符来计算权力

# temp=str1*3     #字符串*整数
# print(type(temp),temp)
#print(2**7)     #求2的7次方


#除法
# /总是返回一个浮点数;
#temp=10/2         #结果为5.0而不是5
#print(type(temp),temp)
# 如果想返回整数结果（丢弃任何分数结果），可以使用// ;
#temp=13//2         #结果等于6
#print(type(temp),temp)
# 计算余数使用%：
#temp=13%2         #余数结果为1；常用来判断一个数是否为奇数或偶数
#print(temp)





'''
切片,用"："
字符串和list的长度len,可以被索引,用负数表示；例如 str[0],list[1];len(str);len(list)
1.始终包含开始，并始终排除结尾; 因为[1,10]:[1,5)[5,10]
2.省略的第一个索引默认为零，省略的第二个索引默认为正在切片的字符串的大小。
'''
#例如：
# str1='automation'
# print(str1[-1])           #打印 n
# print(len(str1))          #长度为10
# print(str1[4:6])          #ma
# print(str1[4:10])         #mation
# print (str1[:])           #打印整个字符串；开始和结束索引都省略
# print(str1[:6]+str1[6:])
# print(str1[-6:])

#list切片，可以自己去练习一下
#print(list1[:])
#print(list1[1:3])


#将首字母大写；将某个字符串大写的方法upper()
#str='hello'
# str=str1[:1].upper()+str1[1:]
# print(str)

'''将 字符串最 中间的字母大写'''
# res='world'
# s=len(res)//2
# print(res[:s]+res[s:s+1].upper()+res[s+1:])

'''
为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

Python的循环有两种，
第一种循环是while循环：
第二种是for...in循环


while:只要条件(:)保持为真，循环就会一直执行。
何为真：
1.任何非零整数值都是true; 零是错误的。
  条件也可以是字符串或列表值; 任何长度不为零的东西都是真的，空序列是错误的。<>==<=>=!=
2.循环的主体是缩进,注意，基本块内的每行必须缩进相同的数量
判断一个东西是否为真：用布尔类型
'''
#例如：
#print(bool(10))   #结果为真；打印True
#print(bool(0))    #结果为假；打印True
#print(bool(3>0))  #结果为真；打印True



#用while计算[0,100]的和：1+2+3+4+。。+100
# n=0;sum=0
# while n<101:
#      sum=sum+n
#      n=n+1
# print (sum)

'''练习：当n定义为99时，求【1，100】的和"'''
# n=99;sum=0
# while n>0:
# 	  sum=sum+n
# 	  n=n-1
# print (sum)



'''练习：求x的n次方 2³'''
# print(pow(2,7))
# sum=1;n=2;x=3
# while x>0:
# 	sum=sum*n
# 	x=x-1
# print(sum)

'''n的阶层  例如：5的阶层=5*4*3*2*1'''
# sum=1;n=5
# while n>0:
# 	sum=sum*n
# 	n=n-1
# print(sum)


'''第二种循环：for
for x  in 循环
1:依次把list或tuple中的每个元素迭代出来,
2.并赋值给变量x 
例如：for x in range list1():
'''
#例如： end='' 表示输入结果不换行
# for i in list1:
# 	print (i,end='')
# for i in dict1:
# 	print (i,end='')
# for i in str1:
# 	print (i)


'''
如果您需要迭代一系列数字，需要用到range(取某个范围)
for in range(n1,n2)
1.循环从n1开始，
2.循环的个数=n2-n1，
3.第一个索引默认值为0'''


#例如：
# for i in range(3,10):
# 	print(i)


'''练习：for 循环里面嵌套循环
list=['java','python','php']；
控制台打印出每个元素的每个字母，结果如下：
j
a
v
a
.
.
p

'''
# list=['java','python','php']
#
# for m in list:
# 	for n in m:
# 		print(n)


'''if：结合自动化，为什么要用if，因为一个测试用例操作过程中，有时候需要判断某个元素的条件，状态，再去点击某个元素
if的结构
if  满足条件判断1:
   action1
else:
   action2
如果条件为True:执行action1，反之执行条件2
.else是可选的
'''

#简单的if实例：
# x=85
# if x>60:
# 	print('好')
# else:
# 	print('加油')


'''
精确判断；需要用到多层if else循环
练习：用if写出判断成绩的等级；
      95     了不得
      90-95  优秀
      80-90  良好
      60-80  刚刚好
      60以下  加油

'''
#grade=80
# if grade>=95:
# 	print('1')
# else:
# 	if grade>=90:
# 		print('2')
# 	else:
# 		if grade>=80:
# 			print('3')
# 		else:
# 			if grade>=60:
# 				print('4')
# 			else:
# 				print('5')



'''elif是'else if'的缩写，对于避免过多的缩进非常有用
if   满足条件判断1:
    <执行1>
elif 满足条件判断2>:
    <执行2>
elif 满足条件判断3:
    <执行3>
else:
    <执行4>
'''


'''用elif写出上面的例子'''
#random是取一个随机数；需要先导入python内置的模块import random
# grade=random.randint(1,100)
# print(grade)
# if   grade>95:
# 	print("了不起")
# elif grade>90:
# 	print ('优秀')
# elif grade>80:
# 	print('良好')
# elif grade>60:
# 	print('刚刚好')
# else:
#     print("未及格,你还需努力")




'''
函数：用def语句
1依次是函数名、括号、括号中的参数和冒号；
2然后在缩进块中编写函数体
3函数的返回值用return语句返回,一旦执行到return时，函数就执行完毕

函数的结构：
   def 函数名 （参数1，参数2）：
       函数体
       return是返回值
参数：可选
return：可选，默认是none
'''
#print(abs(10)) #abs是求绝对值的方法；我们自定义一个函数名称叫 abs_my

# def abs_my(x):
# 	if x>0:
# 		return  x     #函数的返回值
# 	else:
# 		return  -x
# print(abs_my(-10))   #函数需要调用：函数名+参数




'''第二个自动化操作'''


'''
第一节课提到的javascript语句：应用到自动化中
	    打开一个浏览器：window.open('url')
	    页面刷新：location.reload()
	    获取浏览器的高度的值：document.body.scrollHeight
	    滚动条顶部滑动至底部：window.scrollTo(0,document.body.scrollHeight)

'''

#driver = webdriver.Chrome()
#driver.get(https://www.kuaidi100.com/)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 滑动滚动条至底部
# time.sleep(2)  # 等待几秒钟再去执行下一步，需要导入python内置模块time:import time
# driver.execute_script('window.scrollTo(document.body.scrollHeight),0') # 滑动滚动条至顶部
# time.sleep(3)  # 等待几秒钟再去执行下一步，需要导入python内置模块time:import time
# driver.execute_script('location.reload()')  # 刷新页面




'''
最简单找元素的方法：
1.打开谷歌，打开开发者工具（F12）
2.点击左上角的inspect按钮，
3.再点击你需要找的元素
4.点击右键-copy-copyxpath
此时该元素的xpath路径已经复制好了
'''





'''函数练习：
写一个自动化的登录函数
参数为url，username，password
返回值为登录后的用户名的值
用快递100举例：

'''



def login(url,username,password):
	driver = webdriver.Chrome()
	driver.get(url)
	#time.sleep(3)  # 等待几秒钟再去执行下一步，需要导入python内置模块time:import time
	#driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 滑动滚动条至底部
	#driver.execute_script('window.scrollTo(document.body.scrollHeight),0') # 滑动滚动条至顶部
	#driver.execute_script('location.reload()')  # 刷新页面
	# 点击登录
	driver.find_element_by_xpath('//*[@id="welcome"]/a[2]').click()
	# 输入你的用户名 send_key
	driver.find_element_by_xpath('//*[@id="name"]').send_keys(username)
	# 输入密码
	driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
	# 点击登录
	driver.find_element_by_xpath('//*[@id="submit"]').click()
	#获取用户名
	name=driver.find_element_by_xpath('//*[@id="userName"]').text
	if name=='傻子才孤单':
		print("pass")
	assert name=='傻子才孤单'

#定义变量url，username，password
url='https://www.kuaidi100.com/'
username='15902127953'
password='test123456'


#调用上面的login函数：
login(url,username,password)








#函数之间可以相互调用：例如testcase1调用登录函数
def testcase1():
	login(url,username,password)

def testcase2():
	login(url,username,password)



#testcase1()  这句话先调用了testcase1函数，testcase1再去调用login函数







'''homework:定义一个函数：
   函数的功能：将list中元素长度为奇数的元素，最中间的字母大写
def middile_upper(list):
    ?????
    ?????
    ?????
    
    
例如：list1=['hello','python','testing','where']
调用该函数时：print middle_upper(list1)  会打印出 list1=['heLlo','python','tesTing','whEre']
用到的知识点：for len()  // %  切片 函数的参数，返回值
提示：替换list1中某个元素写法：list1[下标]='替换后的值'；
'''


