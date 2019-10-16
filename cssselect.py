import requests

from lxml import html

etree = html.etree


from lxml.etree import *

req = requests.Request(
    method='get',
    url='https://ke.qq.com/course/list/python',
    params={
        'price_min':'1',
        'page':'2'
    },
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
)
pre_req = req.prepare()

session = requests.session()
response = session.send(pre_req)
cont = response.content.decode('utf-8')
#doc
doc = etree.HTML(cont)
# print(doc)
#tree
tree = doc.getroottree()
# print(tree)
# doc.cssselect('',translator='html') #实际上底层只支持xpath 我们使用css选择器最终是翻译成 xpath 然后执行
# nodes = doc.cssselect('section') #所以
# print(type(nodes),nodes)
#
# nodes = doc.cssselect('section,html')  #或
# print(type(nodes),nodes)

# nodes = doc.cssselect('html section')  #html下的section
# print(type(nodes),nodes)
#
# nodes = doc.cssselect('html>body')  #html下的所有子节点head
# print(type(nodes),nodes)

# nodes = doc.cssselect('head+body')  #head的兄弟节点
# print(type(nodes),nodes)



# nodes = doc.cssselect('header#js_main_nav')  #id（#）
# print(type(nodes),nodes)


# nodes = doc.cssselect('.hidden-clip')  #class（.）
# print(type(nodes),nodes[0])

# nodes = doc.cssselect('.main.autoM.clearfix')  #id（#）多个class不要加空格  js里加空格<input class="dd ee" >
# print(type(nodes),nodes[0])

# nodes = doc.cssselect('div[data-report-module]')  #属性
# print(len(nodes),nodes[0])
#
# nodes = doc.cssselect('div[data-report-module="middle-course"]')  #属性
# print(len(nodes),nodes[0])
#
# nodes = doc.cssselect('div[data-report-module^="middle"]')  #属性开头是...
# print(len(nodes),nodes[0])
#
# nodes = doc.cssselect('div[data-report-module$="course"]')  #属性结尾是、、、
# print(len(nodes),nodes[0])
#
# nodes = doc.cssselect('div[data-report-module*="course"]')  #属性包含
# print(len(nodes),nodes[0])


# nodes = doc.cssselect('div[class~="main-left"]')  #属性包含
# print(len(nodes),nodes)
#
# nodes = doc.cssselect('div[class|="main-left"]')  #属性以。。开头
# print(len(nodes),nodes)

# nodes = doc.cssselect('div[class~="main-left"]>div:last-child')  #最后一个子元素div
# print(len(nodes),nodes)


nodes = doc.cssselect('div[class~="main-left"]>div:nth-child(2)')  #第2个子元素div
print(len(nodes),nodes)