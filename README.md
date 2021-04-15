# daily_check_in

利用 github 的 Actions 功能和定向爬虫，  
实现每天自动登录目标网站并签到的功能

# OCR 接口
账号登陆需要验证码识别，本项目使用百度OCR 接口  
  
### 注册 baidu-OCR 接口  
1. 登录 https://login.bce.baidu.com/  
产品服务 → 人工智能 → 文字识别  
  
[![wyFR3j.png](https://s1.ax1x.com/2020/09/15/wyFR3j.png)](https://imgchr.com/i/wyFR3j)  
___
2. 点击创建应用后随便填写完成应用创建  
  
[![wyFyE8.png](https://s1.ax1x.com/2020/09/15/wyFyE8.png)](https://imgchr.com/i/wyFyE8)  
[![wyFc4g.png](https://s1.ax1x.com/2020/09/15/wyFc4g.png)](https://imgchr.com/i/wyFc4g)  
___  
3. 成功创建后在左侧菜单进入**应用列表**，就可以看到百度OCR API 的信息。  
  
[![wyF6US.png](https://s1.ax1x.com/2020/09/15/wyF6US.png)](https://imgchr.com/i/wyF6US)  
[![wyFWgs.png](https://s1.ax1x.com/2020/09/15/wyFWgs.png)](https://imgchr.com/i/wyFWgs)  
___  
### 在 GitHub 项目中设置百度OCR API 的信息
回到 GitHub 该项目中 settings → secrets 中创建名为 ‘**BAIDUOCR_CONFIG**’ 的条目，依次填写百度OCR API 的信息。  
  
[![wyF2CQ.png](https://s1.ax1x.com/2020/09/15/wyF2CQ.png)](https://imgchr.com/i/wyF2CQ)  
  


## RAINPAT 润雨专利
查询专利
