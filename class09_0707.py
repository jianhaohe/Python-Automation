from selenium import webdriver
import unittest,xlrd,xlwt
import  pymysql

'''
第一阶段：
1.输入输出：
	print
	input
	注释
2.python运算


3.数据类型：
	int
	str
	float
	list
	dict
	tuple

4.切片


5.循环
	while: continue ,breake
	true:
	flase:

  for i in list
  for i in range(0,10,2)

5.条件判断：
   if else:
      if elif


6.def 函数名：
   pass
   参数，
   return;

7.class

8.操作文件 txt excel mysql


第二阶段：
	selenium：
	常用基本操作：
		get
		refresh

	鼠标键盘：Keys,ActionChains
	TAB ENTER
	click_and_hold
	release
	move_to_ele
	drag_and_drop
	Actionschains(driver).move_to_ele().perform

	定位元素8中方法
	xpath
	js


	unittest
		1.testcase=unittest.TestSuite()
		2.testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest001))
		3.unittest.TextTestRunner().run(testcase)


	dir=''
	firle=open(dir,'wb')
	runner=HtmlTestRunner(stream=file)
	runner.run(testcase)

	SMTP
	email
	1.定义一些变量数据
		server=smtp.163.com

	2.MIMETEST(''，'html','utf-8')


RF
	click elment   ${点击登录}


	setting
	Library    selenium
	Library    py
	Resoure   ..////..
	Suite setup
	test setup
	teardown


	testcase



	:keyword

	:argument   arg1=0    arg
	retun


	variable



    :for
    :run keyword if
        run keywords  and



# '''


'''练习一'''
# xing=input('firstname:')
# ming=input('lastname:')
# age=float(input('工作年限：'))
# bug1=int(input('bug1:'))
# bug2=int(input('bug2:'))
# print('个人信息：名字%s 工作年限：%.2f 今日提交bug%d'%(xing+ming,age,bug1+bug2))


'''练习二'''
# str='welcomy'
# x=0
# for i in range(0,len(str)):
# 	if x<=len(str)-1:
# 		print(str[x],end='')
# 		x=x+2





'''
练习三
			  x个数  空格数
     x          1    5
    xxx         3    4
   xxxxx        5    3
  xxxxxxx       7    2
 xxxxxxxxx      9    1
xxxxxxxxxxx     11   0
 i表示第几行
（x个数）      x=2*i-1  
 (空格数个数)  space=6-i
'''

#方法一：定义俩个变量，一个表示空格，一个表示x的数量
m=1
n=5
while  m<12:
	print(' '*n+'x'*m)
	m+=2
	n-=1


#方法二：定义一个变量
i=1
while i<7:
	w = ' '
	print((6-i)*w+(2*i-1)*'x')
	i = i+1

'''练习四'''
list=[1,2,'str',[4,5,6]]

def test(list):
	for ele in list:
		if  type(ele)!=int and type(ele)!=str:
			list.remove(ele)
			for x in ele:
				list.append(x)
	return list
print(test(list))




#如果list后面还有元素，方法一：定义一个新的list，
L = [1,'str',3,[4,5,6],8,9,0]
def test(list):
	M = []
	for ele in list:
	    if type(ele) == int or type(ele) == str:
	        M.append(ele)
	    else:
	        for x in ele:
	            M.append(x)
	return M
print(test(L))


#如果list后面还有元素，方法二：就改变原来的list

list = [1,2,'str',[4,5,6],7,8,9]

def test(list):
	for ele in list:
	    if type(ele) not in [int,str]:
	        list.remove(ele)
	        index = list.index('str')+1
	        for x in range(len(ele)):
	            list.insert(index+x,ele[x])
	return list
print(test(list))




'''练习五'''
class TestLogin(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print('这是初始化方法')
		self.write_data(self)
		self.driver = webdriver.Chrome()
		self.driver.get('http://127.0.0.1:5000/')
		self.driver.implicitly_wait(5)
		self.driver.find_element_by_xpath('/html/body/a').click()

	def login_web(self, username, password):
		driver = self.driver
		driver.find_element_by_xpath('/html/body/form/p[1]/input').clear()
		driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys(username)
		driver.find_element_by_xpath('/html/body/form/p[2]/input').clear()
		driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys(password)
		driver.find_element_by_xpath('/html/body/form/p[3]/button').click()

	def write_data(self):
		username = ['', '15902127959', '15902127953', '15902127955', '15902127953', '15902127953']
		password = ['123456', '123456', '123457', '123455', '', '123456']
		excel = xlwt.Workbook()
		sheet = excel.add_sheet('test1')
		sheet.write(0, 0, 'username')
		sheet.write(0, 1, 'password')
		for i in range(0, len(username)):
			sheet.write(i + 1, 0, username[i])
			sheet.write(i + 1, 1, password[i])
		excel.save('test.xls')

	def read_data(self,i):
		excel = xlrd.open_workbook('test.xls')
		sheet = excel.sheet_by_index(0)
		data = sheet.row_values(i, 0, 2)
		return data

	def testcase01(self):
		username=self.read_data(1)[0]
		password=self.read_data(1)[1]
		self.login_web(username,password)
		self.assertEqual(self.driver.title,'登录页面')

	def testcase02(self):
		username=self.read_data(6)[0]
		password=self.read_data(6)[1]
		self.login_web(username,password)
		self.assertEqual(self.driver.title,'登录页面')
	@classmethod
	def tearDownClass(self):
		self.driver.close()





'''python连接数据库mysql'''


def connect():
	'''连接数据库'''
	db=pymysql.connect('localhost','root','test123456','robot')
	return db

def create_table(db):
	'''创建表'''
	cursor = db.cursor()
	sql="""
	    create table test(
	    id CHAR(20),
	    name CHAR (12),
	    number VARCHAR (13)
	     )
	"""
	cursor.execute(sql)


def insert_data(db):
	'''表中插入数据'''
	cursor = db.cursor()

	sql='''insert into test values
	(001,'jianhaohe',12345678978),
	(002,'zhoujielun',1234567989)
	'''
	cursor.execute(sql)
	db.commit()


def query_db(db):
	'''查询数据'''
	cursor = db.cursor()
	sql='''select * from test
	'''
	cursor.execute(sql)
	res=cursor.fetchall()
	data=res[0][2]
	print(data)
	print(res)

def close_db(db):
	'''关闭数据库'''
	db.close()


def main():
	'''方法执行顺序'''
	db=connect()
	create_table(db)
	insert_data(db)
	query_db(db)
	close_db(db)

if __name__=='__main__':
	main()






'''上周作业'''

'''
*** Test Cases ***
case01
    [Documentation]   用例1，查快递：单号错误，继续输入，单号正确，进入查询页面
    goto check_number page   #登录后进入查询页面
    @{list}    create list    123456    ${number}       ${number1}
    :FOR  ${i}  IN  @{list}
    \         input text         xpath=//*[@id="postid"]    ${i}
    \         click element when visible      xpath=//*[@id="query"]
    \         click element when visible      xpath=//*[@class='header']
    \         sleep    1
    \         ${count}              get matching xpath count        //div[@class='result-wrap']
    \         run keyword if        ${count}==1
    \         ...    run keywords   goto_checkrecord_page   AND  exit for loop
    
    
case02
	whether have check record   #定义一个关键字检查一个单号是否查询过，参数为 快递单号
    [Arguments]   ${numbers}
    ${count}     get matching xpath count      //*[@class='a-kuaidinum' and @title='${numbers}']
    run keyword if   ${count}==1
    ...  run keywords    mouse over            xpath=//*[@class='a-kuaidinum' and @title='${numbers}']
    ...  AND    click element when visible     xpath=//tr[contains(@id,'${numbers}')]/td[last()]
    ...  AND    log     删除历史数据
    ...  ELSE   log     没有历史


'''