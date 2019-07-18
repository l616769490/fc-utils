# 函数计算工具库

## 安装使用
``` shell
pip install fcutils
```
## FCHttpUtils
#### getData(host)
发送get请求获取数据
- 参数  
host：请求接口地址
- 返回值  
请求的结果，由具体的接口确定
#### getDataForJson(host, data)
发送post请求获取数据
- 参数  
host：请求的接口地址   
data：json格式的请求数据
- 返回值  
请求的结果，由具体的接口确定
#### getDataForStr(host, data)
发送post请求获取数据
- 参数  
host：请求的接口地址  
data：字符串格式的请求数据
- 返回值  
请求的结果，由具体的接口确定

## JwtUtils
#### encode(payload, priv_key)
使用jwt规则进行加密
- 参数  
payload：需要加密的数据  
priv_key：私钥
- 返回值  
加密后的数据
#### decode( encoded_str, pub_key)
使用jwt规则进行解密
- 参数  
encoded_str：需要解密的数据  
pub_key：公钥
- 返回值  
解密结果

## OSSUtils
#### \_\_init__(self, accessKeyId, accessKeySecret, bucketName, endpoint)
- 参数  
accessKeyId: 阿里云accessKeyId  
accessKeySecret: 阿里云accessKeySecret  
bucketName: bucket名字
#### getFileList(path)
获取文件列表
- 参数  
dirName: 父路径
- 返回值  
status：成功返回200，失败返回错误码  
data：成功返回数据，失败返回错误信息

#### getFileByName(path)
获取文件内容
- 参数  
path: 文件路径
- 返回值  
status：成功返回200，失败返回错误码  
data：成功返回数据，失败返回错误信息
#### updateFile(data, path)
更新文件，没有则新建
- 参数  
path: 文件路径
- 返回值  
status：成功返回200，失败返回错误码  
data：成功返回数据，失败返回错误信息

## PwdUtils
#### createPwd(password, salt)
生成加密密码
- 参数  
password: 密码  
salt: 盐值
- 返回值  
加密后的密码
#### createSalt(length = 6)
生成盐值
- 参数  
length: 盐值长度
- 返回值  
盐值


