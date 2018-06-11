import smtplib,time
from email.mime.text import MIMEText
from email.header import  Header
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
import unittest




'''******笔记只记录知识点
		 上课的很多练习和演示实际效果，笔记三言俩语已经无法描述，
		 或者看直播录播'''



'''课前复习：
特殊元素定位方法：
svg：用xpath的*[name()='svg']
frame:switch_to_frame('id'、'name'、'webelement')   webelement:指该元素本身

为什么要学unittes：方便执行、fail的用例不影响后面的用例
unitest:用来组织用例、执行用例、判断测试结果、集成测试报告
        1.测试方法已test开始，否则不被unittest失败，执行顺序根据（0-9，A-Z,a-z）
        2.setup、teardown：每个用例开始和结束后的动作
          setupclass、teardownclass：所有用例执行前、结束后的动作。（@classmethon）
          以上俩中可以共存
        3.用例结果成功是.失败是F.报错是e
        4.verbosity(0,1,2)
        5.参数stream可以将结果输入到测试报告，HTMLTestRunner
运行三步过程：
		   unittest.main()
           testcase=unittest.TestSuite()
           
           testcase.addTests(测试类名('case名称'))
           testcase.addTests(unittest.TestLoadr().loadTestfromTestcase(测试类名))
           testcase.addTests(unittest.TestLoadr().loadTestfromname('模快名.测试类名'))
           
           
           unittest.TextTestRunner().run(testcase)

集成测试报告：
dir='路径'
time=time.strftime('%Y-%m-%d-%H-%M',time.localtime())     #获取当前时间
file=open(dir,'wb')

runner=HTMLTestRunner(stream=file)
runner.run(testcase)



或者用with打开测试报告
with open(dir,'wb') as f:
    runner=HTMLTestRunner(stream=file)
	runner.run(testcase)         
           

'''





'''常用javascript方法：

selenium中常用方法例如：
判断元素是否存在：       is_dispaly
获取元素的文本：        webelement.text
获取页面的标题：        driver.title
获取元素的某个属性的值：  webelement.get_attribute('属性值')


上面的selenium方法同样的，都可以用js来实现，当遇到selenium不能解决的可以考虑通过执行js；js和xpath一样非常的灵活，强大

JavaScript可以获取浏览器提供的很多对象，并进行操作。
window就是一个对象；表示浏览器窗口
打开新的浏览器窗口：window.open(url)
				 window.innerWidth
				 window.innerHeight
				 window.outerWidth
				 window.outerHeight
				 滚动条：window.scrollTo(0,document.body.scrollHeight)
	                    window.By(0,document.body.scrollHeight)
				 非页面类型的滚动条：document.getElementsById(id)[0].scrollTop=''
				 
location当前页面的URL对象
获取当前url:location.href获取
更改当前url:location.assign()
刷新：location.reload()

document:表示当前页面对象
		 HTML在浏览器中以DOM形式表示为树形结构，
		 document对象就是整个DOM树的根节点,然后去操作子节点
获取当前标题：document.title
输入文本的值：document.getElementsById(id)[0].value=''
操作标签：   document.getElementsById(id)[0].click()
更改属性：   document.getElementById('vip').style.visibility='visible'

'''






'''python发送邮件：
导入email模块
导入smtplib模块；
具体的一些定义看ppt，这里不再描述'''





'''例一：'''
def sendemail1():
	'''发送邮件函数'''



	'''第一步，创建数据'''
	smtpserver = 'smtp.exmail.qq.com'  # 定义变量，邮件服务器
	sender='15902127953@163.com'       #定义变量，发送人
	password='test123456'              #发送人的密码
	receiver = 'xxxxxxx@163.com'       #定义变量， 接收人


	'''第二步，构建邮件内容，通过email中的类MIMEText'''
	content = MIMEText('第一次通过python发送邮件', 'plain', 'utf-8')


	'''邮件发送过程，通过smtplib模块中的SMTP类'''
	server = smtplib.SMTP(smtpserver, 25)   #实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

	server.set_debuglevel(1)                #打印log

	server.login(sender, password, )        #先登录邮件服务器。参数1：发送人；参数2：密码

	server.sendmail(sender, receiver,content.as_string())   #发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

	server.quit()                           #退出邮件服务器

#sendemail1()
#调用发送邮件函数，如果你用的是企业邮箱，此时你已经收到一封通过由python发送的邮件，但是没有主题和发送人；
				#如果你用的是网易邮箱，可能会报错，代码554（收件人和发件人不同），继续看下面的例子




'''例二：
通过MIMIText绑定主题和收件人
第一步和第三步和上面完全一样，只是在第二步通过MIMEText声明一下发件人和收件人和主题：
'''


def sendemail2():
	'''发送邮件函数'''

	'''第一步，创建数据'''
	smtpserver = 'smtp.exmail.qq.com'  # 定义变量，邮件服务器
	sender = '15902127953@163.com'  # 定义变量，发送人
	password = 'test123456'  # 发送人的密码
	receiver = 'xxxxxxx@163.com'  # 定义变量， 接收人

	'''第二步，构建邮件内容，通过email中的类MIMEText
		Header类只需要理解用来转换编码的'''
	content = MIMEText('第二次通过python发送邮件', 'plain', 'utf-8')
	content['From']=Header(sender,'utf-8')
	content['To']=receiver
	content['Subject']=Header('主题是自动化测试','utf-8')


	'''邮件发送过程，通过smtplib模块中的SMTP类'''
	server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

	server.set_debuglevel(1)  # 打印log

	server.login(sender, password, )  # 先登录邮件服务器。参数1：发送人；参数2：密码

	server.sendmail(sender, receiver, content.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

	server.quit()  # 退出邮件服务器


#sendemail2()






'''例三：邮件内容包含html
只需要将上面的列子改一个参数；plain改成html，然后邮件内容中写入html就可
比如：<html><header><title>第一个html</title></header><body><h1>nihao</h1><a href="https://www.baidu.com/">百度首页</a></body></html>
上面一行就是一个简单的html页面，可以将它写入邮件中'''


def sendemail3():
	'''发送邮件函数'''

	'''第一步，创建数据'''
	smtpserver = 'smtp.exmail.qq.com'  # 定义变量，邮件服务器
	sender = '15902127953@163.com'  # 定义变量，发送人
	password = 'test123456'  # 发送人的密码
	receiver = 'xxxxxxx@163.com'  # 定义变量， 接收人

	'''第二步，构建邮件内容，通过email中的类MIMEText
		Header类只需要理解用来转换编码的'''
	content = MIMEText('这里不是html<html><header><title>第一个html</title></header><body><h1>nihao</h1><a href="https://www.baidu.com/">百度首页</a></body></html>', 'html', 'utf-8')
	content['From'] = Header(sender, 'utf-8')
	content['To'] = receiver
	content['Subject'] = Header('主题是自动化测试', 'utf-8')

	'''邮件发送过程，通过smtplib模块中的SMTP类'''
	server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

	server.set_debuglevel(1)  # 打印log

	server.login(sender, password, )  # 先登录邮件服务器。参数1：发送人；参数2：密码

	server.sendmail(sender, receiver, content.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

	server.quit()  # 退出邮件服务器


#sendemail3()





'''例四：邮件内容包含附件，这里讲一种，附件为html测试报告；需要导入email模块中的MIMEMultipart()类
带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
	1.可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
	2.再继续往里面加上表示附件的
'''


def sendemail4():
	'''发送邮件函数'''

	'''第一步，创建数据'''
	smtpserver = 'smtp.exmail.qq.com'  # 定义变量，邮件服务器
	sender = '15902127953@163.com'  # 定义变量，发送人
	password = 'test123456'  # 发送人的密码
	receiver = 'xxxxxxx@163.com'  # 定义变量， 接收人

	'''第二步，实例化MIMEMultipart对象，在通过attach方法增加邮件正文和附件
		Header类只需要理解用来转换编码的'''
	data=MIMEMultipart()
	data.attach(MIMEText('hello','plain','utf-8'))    #增加邮件正文
	data['from']=Header(sender,'utf-8')
	data['to']=receiver
	data['subject']=Header('包含附件','utf-8')

	'''增加附件，'''
	#通过open方法打开一个文件，并且read（），
	att = MIMEText(open(r'/Users/hejianhao/Desktop/testreport.html',encoding='utf-8').read())

	# 这句话说明该文件以附件形式展示，上课以详细展示了效果
	att["Content-Disposition"] = 'attachment; filename="report.html"'
	data.attach(att)

	'''邮件发送过程'''
	server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

	server.set_debuglevel(1)  # 打印log

	server.login(sender, password, )  # 先登录邮件服务器。参数1：发送人；参数2：密码

	server.sendmail(sender, receiver, data.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

	server.quit()  # 退出邮件服务器


#sendemail4()









'''练习一：郑州大学官网http://www.zzu.edu.cn/  虽然上课讲过，再做一遍练习；
这个练习有点意义，大家认真去写一遍完整的用例，包括如何判断用例结果，生成报告，
	写俩个case，只打开和关闭一次浏览器
	case1：打卡官网→点击"院系专业"→再点击"临床医学系"
	case1：再点击"院系专业"下的更多按钮

'''

'''练习二，写一个简单的python算法，练习python基础中的if-else，

我们知道"//"表示除法然后取整，例如16//3=5.333333333;然后取整数等于5                   
		但是如果x//y包含了一正一负，它的算法并不是这样，计算公式前面的笔记写了，自己去看


同理：我们知道"%"取模表示除法后去余数，例如16%3， 取余数结果等于1
	    但是如果x%y中包含了一正一负，它的算法并不是这样，计算公式前面的笔记写了，自己去看



x//y和x%y,假设我们只知道当xy都为正数的计算方法，
现在写一个函数实现效果，不管xy是正数还是负数都正确的打印出结果：


def test(除数,被除数,运算符号):
	函数体
	//  abs if—else renturn
	

调用该函数，传入三个参数，
test(18,4,%)   打印出即如果2
test(-18,4,%)  打印出即如果2
test(18,-4,%)  打印出即如果-2
test(18,4,//)  打印出即如果4
test(-18,4,%)  打印出即如果-5
test(18,-4,%)  打印出即如果-5
test(18,-4,+)  打印出:您的运算符号输入错误，请重新输入


'''





