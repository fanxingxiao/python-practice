GitHub本地仓库创建过程，\n
登录GitHub官网，注册账号；\n
点击 ‘用户名’ 旁边的 ‘+’ -> New repository -> 输入名字 -> Create repository；\n
本地安装gitbash；\n
git clone https://github.com/fanxingxiao/python-practice.git；\n
cd python-practice；\n
vim README.md；\n
echo python-practice；\n
:wq；\n
git add README.md；\n
git commit -m "first commit"；\n
git config user.name [github用户名]；\n
git config user.email [github邮箱]；\n
git remote add python-practice https://github.com/fanxingxiao/python-practice.git；\n
git push -u python-practice master；\n
[修改后提交、同步]；\n
git add README.md；\n
git commit -m "提交说明"；\n
git push -u python-praction master；\n
