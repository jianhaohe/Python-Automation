from selenium import  webdriver
import random,time
'''
while

'''
#计算【1，100】的和； 1+2+3....+100 求
# n,sum=1,0
# while n<101:
#     sum=sum+n
#     n=n+2
# print(sum)



'''
计算n的阶层；n！=n*n-1*n-2  5*4*3*2*1 求积

'''
# n=10;sum=1
# while n>0:
#     sum=sum*n
#     n=n-1
# print(sum)

'''
for 
'''
#用while 写一个n的x次方循环，

'''

for 循环
'''
#javapythonnode
# list1=['java','python','node']
# for temp in list1:
# 	for i in temp:
# 		print(i,end='')

'''
'''



# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in list:
# 	print(i)
# 	sum=sum+i
# print(sum)


#求1-100的和
# sum=0
# for i in range(1,100):
#     sum=sum+1
# print(sum)

# for in 与for in range的区别
#字典，list str
# str1='python'
# for i in  str1:
# 	print(i)
# for i in range(100):

'''
条件判断；if
'''
# grade=int(input('请输入你的成绩：'))
# #如果大于60 及格，输的值小于60；需要努力
# if grade>60:
# 	print('及格')


'''
grade>95 :了不起
grage>90 优秀
grade>80  良好
grade>60  及格
grade<60  需要努力
'''

# x=random.randint(1,100)
# print("随机数x等于：%d"%x)

# if x>95:
# 	print('了不起')
# else:
# 	if x>85:
# 		print('优秀')
# 	else:
# 		if x>80:
# 			print('良好')
# 		else:
# 			if x>60:
# 				print('及格')
# 			else:
# 				print('需要努力')
#elif

# if x>95:
# 	print('了不起')
# elif x>85:
# 	print('优秀')
# elif x>80:
# 	print('良好')
# elif x>60:
# 	print('及格')
# else:
# 	print('需要努力')
#


'''函数
   def 函数名 （参数，）：
       return
'''
#print(abs(10)) #求绝对值

# def def_my(x):
# 	if x>0:
# 		return  x
# 	else:
# 		return  -x
# print(def_my(0))


#//*[@id="welcome"]/a[2]
''''''
url='https://www.kuaidi100.com/'
username='15902127953'
password='test123456'



#写一个登录函数，获取元素的值方法叫做text,返回获得的用户名
#
# def login(url,username,password):
# 	driver = webdriver.Chrome()
# 	driver.get(url)
# 	# 活动滚动条至底部
# 	#time.sleep(3)  # 等待几秒钟再去执行下一步
# 	#driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 	#time.sleep(2)
# 	#driver.execute_script('location.reload()')  # 刷新页面
# 	# 点击某个元素
# 	driver.find_element_by_xpath('//*[@id="welcome"]/a[2]').click()
# 	# 输入你的用户名 send_key
# 	driver.find_element_by_xpath('//*[@id="name"]').send_keys(username)
# 	# 输入密码
# 	driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
# 	# 点击登录
# 	driver.find_element_by_xpath('//*[@id="submit"]').click()
# 	#获取用户名
# 	name=driver.find_element_by_xpath('//*[@id="userName"]').text
# 	if name=='傻子才孤单':
# 		print("pass")
# 	assert name=='傻子才孤单'
# 	return name
#
#
# def testcase1():
# 	login(url,username,password)
#
# def testcase2():
# 	login(url,username,password)
# testcase1()







'''homework
定义一个函数：将list中的每个元素最中间的字母大写
list=['hello','world','java','automaton']
list=['heLlo','woRld','java','autoMaton']

'''

'''
python运算：+—*/，//,%, 
切片：list的切片
while: [1,100]求和，【1，10】求积； x的n次方
for i in；range()
if条件判断；elif
def():
找元素的方法，selenim执行javascript脚本
类 class

'''














