'''class01:
         selenium环境安装：
         selenium基本操作
         元素定位方法'''
#环境安装：
'''1.进入cmd， pip install selenium
   2.将对应版本的chromedriver放置python的安装目录下，python目录可在cmd用命令 where python查看
'''

#打开本地测试网址127.0.0.1:5000
'''
1.解压压缩包至本地
2.用pycharm打开该文件。file-open-选择该文件目录，注意是选择整个目录webtest，而不是webautotest.py文件
3.运行webautotest.py，打开127.0.0.1:5000
'''

#第一个自动化脚本
from selenium import  webdriver
driver=webdriver.Chrome()                   #打开谷歌浏览器，如果是火狐打开Firefox。这是实例化一个浏览器对象，后面的操作都是用这个对象里面的方法，例如get
driver.get("http://127.0.0.1:5000/")        #用get方法输入网址

'''元素定位：1.F12打开浏览器开发者模式，2.切换至Elements，3.点击左上角定位元素按钮，就可定位页面上的元素。
对于对于 Web 自动化测试来说，就是操作页面上的各种元素，在操作元素之间需要先找到元素，换句话说就是定位元素
selenium常见定位元素8中方法：
Id、Name、Classname、Tagname、linkText、partialLinkText、cssSelector、Xpath
前面7种方法一起过一遍，自己敲一遍看效果，重点是xpath定位元素
'''


'''
find_element：找到页面上某一个元素
find_elements：找到页面上所有相同属性元素的list，
'''


'''定位元素方法 id'''
driver.find_element_by_id("testid").click()        #定位元素属性id为“testid”的元素
'''tagname:标签名称'''
tag_list=driver.find_elements_by_tag_name("a")
print("tag_list{0},类型是{1}".format(tag_list,type(tag_list)))
tag_list[0].click()
'''name'''
driver.find_element_by_name("username").send_keys("15902127953")
'''classname: class的名称'''
driver.find_element_by_class_name("testclassname").click()

'''partialLinktext：超链接文本包含xx值
   linktext：超链接文本值，例如测试网址登陆页面 有几个超链接，文本信息是"练习一下鼠标移动" 和"练习鼠标拖拽"'''
driver.find_element_by_link_text("登录").click()
driver.find_elements_by_partial_link_text("淘宝")[1].click()
driver.close()

'''xpath：为什么要学xpath 1.元素id或者name不唯一 2.id是动态  3.元素没有id或class  4.直接在浏览器可调试元素是否定位正确
看看一些符号的定义
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

'''比如测试网址首页的"点击此处"的按钮的text文本为：点击此处
   写相对路径xpath：//button[text()='点击此处']
    或者标签名任意：//*[text()='点击此处']
'''




'''selenium常用操作方法

   刷新：refresh,
  获取浏览器窗口大小:get_window_size 设置浏览器窗口大小:set_window_siez最大化:maximizewindow
  获取浏览器窗口个数、切换到指定窗口:switch_handle,switch_to.window()
  前进：forward
  后退：back
  关闭：close
  退出：quit
    
'''
import time
#刷新refresh
# time.sleep(2)
# driver.refresh()
#前进/后退
# driver.find_element_by_xpath("/html/body/a").click()
# time.sleep(1)
# driver.back()
# time.sleep(1)
# driver.forward()

#获取有多少个窗口.切换窗口
# driver.find_element_by_xpath("/html/body/div[2]/a").click()
# l=driver.window_handles
# # print(l)
# time.sleep(2)
# driver.switch_to.window(l[1])
# time.sleep(2)
# driver.switch_to.window(l[0])

#获取窗口大小，设置大小
# size=driver.get_window_size()
# print(size)
# driver.set_window_size(300,300)
# size1=driver.get_window_size()
# print(size1)

#关闭和退出
# driver.find_element_by_xpath("/html/body/div[2]/a").click()
# l=driver.window_handles
#
# time.sleep(2)
# driver.switch_to.window(l[1])
# driver.switch_to.window(l[0])
# # driver.quit()
# driver.close()

#放大缩小
# driver.minimize_window()
# time.sleep(2)
#driver.maximize_window()



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
