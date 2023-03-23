⚠️注：目前chatgpt的api在国内已经被墙了，微信云托管的服务器是国内的。所以大家就不要尝试了，如果给大家造成了困扰，这了表示真诚的歉意～

## 快速部署

> 必备条件：
>
> `api_key`：[官网](https://platform.openai.com/account/api-keys)获取
>
> `服务器`：微信云托管免费使用3个月的环境，还附赠MySQL
>
> `源码`：直接fork该仓库即可

### 准备源码

fork一下（可放心公开，api_key写进了环境变量里，不在代码中展示）

### 部署服务器

- 进入控制台：在公众号管理界面-开发者工具-点选进入微信云托管-点击免费试用

- 部署：服务列表-模版部署-点选使用flask-直接部署，等待完成就行

- 填写环境变量API_KEY：在服务设置的最下方的环境变量中增加一行，填上自己的密钥就行。

- 发布：点击发布-绑定GitHub仓库-选择自己的仓库-分支选master-端口默认80，然后点发布等待发布完成就行，如下图。

- 消息推送：设置-全局设置-消息推送-path地方填【/wechat】-推送模式选【XML】-提交。然后扫码确认即可。


### 公众号上测试

![image-20230305172627375](https://gitee.com/HsuHeinrich/images/raw/master/img/20230305172627.png)

