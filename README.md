# solitaire-miniprogram #
**微信接龙小程序脚本**  
![Markdown](http://i4.bvimg.com/604676/fd0e52650fb0cc4f.png)

# 版本支持 
**Python3.x**  

# 使用方法 

**1.安装Python，此处移步[Python 基础教程](http://www.runoob.com/python/python-tutorial.html)**  

**2.安装相关的包**  
<pre>pip install requests</pre>  
<pre>pip install json</pre>  

**3.获取userID**  
此处用到Charles抓包工具，移步[charles的使用-简书](https://www.jianshu.com/p/fb2bdde5b498)  

> 完成以后配置步骤后，打开微信上已接过龙的小程序，点开json数据栏，然后根据自己的微信昵称来查找自己的userID  

之后修改*info.py*(用于显示接龙上面的名字)并保存退出，代码例子：  
    
	# coding=utf-8

	INFODICT = {
	    '姓名' : 'userID'
	}
	

**4.获取最新的接龙房间号**  
浏览器奇前往，手动修改房间号  
> https://solitaire.sayweee.cn/index.php/solitaire/api/events/房间号  

例子演示：  
![Markdown](http://i1.bvimg.com/604676/95954d6353e70c2d.png)  
如果json数据中的result位false则表示此接龙房间号已被占用  
![Markdown](http://i1.bvimg.com/604676/d2aa7c0ed6a41c23.png)
若为false则相反，但不一定代表是最新的房间号，需要满足它下一个房间号的result也为false  
> 那么如何获取你想要接龙的接龙房间号呢？首先，最好在十分钟前就折半查找出最新的房间号  

**5.修改solitaire.py中的全局变量**  
找到两个全局变量，分别是：<pre>KEYWORD</pre><pre>START_POSITION</pre>  

*KEYWORD -- 发起接龙者的微信昵称*  
*START_POSITION -- 起始房间号，需要用最新房间号-1*  

代码演示：  
    
	KEYWORD = ''
	START_POSITION = 155554  

**6.运行脚本**  
*打开cmd,输入*  
<pre>python solitaire.py</pre>  


----------
**在我的阿里云上的运行结果**  
![Markdown](http://i2.bvimg.com/604676/cf282caedba1e65e.jpg)