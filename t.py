import top.api
long =''
url = 'https://item.taobao.com/item.htm?spm=a21c9.8840246.pinzhi.1.35b0d0adR5KvC2&id=520055109160'
appkey ='27957360'
secret='ccaf71c91a5109d2eb00daf18d40a566'
req = top.api.TopatsResultGetRequest(url)
req.set_app_info(top.appinfo(appkey, secret))
req.fields = "title,nick,price"

resp = req.getResponse()



print(resp)
