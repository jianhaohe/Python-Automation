#coding=utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.common.action_chains import ActionChains
#import xlwt,xlrd
#from  fanmaotesting.HTMLTestRunner_PY3 import HTMLTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


'''
课前复习：
selenium基本操作：刷新，前进、后退、获取多少个浏览器窗口、切换窗口、关闭、退出、设置窗口大小值
键盘操作：导入Keys ： TAB ENTER
鼠标操作：导入：Actionchains:  
		双击：double_click
		按住鼠标左键不松开：click_and_hold
		松开：release
		拖拽：drag_and_drop
		移动至某个元素：move_to_elements
定位元素：id 、name、 classname、linktext、patialinktext、css、tag_name xpath
xpath ：稳定 灵活 万能，且xpath里面支持变量
		//+标签
		//:相对路径
		@:[@属性名='值']
		text:[text()='值']
		/..:上家
		/:下级
		*:
		模糊查询：
		contains:[contains(@属性名称,'值包含了什么')]
		starts-with:[starts-with(text(),'已什么开始')]
		
'''






'''特殊的元素定位：svg,frame'''




'''SVG 指可伸缩矢量图形 (Scalable Vector Graphics)
	
	需要xpath里面的name()方法:*[name()='svg']'''


'''frame：
frame标签有frameset、frame、iframe三种,
frameset跟其他普通标签没有区别，不会影响到正常的定位，
而frame与iframe需要切换进去才能定位到其中的元素
看例子：'''


driver=webdriver.Chrome()
driver.get("http://www.kuaidi100.com/")
driver.find_element_by_xpath('//*[@id="uDeskTarget"]').click()                       #点击客服聊天按钮


#切换至frame
driver.switch_to_frame(driver.find_element_by_xpath('udesk_iframe'))                #用frame的id来切换
#driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="udesk_iframe"]'))    #如果frame没有id和name，用它的xpath来切换

driver.find_element_by_xpath('//*[@id="txtMsg"]').send_keys('123')
#driver.execute_script("document.getElementById('txtMsg').value='456'")              #输入文字也可以用js来执行


#跳出frame回到住界面，再点击其它的元素
driver.switch_to_default_content()


'''
unittest：是Python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架。
'''
'''官方简单的列子，是俩个简单的单元测试，测试add、multiply这俩个方法，assertequal用来判断测试结果'''

# class IntegerArithmeticTestCase(unittest.TestCase):
# 	def testAdd(self):                          # test method names begin 'test*'
# 		print('用例名称')
# 		self.assertEqual((1 + 2), 3)
# 		self.assertEqual(0 + 1, 1)
#
# 	def testMultiply(self):
# 		self.assertEqual((0 * 10), 0)
# 		self.assertEqual((5 * 8), 40)
#
#
# if __name__=='__main__':
# 	unittest.main()









'''	
为什么要学unittest:
			1.方便用例运行，可以灵活的组织用例，
			2.如果有fail的用例不影响后面的用例运行
			
			
			
unittest可以用来：
		1.灵活的组织测试用例
		2.让用例高效的执行
		3.方便验证测试用例的结果
		4.集成html形式测试报告
'''


'''看列子：以下是俩个测试类，一个不继承unittest，一个继承了unittest.testcase'''

class Testcase1():
	'''未继承unittes'''
	def testcase1(self):
		print('用例1，点击左边的按钮，弹出alert，点击接受')

		driver=webdriver.Chrome()
		driver.get('http://127.0.0.1:5000/')
		driver.find_element_by_xpath('//*[@id="testid"]').click()
		text=driver.switch_to_alert().text
		print(text)
		driver.switch_to.alert.accept()

	def testcase2(self):
		print('用例2，点击登录网站进入练习页面')
		username='15902127953'
		driver=webdriver.Chrome()
		driver.get('http://127.0.0.1:5000/')
		driver.find_element_by_xpath('/html/body/a').click()
		driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
		driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
		driver.find_element_by_xpath('/html/body/form/p[3]/button').click()
		print('case2')

Testcase1().testcase1()
Testcase1().testcase2()

'''没有继承unittest，
 1.运行用例时，类里面有多少个测试用例，就需要调用多少次
 2.其中有一个用例失败了，导致程序停止运行，所有后面的用例也停止运行'''




class Testcase2(unittest.TestCase):
	'''继承unittes'''
	def testcase1(self):
		print('用例1，点击左边的按钮，弹出alert，点击接受')

		driver=webdriver.Chrome()
		driver.get('http://127.0.0.1:5000/')
		driver.find_element_by_xpath('//*[@id="testid"]').click()
		text=driver.switch_to_alert().text
		print(text)
		driver.switch_to.alert.accept()

	def testcase2(self):
		print('用例2，点击登录网站进入练习页面')
		username='15902127953'
		driver=webdriver.Chrome()
		driver.get('http://127.0.0.1:5000/')
		driver.find_element_by_xpath('/html/body/a').click()
		driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
		driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
		driver.find_element_by_xpath('/html/body/form/p[3]/button').click()
		print('case2')


if __name__=='__main__':
	unittest.main()


'''继承unittest类
 1.运行用例时，不管有多少个用例，直接用unittest.main()运行,
            unittest.main():可以方便的将一个测试模块，变为可直接运行的测试脚本
 2.其中有一个用例失败了，不影响其它用例正常运行'''
















'''


unittest特点或者定义：


1.一个class继承unittest.TestCase，即是一个个具体的TestCase（测试方法均以 test 开头，否则是不被unittest识别）

2.每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E

3.verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。

4.用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境

5.参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。

6.多个单个的测试用例集合在一起，就是TestSuite

'''

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
		self.driver.get('http://127.0.0.1:5000/')

	@classmethod
	def tearDownClass(self):
		'''所有用例执行结束后的操作，且只执行一次'''
		self.driver.close()

	def testcase1(self):
		'''用例1：点击网址首页的按钮，弹窗alert，并验证alter的值'''
		self.driver.find_element_by_xpath('//*[@id="testid"]').click()
		text=self.driver.switch_to_alert().text              #获取alert的值
		self.driver.switch_to.alert.accept()                #切换至alert
		self.assertEqual(text,'别点点登录啊')                 #判断测试结果，


	def testcase2(self):
		'''用例2：登录，验证登录后用户名是否出现'''
		username='15902127953'
		self.driver.find_element_by_xpath('/html/body/a').click()
		self.driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
		self.driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
		self.driver.find_element_by_xpath('/html/body/form/p[3]/button').click()
		'''第一种判断方法，用户名那个元素是否出现
				 #is_displayed()判断页面上是否出现某个元素，如果出现了，返回true
				 assertTrue判断是否为真'''
		#self.assertTrue(self.driver.find_element_by_xpath('/html/body/pa').is_displayed())

		'''第二种，判断用户名里面的值，是否是你输入的电话号码'''
		self.assertTrue(self.driver.find_element_by_xpath("//*[text()='welcome%s']"%username).is_displayed())

if __name__=='__main__':
	unittest.main()





'''以上讲的都是在一个文件，如果有多个测试文件，
   我们新建一个runtestcase文件，来运行所有的测试文件
'''



'''
unittest的流程：
a.写好TestCase， 创建TestSuite实例，                                  
b.可以通过addTest或addTests向TestSuite中添加case     #通过实例中的addtest方法添加测试用例 至testsuite
    或者用TestLoader加载TestCase到TestSuite，
    可以用TestLoader的loadTestsFrom__()方法。
	
c.通过TextTestRunner类里面的run()方法来来运行TestSuite
  

'''

testcase=unittest.TestSuite()        #第一步，创建一个TestSuite实例

#第二步，增加测试用例

'''第一种方法：直接用addtest+方法添加单个。
			传入参数：类名称('用例名称')
			'''
#testcases.addTest(LoginTest001('testcase2'))


'''第二种方法：直接用addtests方法添加多个测试用例，而且根据添加是顺序来执行'''

# testcases.addTests([LoginTest001('testcase2'),LoginTest001('testcase1')])



'''第三种方法：addtests+TestLoad添加测试类，而不是单个的测试用例
		loadTestsFromTestCase：参数（直接传入类名）
		loadTestsFromName:参数（传入文件模块名.类名）
		loadTestsFromNames:参数：（传入文件模块名.类名的列表）
		'''

#例如：
#testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest001))

#testcases.addTests(unittest.TestLoader().loadTestsFromName('login01.LoginTest001'))

#testcases.addTests(unittest.TestLoader().loadTestsFromNames(['login01.LoginTest01','login01.LoginTest001']))



#第三步：TextTestRunner来运行所有测试用例
unittest.TextTestRunner().run(testcase)



'''以上三步动作，用什么方法，一定要理解，传入参数的格式只能记住'''










'''集成测试报告，前面2步动作和上面的一样，只是第三步现在用HTMLTestRunner类来运行所有测试用例
	1.创建TestSuite实例，
	2.用addtest方法，再去组织TestSuite
	3.定义报告路径，实例化HtmlTestRunner,run,
	'''
testcase=unittest.TestSuite()                                                       #第一步
testcase.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest001))        #第二部

time=time.strftime('%Y-%m-%d-%H-%M',time.localtime())     #获取当前时间

dir='/Users/hejianhao/Desktop/'+time+'report.html'        #定义测试报告路径+当前时间

file=open(dir,'wb')

runner=HTMLTestRunner(stream=file,title='凡猫自动化测试报告',description='selenium')

runner.run(testcase)                                                                 #第三步









'''等待时间大家看看，有时间再讲'''
'''三种等待时间'''
'''等待方式：强制等待、显性等待、隐形等待
等待：下一步操作需要依赖上一步的内容或结果，如果，上一步操作或加载花费时间较长，立即点下一步操作，会产生元素找不到，或者元素的状态不对
强制等待sleep:强制等待几秒，执行下一步操作
优点：使用简单，可以在调试时使用。
缺点：不准确，浪费等待时间

隐式等待implicitly_wait(x):，在X时间内，页面加载完成，进行下一步操作
优点：设置一次即可
缺点：等待整个页面加载完成


显式等待WebDriverWait：程序每隔X秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException异常。
WebDriverWait(driver, 超时时间, 调用频率).until(要执行的方法, 超时时返回的错误信息)
'''



