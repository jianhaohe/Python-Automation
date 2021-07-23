#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlwt,xlrd




'''
请假的同学请先下载文件夹“测试网站”，因为网站有更新
复习：
面象对象编程：类（class）
	a：将数据和逻辑封装起来，简化编程
		__init__方法：
		1.第一个参数永远是self，
		2.每创建一个实例化对象，会自动调用这个方法
		3.在方法内部，用self.name=name将数据绑定
	b：方便调用，不需要知道具体实现细节 
	c:代码重用，通过继承机制

上次的作业：写一个"测试登录"的类,实现效果,每创建一个实例化对象就等于执行了一个具体的登录测试用例，只是每个测试用例的测试数据用户名和密码不一样，'''

class LoginTest:

	'''登录类'''
	driver = webdriver.Chrome()     #类变量
	driver.get('http://127.0.0.1:5000/')  #打开浏览器
	driver.find_element_by_xpath("//*[text()='登录']").click()  #点击登录

	'''表示上面三行代码只会执行一次，下面的方法每次去调用一次就执行一次'''

	def __init__(self,username,password):
		self.username=username    #绑定用户名
		self.password=password    #绑定密码

	def login(self):
		name=LoginTest.driver.find_element_by_xpath("/html/body/form/p[1]/input")   #输入用户名
		name.send_keys(self.username)
		pwd=LoginTest.driver.find_element_by_xpath("/html/body/form/p[2]/input")    #输入密码
		pwd.send_keys(self.password)
		LoginTest.driver.find_element_by_xpath("/html/body/form/p[3]/button").click()  #点击signin
case1=LoginTest('15902127950','123456').login()  #实例化一个对象，等于执行了一个测试用例
time.sleep(3)
case2=LoginTest('15902127953','123').login()     #实例化第二个对象，等于执行了第二个测试用例，只是用户名不一样

#继承上面的类
time.sleep(3)

class Child(LoginTest):
	pass
case3=Child('123455','124343').login()             #调用父类的方法，等于执行了第三个测试用例



'''复习一下excel
xlwt:写入数据
xlrd:读取数据
# '''
excel=xlwt.Workbook()           #创建一个excel表
sheet=excel.add_sheet('test')   #创建一个sheet
sheet.write(0,0,'username')   #第一行第一个空格写入数据
sheet.write(0,1,'password')   #第一行第二个空格写入数据
excel.save('0526.xls')        #保存的数据是上面写入的数据，可以多次写入，最后保存


'''将list1作为第一列（用户名），list2作为第二列（密码），下面练习用到这个excel表中的数据
     只有最后一组数据是正确的用户名和密码：15902127953，123456
'''
excel=xlwt.Workbook()           #创建一个excel表
sheet=excel.add_sheet('test')   #创建一个sheet
list1=['15902127951','15902127952','15902127954','15902127955','15902127956','15902127953']
list2=['12345678','123456789','123456','1234567','1234567','123456',]
for i in range(len(list1)):
	sheet.write(i,0,list1[i])         #写入第一列：用户名
for i in range(len(list2)):
	sheet.write(i,1,list2[i])        #写入第二列：密码
excel.save('0526.xls')               #保存


'''xlrd：读取'''
excel=xlrd.open_workbook('0526.xls')  #读取某个excel
sheet=excel.sheet_by_index(0)         #获取该excel的第一个sheet
print (sheet.nrows)                   #获取excel的行数
print (sheet.ncols)                   #获取excel的列数

print(sheet.row_values(0,1,2))        #获取第一行的第二个空格的值
#

'''从上面写好的excel表'0526.xls'读取数据，
excel表的数据是：
15902127951  123456
15902127952  12345678
15902127954  123456
15902127955  123456
15902127956  123456
15902127953  123456

，'''


'''作业1：******'''

'''前面学的东西不能全忘了，做一个小小的作业，就几行代码
   写一个login函数，调用execute_case，实现效果：
调用execute_case函数时，会分别去读取上面的excel表格的6组用户名和密码，登录我的测试网址，127.0.0.1
要求：上面有多少组数据，就会打开多少次浏览器，用每一组的数据去登录	（组数不固定，比如现在是6组数据，也有可能是8组，10组）
'''

excel=xlrd.open_workbook('0526.xls')
sheet=excel.sheet_by_index(0)

def login(username,password):
	driver = webdriver.Chrome()
	driver.get('http://127.0.0.1:5000/')
	driver.find_element_by_xpath("//*[text()='登录']").click()
	name=driver.find_element_by_xpath("/html/body/form/p[1]/input")
	name.send_keys(username)
	pwd=driver.find_element_by_xpath("/html/body/form/p[2]/input")
	pwd.send_keys(password)
	driver.find_element_by_xpath("/html/body/form/p[3]/button").click()
	driver.close()

def execute_case():

	'''请在这里补充代码实现：调用这个函数时，会分别去读0526.xls中的数据，不管它里面有多少组数据，（有多少组就执行多生次）
	提示：1.用for 循环读取excel表的数据
	     2.调用上面的登录函数
	'''

execute_case()

'''自动化测试：
selenium
1.它可以让浏览器自动执行各种web应用，主要用于执行web自动化测试
2.自动化管理基于web的各种无聊费时的任务
3.无数测试工具，api和核心框架的技术支撑
4.还可以用来爬虫
'''



'''
1.模拟手机浏览器：
    打开google浏览器，打开开发者工具，点击左上角的第二个按钮，可以将浏览器设置成手机模式
    当然自动化一样的可以浏览器设置成为手机模式
'''

mobile_emulation = {"deviceName": "iPhone X"}    #定义一个词典，说明设备名称，为iPhone X
chrome_options =webdriver.ChromeOptions()        #实例化ChromeOptions类的一个对象chrome_options
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  #调用里面的add_experimental_option方法，将设备信息参数传进去


driver = webdriver.Chrome(chrome_options=chrome_options)   #再将上面的chrome_options作为参数，传递给Chrome类
driver.get("http://www.baidu.com")                         #这时候就会以iPhone X的模式打开手机





'''
2.基本操作：
  刷新页面：  driver.refresh
  获取浏览器窗口大小:driver.get_window_size()
  设置浏览器窗口大小:driver.set_window_size()
  浏览器最大化窗口:driver.maximize_window()
  浏览器全屏：driver.fullscreen_window()
  获取浏览器窗口个数：driver.get_window_handle,返回的是一个列表
  切换到指定窗口: driver.switch_to.window()
  前进：driver.forward()
  后退：driver.back()
  关闭：driver.close() 关闭当前窗口
  退出：driver.quit()  完全退出浏览器
'''

driver=webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
time.sleep(2)
driver.refresh()        #刷新

size=driver.get_window_size()
print(size)             #打印当前窗口大小

driver.set_window_size(800,900) #设置窗口大小
time.sleep(3)
driver.maximize_window()  #最大化




再新开一个浏览器窗口
js='window.open("https://www.google.com/")'
driver.execute_script(js)
#
hand=driver.window_handles
print(hand)                #获取当前浏览器窗口个数，打印出来的是一个list，里面有2个元素。说明2个窗口

driver.switch_to.window(hand[1])  #切换到第二个窗口
driver.switch_to.window(hand[1])  #再切回到第一个窗口




#先点击测试网站的登录，再后退，再前进
driver.back()
time.sleep(2)
driver.forward()


time.sleep(5)
driver.close()  #关闭，
driver.quit()   #退出，退出所有浏览器


'''键盘操作：Tab,Enter
1.先导入selenium中的class:Key
from selenium.webdriver.common.keys import Keys

1.还是先定位到元素，2.再在该元素上操作，键盘上的按键，例如：
Tab:driver.find_element_by_xpath("").send_keys(Keys.TAB)

Enter:driver.find_element_by_xpath("").send_keys(Keys.ENTER)
'''

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
driver.find_element_by_xpath("//*[text()='登录']").click()        #点击登录
driver.find_element_by_xpath("/html/body/form/p[1]/input").send_keys("15902127953")  #输入用户名
time.sleep(2)

driver.find_element_by_xpath("/html/body/form/p[1]/input").send_keys(Keys.TAB)       #在用户名输入框按一下Tab键
driver.find_element_by_xpath("/html/body/form/p[2]/input").send_keys("12345678")     #输入密码
time.sleep(2)
driver.find_element_by_xpath("/html/body/form/p[2]/input").send_keys(Keys.ENTER)     #按Enter,相当于点击登录













'''鼠标操作：先导入selenium中的class:ActionChains
from  selenium.webdriver.common.action_chains import ActionChains
ActionChains原理：
1.调用该类里面的方法是，不会立即执行，将需要执行的动作按顺序存放在一个列队里，
2.调用 perform()方法时，依次执行列队里的动作

'''

'''双击：double_click：
以下是双击测试网址中，用户名输入框的实例：
'''
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
driver.find_element_by_xpath("//*[text()='登录']").click()            #点击登录
driver.find_element_by_xpath("/html/body/form/p[1]/input").send_keys("15902127953")  #输入用户名


#1.还是先定位元素，
#2.先double_click，再调用perform方法
# username=driver.find_element_by_xpath("/html/body/form/p[1]/input")    #需要双击的元素
# ActionChains(driver).double_click(username).perform()



'''鼠标移动至某个元素：move_to_element
测试网址有个元素，移动上去，颜色变红的实例：
1.同样的先定位到，需要将鼠标移动到哪里去的元素
2.再用move_to_element+perform方法
'''

# tag=driver.find_element_by_xpath("/html/body/div/a")        #需要移动的目标元素
# time.sleep(2)
# ActionChains(driver).move_to_element(tag).double_click(username).perform()



'''鼠标左键不松开：click_and_hold
   松开鼠标左键：release
   测试网址有个元素点击鼠标左键不松开，颜色变浅的实例：
   1.定位到元素
   2.click_and_hold+perform方法
   3.release，再松开鼠标左键，颜色又变深
'''
# driver.find_element_by_xpath("/html/body/div/div[1]/a").click()      #进入到拖拽练习的页面
# temp=driver.find_element_by_xpath('//*[@id="dragger"]')              #定位元素
# time.sleep(2)
# ActionChains(driver).click_and_hold(temp).perform()                  #按住鼠标左键不松开
# time.sleep(2)
# ActionChains(driver).release(temp).perform()                         #然后松开鼠标左键



'''拖拽元素：drag_and_drop
   测试网址上拖拽一个元素到另外一个框里面的实例：
   1.定位到被拖的元素
   2.定位到需要拖到的目的地的元素
   3.drag_and_drop+perform方法
'''
# driver.find_element_by_xpath("/html/body/div/div[1]/a").click()      #进入到拖拽练习的页面
# temp=driver.find_element_by_xpath('//*[@id="dragger"]')              #定位被拖的元素
# item1=driver.find_element_by_xpath("/html/body/div[2]")                #定位到拖拽到哪里的元素
# time.sleep(2)
# ActionChains(driver).drag_and_drop(temp,item1).perform()




'''练习：drag_and_drop方法的功能是将一个元素拖拽另外一个元素上面，
		其实用我们上面学到的click_and_hold+move_to_element+release（依次执行按住鼠标不松开+移动元素+松开）
		可以实现一模一样的效果
刚好理解一下ActionChains的原理（将需要执行的动作按顺序存放在一个列队里，调用 perform()方法时，依次执行列队里的动作）'''


#实现drag_and_drop的拖拽效果
# driver.find_element_by_xpath("/html/body/div/div[1]/a").click()      #进入到拖拽练习的页面
# temp=driver.find_element_by_xpath('//*[@id="dragger"]')              #定位被拖的元素
# item1=driver.find_element_by_xpath("/html/body/div[2]")               #定位到拖拽到哪里的元素
#ActionChains(driver).click_and_hold(temp).move_to_element(item1).release(temp).perform()





'''元素定位：
对于对于 Web 自动化测试来说，就是操作页面上的各种元素，在操作元素之间需要先找到元素，换句话说就是定位元素
selenium常见定位元素8中方法：
Id
Name
Classname
Tagname
linkText
partialLinkText
cssSelector
Xpath
前面7种方法一起过一遍，自己敲一遍看效果，重点是xpath定位元素
'''





'''通过id定位，测试网址首页"点击此处"按钮的id为 testid


""'''
# driver=webdriver.Chrome()
# driver.get('http://127.0.0.1:5000')
# time.sleep(2)
# driver.find_element_by_id('testid').click()


'''classname
测试网址首页"点击此处"按钮的classname为 testclassname'''

#driver.find_element_by_class_name('testclassname').click()




'''name,测试网址"用户名输入框"的name为 username'''
#driver.find_element_by_name('username').send_keys('15902127953')



'''tagname,通过标签名称定位
  测试网址的用户名输入框的标签为input
'''

#driver.find_element_by_tag_name('input').send_keys('1763798976')


'''但是用户名和密码输入框的标签都是input，
我们就需要用到find_elements，而不是find_element方法
1.它先返回一个list，表示这个页面有多少个input标签
2.你再根据list的索引去操作这个元素

注意：其它的元素定位方法也是同样的道理，如果定位到多个，用find_elements

'''
#input=driver.find_elements_by_tag_name('input')     #返回一个list，因为用户名和密码都是input标签
#input[1].send_keys('1763')                          #list[1] 表示在第二个标签输入


'''linktext 超连接中的文本信息来定位元素
   测试网址登陆页面 有几个超链接，文本信息是"练习一下鼠标移动" 和"练习鼠标拖拽"
'''
#time.sleep(2)
#driver.find_element_by_link_text('练习一下鼠标移动').click()

'''partialLinkText：是上面linktext方法的扩展。就是跟据文本的部分信息定位元素，
例如：文本信息是"练习鼠标拖拽"，可以通过"拖拽"定位这个元素
'''
#driver.find_element_by_partial_link_text('鼠标拖拽').click()

'''cssselector，层叠样式表定位元素，此方法大家还是先copy开发者工具中的selector，有兴趣的可以自己写css

'''
#driver.find_element_by_css_selector("body > div > div:nth-child(7) > a").click()





'''xpath
以上7种方法学会了就行，我强烈不推荐，前提是你学会了下面的xpath方法，
xpath:path就是路径，类似文件夹Desktop/classnotes/

绝对路径定位：copy xpath  (借助谷歌浏览器)
缺点：当页面元素父级元素发生改变，页面元素的位置发生改变时，都需要修改

相对路径定位：以//开头+标签名  （自己写xpath）
优点：长度和标签开始的位置并不受限制，稳定且万能


至于为什么要学xpath，我上课现场改了我测试网址的前端代码，copy的xpath就报错，举了实例。

'''



'''看看一些符号的定义
//  :表示相对路径    （所以xpath的写法是：以//开头+标签名 ）
/.. :表示找上级       
/   :表示找下级
@:标签属性定位        
() :text的值          
*  ：标签名任意

'''

'''比如测试网址首页的"点击此处"的按钮的id为：testid
   写相对路径xpath：//button[@id='testid']
    或者标签名任意：//*[@id='testid']
'''
#driver.find_element_by_xpath("//button[@id='testid']").click()


'''比如测试网址首页的"点击此处"的按钮的text文本为：点击此处
   写相对路径xpath：//button[text()='点击此处']
    或者标签名任意：//*[text()='点击此处']
'''


#driver.find_element_by_xpath("//button[text()='点击此处']").click()


'''模糊查询：starts-with

'''
#//+标签名[starts-with(@什么属性，'以什么开始')]
#//div[starts-with(@style,'border')]


'''模糊查询：  contains():
   表示该元素的属性的值，包含了什么东西

'''

#//+标签名[contains(@什么属性，'包含了什么值')]
#//div[contains(@class,'success')]






'''文件上传，input的文件上传，例如测试网址登陆进去后的页面
	用send_keys方法+文件路径名称
'''
driver.find_element_by_xpath("//*[text()='文件上传']/..//input").send_keys('/Users/hejianhao/Downloads/test.png')











# #上传文件
# #time.sleep(2)
# #driver.find_element_by_xpath('//*[@id="testtableafter"]/tbody/tr[1]/td[2]/input').send_keys('/Users/hejianhao/Downloads/test.png')




'''作业2： 测试网站登陆进去定位元素练习页面，有一行叫做Checkbox，右边有四个checkbox（网络、培训、朋友介绍、其它方式）
   根据左边的Checkbox的xpath，写出"朋友介绍"的xpath，

#左边的Checkbox的xpath我已经写好了：
//*[text()='CheckBox']，根据这个xpath去定位到右边的第三个checkbox（就是"朋友介绍"）
但是xpath中不能包含"朋友介绍"这几个字，（假设这几个字不固定的），
题目还不懂的看群里截图
'''
#右边第三个checkbox的xptah如下：
#/*[text()='CheckBox']？？？？？？？？？?
