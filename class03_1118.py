from  selenium import webdriver
from  selenium.webdriver.support.wait import  WebDriverWait
import time
from  selenium.common.exceptions import NoAlertPresentException,NoSuchElementException
from HTMLTestRunner_PY3 import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains


'''review:
     xpath: contains() starts-with,动态xpath可以包含变量
     frame的切换 switch_to.frame
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
     js: 
        window:
                window.open
                window.scrollTo(0,)
        document:
                document.getElementsById("id").click() .value .style=''
        querySelector:document.querySelector("复制的css").click()
                
     数据驱动：
            操作excel：
            xlrd：
                excel=xlrd.open_workbook("path")
                sheet=excel.sheet_by_index(0)
                sheet.nrows.ncols
                sheet.row_values()
            一个用例循环去去excel的数据    ：下面是作业的答案            
'''


import xlrd, xlwt

excel = xlrd.open_workbook(r'C:\Users\MIME\Desktop\test.xlsx')
sheet = excel.sheet_by_index(0)
def login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    driver.find_element_by_xpath("/html/body/a").click()
    # 循环去取excel数据循环的是excel的行数(sheet.nrows)
    for i in range(sheet.nrows):
        username = int(sheet.row_values(i)[0])
        password = int(sheet.row_values(i)[1])
        print('第{0}行，用户名{1}，密码{2}'.format(i, username, password))
        driver.find_element_by_xpath("/html/body/form/p[1]/input").send_keys(username)
        driver.find_element_by_xpath("/html/body/form/p[2]/input").send_keys(password)
        driver.find_element_by_xpath("/html/body/form/p[3]/button").click()
        '''第一种方法'''
        # ele=driver.find_elements_by_xpath("//*[text()='welcome15902127953']")
        # if len(ele)>0:
        #     driver.back()
        try:
            driver.find_element_by_xpath("//*[text()='welcome15902127953']")
            return True
        except NoSuchElementException as e:
            return False


'''今日讲解：selenium接入unittest：
                                1.灵活的组织测试用例
                                2.让用例高效的执行
                                3.方便验证测试用例的结果
                                4.集成html形式测试报告
            python发送自动化测试html的邮件报告'''







class Testcase1():
    '''写一个测试类，未继承unittest'''
    def testcase1(self):
            print('用例1，点击左边的按钮，弹出alert，点击接受')
            driver=webdriver.Chrome()
            driver.get('http://127.0.0.1:5000/')
            try:
                driver.find_element_by_xpath('//*[@id="testid"]').click()
            except NoSuchElementException as e:
                print(e)
            time.sleep(2)
            text=driver.switch_to.alert.text
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

'''没有继承unittest，
 1.运行用例时，类里面有多少个测试用例，就需要调用多少次
 2.其中有一个用例失败了，导致程序停止运行，所有后面的用例也停止运行

'''
# Testcase1().testcase1()
# Testcase1().testcase2()



'''继承unittest类
 1.运行用例时，不管有多少个用例，直接用unittest.main()运行,
            unittest.main():可以方便的将一个测试模块，变为可直接运行的测试脚本
 2.其中有一个用例失败了，不影响其它用例正常运行'''

import  unittest
class Testcase(unittest.TestCase):
    '''写一个测试类，继承unittest.TestCase'''

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def testcase1(self):
            print('用例1，点击左边的按钮，弹出alert，点击接受')
            driver=self.driver
            driver.get('http://127.0.0.1:5000/')
            try:
                driver.find_element_by_xpath('//*[@id="testid"]').click()
            except NoSuchElementException as e:
                print(e)
            time.sleep(2)
            text=driver.switch_to.alert.text
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

    def testcase3(self):
        username='15902127953'
        driver=webdriver.Chrome()
        driver.get('http://127.0.0.1:5000/')
        driver.find_element_by_xpath('/html/body/a').click()
        driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
        driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
        driver.find_element_by_xpath('/html/body/form/p[3]/button').click()
        print('case2')

unittest.main()

'''
unittest特点定义总结：
1.一个class继承unittest.TestCase，即是一个个具体的TestCase（测试方法均以 test 开头，否则是不被unittest识别）
2.每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E
3.verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
4.用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境
5.参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。
6.多个单个的测试用例集合在一起，就是TestSuite
'''



'''接入html测试报告'''


# 第一步，创建一个TestSuite实例
testcase = unittest.TestSuite()

# 第二步，增加测试用例

'''第一种方法：直接用addtest+方法添加单个。
            传入参数：类名称('用例名称')
            '''
# testcases.addTest(LoginTest001('testcase2'))

'''第二种方法：直接用addtests方法添加多个测试用例，而且根据添加是顺序来执行'''

# testcases.addTests([LoginTest001('testcase2'),LoginTest001('testcase1')])

'''第三种方法：addtests+TestLoad添加测试类，而不是单个的测试用例
        loadTestsFromTestCase：参数（直接传入类名）
        loadTestsFromName:参数（传入文件模块名.类名）
        loadTestsFromNames:参数：（传入文件模块名.类名的列表）
        '''

# 例如：
# testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest001))

# testcases.addTests(unittest.TestLoader().loadTestsFromName('login01.LoginTest001'))

# testcases.addTests(unittest.TestLoader().loadTestsFromNames(['login01.LoginTest01','login01.LoginTest001']))

# 第三步：HTMLTestRunner来运行所有测试用例
now = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
f = open(r'C:\Users\MIME\Desktop\test.html', 'wb')
runner = HTMLTestRunner(stream=f, title='中文1', description='中文2')
runner.run(testcase)





'''python发送邮件的函数,导入email模块
导入smtplib模块；'''
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart



'''例一：发送普通邮件，'''

def sendemail1():
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




'''例二：带附件的邮件'''
def sendemail2():
    '''发送邮件函数'''

    '''第一步，创建数据'''
    smtpserver = 'smtp.163.com'         # 定义变量，邮件服务器
    sender='15902127953@163.com'       #定义变量，发送人
    password='test123456'              #发送人的密码
    receiver = '15902127953@163.com'       #定义变量， 接收人

    '''第二步，实例化MIMEMultipart对象，在通过attach方法增加邮件正文和附件
    		Header类只需要理解用来转换编码的'''
    content = MIMEMultipart()
    content.attach(MIMEText('hello', 'html', 'utf-8'))  # 增加邮件正文
    content['from'] = Header(sender, 'utf-8')
    content['to'] = receiver
    content['subject'] = Header('包含附件', 'utf-8')

    '''增加附件，'''
    # 通过open方法打开一个文件，并且read（），
    att = MIMEText(open(r'C:\Users\MIME\Desktop\test.html',encoding='utf-8').read())

    # 这句话说明该文件以附件形式展示，上课以详细展示了效果
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    content.attach(att)


    '''邮件发送过程，通过smtplib模块中的SMTP类'''
    server = smtplib.SMTP(smtpserver, 25)   #实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

    server.set_debuglevel(1)                #打印log

    server.login(sender, password, )        #先登录邮件服务器。参数1：发送人；参数2：密码

    server.sendmail(sender, receiver,content.as_string())   #发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

    server.quit()                           #退出邮件服务器

'''homework：写俩个用例
        用例1：查询一个正确的快递单号，循环查询快递公司
        用例2：与客服聊天对话
        
'''

