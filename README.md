# Learn-neo4j
安装(ubuntu)：

0: add-apt-repository ppa:webupd8team/java
1: apt install software-properties-common
2: apt-get update
3: apt-get install oracle-java8-installer
注：不要安装java9,官网提示不兼容

4: wget --no-check-certificate -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
5: echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list
6: apt update
7: apt-get install neo4j=1:3.4.1

8: 设置密码，默认用户neo4j,此处密码设置为123456
   neo4j-admin set-initial-password 123456

9: 启动
   mkdir /var/run/neo4j
   neo4j start

10: 
 http://localhost:7474/


python driver：

1: neo4j-driver 原生态的driver
安装: 
     pip install neo4j-driver

example:
    https://github.com/neo4j-examples/movies-python-bolt

2: Py2neo 第三方模块，个人感觉相对好用
安装:
   pip install py2neo==2.0.9

4: Neo4jRestClient
   source: https://github.com/versae/neo4j-rest-client
   Example: https://github.com/neo4j-examples/movies-python-neo4jrestclient

5: Bulbflow
   
参考文档：
1: https://neo4j.com/developer/python/#_py2neo
 
