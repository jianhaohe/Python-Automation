# Python-Automation

1.cd到本地仓库文件夹，建立git仓库 ：
  git init
2.将本地的仓库关联到GitHub，后面的https改成自己的地址:
  git remote add origin https://github.com/jianhaohe/Python-Automation
3.上传github之前pull一下
  git pull origin master
4.上传代码到GitHub远程仓库
  git push -u origin master


更新代码
第一步：查看当前的git仓库状态，可以使用git status
git status
第二步：更新全部
git add *
第三步：接着输入git commit -m "更新说明"
git commit -m "更新说明"
第四步：先git pull,拉取当前分支最新代码
git pull
第五步：push到远程master分支上
git push origin master
