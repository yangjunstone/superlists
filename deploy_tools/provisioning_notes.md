配置新网站
===============

##需要安装的包：
* nginx
* Python3
* Git
* pip
* virtualenv

以centos7为例， 可以执行以下安装命令：
yum install nginx git python3 python3-pip
pip3 install virtualenv

配置Nginx虚拟主机

*参考nginx.template.con
*把SITENAME替换成所需的域名， 例如www.staging.yangjunstone.cn

##Gunicorn服务器开机启动
参考gunicorn.service.template.conf 在centos7下生成gunicorn.service文件，通过systemctl[start, stop, reload]启动
把SITENAME替换成所需的域名， 例如www.staging.yangjunstone.cn
备注： 目前Start gunicorn服务器报time out错误，需进一步调试

##文件夹结构
SITENAME
 |----database
 |----source
 |----static
 |----virtualenv