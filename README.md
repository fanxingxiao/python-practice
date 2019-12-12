GitHub本地仓库创建过程，

登录GitHub官网，注册账号

点击 ‘用户名’ 旁边的 ‘+’ -> New repository -> 输入名字 -> Create repository

本地安装gitbash

git clone https://github.com/fanxingxiao/python-practice.git

cd python-practice

vim README.md

echo python-practice

:wq

git add README.md

git commit -m "first commit"

git config user.name [github用户名]

git config user.email [github邮箱]

git remote add python-practice https://github.com/fanxingxiao/python-practice.git

git push -u python-practice master

[修改后提交、同步]

git add README.md

git commit -m "提交说明"

git push python-practice master

git pull python-practice master
