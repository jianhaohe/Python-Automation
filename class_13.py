'''
appium
     环境搭建：
     启动appium：
     获取被测app的包名和activity名称：
     找元素方法：uiautomatorview，id，class,xpath(/../android.widget.butoon)
     获取设备信息，location，滑动，swipe(x,y.x,x,y,500)
     获取属性，text,class



     send_keys:
     unittest
     webview,


     uiautomator



并发执行测试用例：pabot
		Pabot将从套件文件中拆分测试执行，而不是从单个测试级别
		-- processes  n 表示线程数

	已经安装好docker的同学，
1.先下载docker_compose文件，
2.cd 至该文件路径下面，
只需执行一行命令:docker-compose -f docker_compose.yml up -d
		然后在代码里面以一个参数：emote_url=http://0.0.0.0:4444/wd/hub

'''




'''

webapp
查看元素：chrome://inspect/#devices
	    第一步：获取当前的页面：driver.contexts
	          切换至webview：dirver.switch_to.content
	          然后打开谷歌去定位元素，类似web端定位元素
	    




from appium import webdriver
import unittest,time


# des_weixin={
# 	'platformName':'Android',
# 	'deviceName':'8BN0218309004925',
# 	'appPackage':'com.tencent.mm',
# 	'appActivity':'.ui.LauncherUI',
# 	'noReset':'true',
# 	'unicodeKeyboard':'True',
# 	'resetKeyboard':'True'
# }


# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=des_weixin)
# driver.wait_activity('.ui.LauncherUI',5)

'''
#登录过程
# time.sleep(2)
# driver.find_element_by_xpath('//android.widget.Button[@text="登录"]').click()
# driver.find_element_by_id("com.tencent.mm:id/hx").send_keys('17621947612')
# driver.find_element_by_id("com.tencent.mm:id/ak_").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@text='请填写微信密码']").send_keys('test123456')
# driver.find_element_by_id("com.tencent.mm:id/ak_").click()
'''
#点击我的
#driver.find_element_by_xpath('//android.widget.TextView[@text="我"]').click()



#driver.quit()


class Test_weixin(unittest.TestCase):
	des_weixin = {
		'platformName': 'Android',
		'deviceName': '8BN0218309004925',
		'appPackage': 'com.tencent.mm',
		'appActivity': '.ui.LauncherUI',
		'noReset': 'true',
		'unicodeKeyboard': 'True',
		'resetKeyboard': 'True'
	}

	des_yudada = {
		'platformName': 'Android',
		'deviceName': '8BN0218309004925',
		'appPackage': 'com.yudada.main',
		'appActivity': '.page.web.main.WebMainActivity',
		'noReset': 'true',
		'unicodeKeyboard': 'True',
		'resetKeyboard': 'True'
	}

	@classmethod
	def setUpClass(self):
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=self.des_yudada)
		self.driver.wait_activity('.page.web.main.WebMainActivity', 5)
		print('所有用例执行前的动作')
	# @classmethod
	# def tearDownClass(self):
	# 	self.driver.quit()
	# 	print("所有用例执行后的动作")
	# def setUp(self):
	# 	self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=self.des_weixin)
	# 	self.driver.wait_activity('.ui.LauncherUI', 5)
	# 	print('每个用例执行前的动作')
	#
	#
	# def tearDown(self):
	# 	self.driver.quit()
	# 	print("每个用例执行后的动作")


	# def testcase01(self):
	# 	driver=self.driver
	# 	driver.find_element_by_xpath('//android.widget.TextView[@text="我"]').click() #点击我的
	# 	time.sleep(2)
	# 	weixinhao = driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"微信号：")]')
	# 	text = weixinhao.text
	# 	print(text)
	# 	weixin = text.split('：')[1]
	# 	print(weixin)
	# 	self.assertEqual(weixin,'hejianhao06')
	# 	print('用例1')
	# def testcase02(self):
	# 	print('开始运行用例2')
	#
	# 	driver=self.driver
	# 	driver.find_element_by_xpath('//android.view.View[@text="剑豪"]/../../..').click() #选择聊天对象
	# 	driver.find_element_by_id('com.tencent.mm:id/aaa').send_keys('你好')  #输入聊天内容
	# 	driver.find_element_by_id('com.tencent.mm:id/aag').click()         #点击发送
	# 	#self.assertEqual()


# 	def testcase01(self):
# 		driver=self.driver
# 		temp=driver.contexts
# 		driver.switch_to.context(temp[1])
# 		time.sleep(3)
# 		driver.find_element_by_xpath("//*[text()='出售大厅']/..").click()
#
#
# if __name__=='__main__':
# 	unittest.main()




#s='微信号: 123456'
# weixin=s.split(' ')[1]
# print(weixin)


'''
# uiautomator2
#  前提：安卓开发环境，adb保证连接成功
#  1.pip install --pre uiautomator2  安装python的库
#
#  2.python -m uiautomator2 init
#
#  3.pip install --pre -U weditor

#如果是源码安装：
'''
	git clone 'lujing/uiautomator2'
	cd  uiautomator2 看里面是否有个 setup.py文件
	cd 进去之后，python setup.py install
	  如果提示什么模块找不到，单独pip install 该模块
'''
 


 
'''
import  uiautomator2 as ui2
import  uiautomator2.ext.htmlreport  as htmlreport

# info=driver.device_info
# print(info)
# driver(resourceId="com.tencent.mm:id/c9f", text=u"我").click()
# time.sleep(3)
# driver.screen_off()
#
# time.sleep(3)
# driver.screen_on()
# time.sleep(3)
# driver.unlock()





d = ui2.connect('8BN0218309004925')  #connect 连接设备
d.app_stop_all()
report=htmlreport.HTMLReport(d)
report.patch_click()  #表示每次的点击都会自动截图
d.app_start('com.tencent.mm')        #启动app

x=d.window_size()[0]
y=d.window_size()[1]

#print(x*0.284,y)

d.click(x*0.405, y*0.259)
d.swipe(x,y,x,y,x,y,x,y,5)

# d(text="剑豪").click() #点击聊天对象
# #d(resourceId="com.tencent.mm:id/aaa").send_keys('你好') #输入聊天内容
# d(resourceId="com.tencent.mm:id/jz", className="android.view.View", instance=3).long_click() #第四局聊天信息




