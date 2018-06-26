from selenium import webdriver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import time,datetime,unittest


'''
课前复习：
常用selenium方法和javascript方法
获取元素属性的值：get_attribute('src')
元素是否在当前页面出现：webelement.is_display()
获取元素的文本：webelement.text

javascript可以获取浏览器对象：window(浏览器窗口)、location（浏览器url）、document（DOM元素根节点）
window.scrollTo(0,10000)
window.open(url)


location.reload()
location.assgin()
location.href()

document.getElementsById().click()
document.getElementsByclassname().value=
document.getElementsByTagname()[0].click
document.getElementsByclassname().style.visibility='visible'



'''javascript 获取元素的值，需要用return，和写一个def函数一样的道理，如果函数中没有return，获得的值为NONE'''

driver=webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
js='return document.getElementById("vip").style.visibility'
value=driver.execute_script(js)
print(value)


'''js非常强大，可以实现各种酷炫的效果；大家可以去学习一些基本的JS和html，对自动化测试非常有帮助
	例如：用红色框框，高亮某个元素，
	js语句用分号分开；
	arguments[i]和元素一一对应'''
hidden=driver.find_element_by_xpath("/html/body/input[1]")    #元素一
visible=driver.find_element_by_xpath("/html/body/input[2]")   #元素二
driver.execute_script('arguments[0].style.border="6px solid red";arguments[1].style.border="6px solid red"', visible,hidden)



python发送邮件：导入：email  smtplib
三个步骤：
1、设置基本数据信息
2、email中的MIMEText类构建邮件的内容
3、smtplib.SMTP类 发送邮件
'''


def send_report():
	'''第一步：账号数据信息'''
	sender='15902127953@163.com'
	password='test123456'
	recevier='15902127953@163.com'
	smtpserver='smtp.163.com'


	'''第二部：构建邮件内容'''
	email=MIMEText('<html>这就是html</html>','html','utf-8')
	email['from']=Header(sender,'utf-8')
	email['to']=recevier
	email['subject']=Header('这是主题','utf-8')


	'''第三步：发送邮件'''
	send=smtplib.SMTP(smtpserver,25)
	send.login(sender,password)
	send.set_debuglevel(2)
	send.sendmail(sender,recevier,email.as_string())
	send.quit()


'''
练习：
//: x//y=坐标上x到y的距离//y，    结果符号为负
% : x%y=|x|-(|y|*|x//y|)       结果符号与y相同

'''

class Homework(unittest.TestCase):

	'''继承unittest类，可以进行单元测试，测试某个方法的功能'''
	def homework(self,x,y,symbol):
		'''被测试的函数'''
		if symbol == '//':
			if x * y > 0:
				return x // y
			else:
				return -(abs(x - y) // abs(y))

		elif symbol == '%':
			if x * y > 0:
				return x % y
			else:
				result = abs(x) -(abs(y) * abs(abs(x - y) // abs(y)))
				if result * y > 0:
					return result
				else:
					result (-result)
		else:
			return '您输入的预算符号错误'

	@classmethod
	def setUpClass(self):
		print('开始单元测试')

	@classmethod
	def tearDownClass(self):
		print('单元测试结束')

	def testcase1(self):
		'''用例1：检验上面homework函数的功能，//'''
		result=self.homework(18,-4,'//')
		self.assertEqual(result,18//-4)

	def testcase2(self):
		'''用例2：检验上面homework函数的功能，%'''
		result=self.homework(18,-4,'%')
		self.assertEqual(result,18%-4)


if __name__=='__main__':
	unittest.main()









'''
robotframework:
rf运行环境安装和基本概念：看ppt和我发的PDF文档

1.练习1打开测试网站，验证用户名，验证表格行数


#setting，主要用来导入库，和一些用户自定义的源文件，或者自己写的py文件；
关键字：Library、Resource

*** Settings ***                   
Library           Selenium2Library                                          #导入库
Suite Testsetup   open browser    http://www.zzu.edu.cn/    chrome          #所有用例执行前的动作
Suite Teardown    close browser                                             #所有用例执行后的动作
Test Setup                                                                  #每个用例执行前的动作
Test Teardown                                                               #每个用例执行后的动作  


*** Test Cases ***     #下面全是测试用例

case01     
   [Documentation]  这里是注释文档，用例1；验证登录后，某个元素存在，且welcome+用户名元素存在
   Wait until element is visible    xpath=/html/body/a         10                登录元素还未加载出来
   click element                    xpath=/html/body/a
   input text                       xpath=/html/body/form/p[1]/input             ${username}
   input text                       xpath=/html/body/form/p[2]/input             ${password}
   click element                    xpath=/html/body/form/p[3]/button
   #element should be visible       xpath=/html/body/p     用户名不存在            
   element text should be           xpath=/html/body/p     welcome${username}    登录者身份不对





*** Variables ***           #用来设置一些全局变量，例如url，用户名，密码，网站的title等等

${username}   15902127953
${password}   123456


'''












'''练习2：下面是selenium和roborframework练习郑州大学的俩个简单的用例

'''


from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
class Testcase(unittest.TestCase):
	def setUp(self):
		'''每次用例(指以test开头的测试方法)运行前的初始化工作：例如开打浏览器、'''
		print('this is setup')

	def tearDown(self):
		'''每个用例执行完后的工作：例如关闭浏览器、清理测试数据等等'''
		print('this is teardown')

	@classmethod
	def setUpClass(self):
		'''所有用例执行前操作，且只执行一次'''
		print('this is setupclass')
		self.driver=webdriver.Chrome()
		self.driver.get(' http://www.zzu.edu.cn/')

	@classmethod
	def tearDownClass(self):
		'''所有用例执行结束后的操作，且只执行一次'''
		self.driver.close()

	def testcase1(self):
		'''用例1：点击院系专业'''
		self.move_to_yuanxizhuanye()
		self.driver.find_element_by_xpath("//*[text()='临床医学系']").click()

	def testcase2(self):
		'''用例2：点击更多'''
		self.driver.switch_to.window(self.driver.window_handles[0])
		self.move_to_yuanxizhuanye()
		self.driver.find_element_by_xpath("//*[contains(text(),'医学类')]/..//*[text()='更多>>']").click()

	def move_to_yuanxizhuanye(self):
		self.driver.switch_to.frame('zzu_top_6')
		yuanxizhuanye=self.driver.find_element_by_xpath("//*[text()='院系专业']")
		ActionChains(self.driver).move_to_element(yuanxizhuanye).perform()


if __name__=='__main__':
		unittest.main()   #接入HTMLTestRunner测试报告自己去练习一遍





'''
*** Settings ***                   
Library           Selenium2Library                                          #导入库
Suite Testsetup   open browser    http://www.zzu.edu.cn/    chrome          #所有用例执行前的动作
Suite Teardown    close browser                                             #所有用例执行后的动作
Test Setup                                                                  #每个用例执行前的动作
Test Teardown                                                               #每个用例执行后的动作  



*** Test Cases ***     
case01
    [Documentation]  郑州大学用例1，打开临床医学系连接
    move_to_yuanxizhuanye    
    click element   xpath=//*[text()='临床医学系']


case02
    [Documentation]  用例2，点击临床医学系下面的更多
    switch to NewTab
    move_to_yuanxizhuanye
    click element   xpath=//*[contains(text(),'医学类')]/..//*[text()='更多>>']


*** Keywords ***
switch to NewTab
    [Documentation]  这里是注释，定义这个关键字，表示切换TAb,参数为 i,表示切换至第几个窗口，默认为0
    [Arguments]  ${i}=0
    ${window}       list windows                     #获取当前所有windows个数，返回的是一个数组
    ${newwindow}    evaluate       ${window}[${i}]   #通过evaluate方法，或者数组的第几个值
    select window   ${newwindow}                     #切换至指定的window
    
	select window  title=郑州大学官网                  #当然，只用这一行代码，也能实现上面的效果。  


move_to_yuanxizhuanye
	[Documentation]  切换frame和鼠标移动到院系专业，将类似这样的连贯和通用型的动作，绑定在一起。形成一个个用户自定义的关键字，让用例简单明了
    select frame     zzu_top_6                        #切换frame
    mouse over       xpath=//*[text()='院系专业']      #鼠标移动至院系专业


一个好的测试用例，一看就知道这个用例做了什么，而不是怎么去做
what to do   
how  to do
很重要的思想
'''


接下来会讲rf的if-else；for循环、自定义源文件；等robotframework你用多了之后，会感觉它非常方便，实用，强大








'''homework
用robotframework写一个简单的用例：快递100网站，
验证快递查询功能：
已知条件：一个正确的快递单号；且不知道它是某个快递公司
查询该快递，然后在我的查件记录页面验证结果
一：验证新增一条查件记录，
二：验证查件记录中的快递公司是否正确）

'''




