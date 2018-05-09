
#python的注释：

#这是一个注释

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''


'''
1.自动化的原理是什么？
    是通过javascript来实现对web元素的操作，他提供了丰富的对页面元素操作的方法
    比如selenium：它将我们要操作的网页内嵌到它自己的网页，然后通过脚本语言（javascript）去执行自动化操作
	    android：adb

    例如：打开谷歌浏览器-打开开发者工具(F12)-切到控制台（console）
	    打开一个浏览器：window.open('url')
	    页面刷新：location.reload()
	    获取浏览器的高度的值：document.body.scrollHeight
	    滚动条顶部滑动至底部：window.scrollTo(0,document.body.scrollHeight)



2.自动化的框架是什么？
    多数是第三方的技术框架，根部不同的产品模型有很多种：web的元素自动捕获识别，windows的窗体识别，基于图像识别
    web自动化主流框架:selenium,robotframework,macaca
    移动端自动化主流框架：appium,macaca,uiautomator2,robotframework


3.自动化的架构是什么？（后面课程继续讲解）
   测试代码的模块化，层级结构，数据驱动，关键字驱动，自动化测试报告，日志和断言系统等待


4.自动化的体系是什么？ （后面课程继续讲解）
   jenkins,doceker


'''



'''python语法基础'''
'''输入与输出
输出：print()在括号中加上字符串，就可以向屏幕上输出指定的文字
     单引号和双引号括起来的东西原样输出
'''
#例如，控制台打印"hello, world"
print('hello, world')

#输出中包含变量
name='hejianhao'  #定义一个字符串变量
where='长沙'
#打印出： 我的名字叫做 hejianhao
print('我的名字叫做',name)
#打印出： 我的名字叫做hejianhao来自长沙
print('我的名字叫做%s来自%s'%(name,where))


'''输入input
Python提供了input可以让用户输入字符串，并存放到一个变量里
'''
name=input("请输入你的用户名:") #将输入的字符串保存到变量name中
print(type(name),name)  #打印name的类型和name的值


'''type查看数据类型'''

'''字符串
   字符串是以单引号‘或双引号“括起来的任意文本。
'''
temp='123'
print('temp的值是%s'%temp)
#如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识  例如： are you"ok, im'ok
str="are you\"ok, im\'ok"
str2='are you\"ok, im\'ok'
print(str,str2)


'''整数和浮点数
   Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一摸一样

'''
a=10
b=12300000
c=1.23
d=1.23e7
print(type(a))
print(type(c))
print(type(d))



#整数和字符创的转换,int(),将字符创转换为整数，str()
a=10
b='10'
c=int(b)
d=str(a)
print(type(d))



'''输入中包含字符串、整数、浮点数联系
   在屏幕下方打印：我的名字叫做hhh年龄30年限1.5
'''
name='hhh'    #%s
age=30        #%d
nianxian=1.5  #%.2f  1.500000

print('我的名字叫做%s年龄%d年限%.2f'%(name,age,nianxian))
print('我的名字叫做{}'.format(name))


'''数组list和元组
   list:是一种有序的集合，可以随时添加和删除其中的元素，用[]表示

'''
list1=['我是谁','我在哪','我在干什么']
print(type(list1))   #查看类型
#list中的元素  索引从0开始，也可以用负数表示，
print(list1[0])
print(list1[-1])

#获取list长度：len
print(len(list1))
#增加元素,insert增加指定位置的元素，参数1为索引值，参数2位增加的元素的值,
list1.insert(1,'我不知道我是谁')
#append 默认增加至list最后一个元素
list1.append('哈哈哈')
print(list1)

#删除元素,remove删除指定的元素，pop删除指定索引的元素，默认是删除最后一个元素
list1.remove('我是谁')
list1.pop(0)
print(list1)


'''list的元素包含list'''
list=['1','2','3',['one','two','three']]
#打印"one"
print(list[3][0])

'''元组,不能增加和删除元素'''
# tuple=(1,2,3,['4','5','6'])
# print(type(tuple))
# print(tuple)
# print(tuple[0])#tuple.append('9')



'''字典dictionary
   字典是除列表之外python中最灵活的内置数据结构类型。
   列表是有序的对象结合，字典是无序的对象集合
   字典当中的元素是通过键-值(key-value)存储和取值。列表通过偏移存取
'''
dict={'name':'zhangsan','age':'18','from':'changsha'}
print(type(dict))
name=dict['name']
print(name)


'''字典中的value包含字典'''
dict1={'zhangsan':{'age':'19','form':'changsha'},'lisi':'18'}

#打印出 '19'
print(dict1['zhangsan']['age'])




'''第一个自动化脚本'''
#安装selenium：  pip install selenium
#将chromedriver放在你python.exe同级目录及下。
from selenium import webdriver    #导入selenium中的webdriver
#driver=webdriver.Chrome()         #打开谷歌浏览器
#driver.get('https:www.baidu.com') #访问指定的网页
#driver.close()                    #关闭浏览器




#打开快递100网站
from selenium import webdriver    #导入selenium中的webdriver
driver=webdriver.Chrome()         #打开谷歌浏览器
driver.get('https://buyer.kuaidi100.com/')
#输入自己的用户名
driver.find_element_by_xpath("//input[@placeholder='手机号/邮箱/用户名']").send_keys('你的用户名')
#输入密码
driver.find_element_by_xpath("//input[@type='password']").send_keys('密码')
#点击登录
driver.find_element_by_xpath("//button[@id='submit']").click()




























