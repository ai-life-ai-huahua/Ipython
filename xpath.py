
import requests

from lxml import html

etree = html.etree
a = "1".e


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
# pre_req = req.prepare()
#
# session = requests.session()
# response = session.send(pre_req)
# cont = response.content.decode('utf-8')
# #doc
# doc = etree.HTML(cont)
# print(cont)
#解析器
# parse = html.etree.HTMLParser()
# #加载数据产生节点：节点树 <-> 节点
# doc = html.etree.fromstring(cont,parse)
# doc = html.etree.HTML(cont)
# leng = len(doc)
#遍历方式
# for i in range(leng):
#     print(doc[i])
# doc = iter(doc)


# for i in doc:
#     print(doc[i])


#遍历（节点管理操作）
# nodes = doc.getchildren()
# for i in nodes:
#     print(i.tag,i.text)

#吧节点变换成数
# tree = doc.getroottree()
# print(type(tree))

#属性提供结婚特殊函数get（）属性值，items（），keys（），values

# nodes = doc.getchildren()
# for i in nodes:
#     print(i.items(),i.keys(),i.values(),i.get('no','缺省值'))



#1.find
#在子节点查找
# nodes = doc.findall('body')
# print(nodes)
#节点不是根  要转化为树 才可以用/根
# tree = doc.getroottree()
# nodes = tree.findall('/body')
# print(nodes)

#find不是严格的xpath  @在find不处理
# nodes = doc.xpath('body/header/@id')
# print(len(nodes))


#取文本
# nodes = doc.xpath('body/header/div/div/div/a/text()')
# print(len(nodes),nodes[0])

# #所以课程的价格
# nodes = doc.xpath('//div[@class="item-line item-line--bottom"]/span[@class="line-cell item-price"]/text()')
# print(len(nodes),nodes)
#
# #所以课程名称
# nodes = doc.xpath('//div[@class="item-line item-line--middle"]/span[@class="item-source"]/a[@class="item-source-link"]/text()')
# print(len(nodes),nodes)
#
# # nodes = doc.xpath('//span/a/text()')
# # print(len(nodes),nodes)

#访问技巧  用节点当锚点 node() 所以节点的  text（）所有文本
# nodes = doc.xpath('//div[span="¥98.00"]/span/text()')
# print(len(nodes),nodes)

#逻辑运算 + - * div mod 关系 逻辑 and or  |两个选择
# 1. find
# 节点：在子节点查找
# nodes = doc.findall('span')
# print(nodes)
# 节点的根：树才有根，才能使用/， /路径分隔符号，子节点（下一级节点）
# 。标签当前节点
# //后代节点
# nodes = doc.findall('body/.//div')
# print(len(nodes))
# tree = doc.getroottree()
# nodes = tree.findall('//div')
# print(len(nodes))
# .. 表示上一级节点
# nodes = doc.findall('body/..')
# print(len(nodes),nodes[0])
# tree = doc.getroottree()
# nodes = tree.findall('/body/..')
# print(len(nodes),nodes[0])

# find不是严格的xpath,@语法在find不处理。
# 取属性
# nodes = doc.xpath('body/header/@id')
# print(len(nodes),nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/@id')
# print(len(nodes),nodes[0])
# 取文本节点
# nodes = doc.xpath('body/header/div/div/div/a/text()')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div/div/a/text()')
# print(len(nodes),nodes)
# 按照位置取节点(第一个位置是1，最后一个位置last())
# nodes = doc.xpath('body/header/div/div/div/a/text()')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div[last()-1]')
# print(nodes)

# 使用positon()获取位置，并且做测试
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div[position()>2]')
# print(len(nodes),nodes)
# 属性测试
# tree = doc.getroottree()
# # nodes = tree.xpath('/html/body/header/div/div[@class]/@class')
# nodes = tree.xpath('/html/body/header/div/div[@class="header-index-text"]')
# print(len(nodes),nodes)

# 访问技巧(节点做测试 node() span ='￥7280.00')
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[@class="item-line item-line--bottom"]/span[@class="line-cell item-price"]/text()')
# nodes = tree.xpath('//span/a/text()')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[span="¥7280.00"]/span/text()')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span[text()="¥7280.00"]/@*')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[node()="¥7280.00"]/span/text()')
# print(len(nodes), nodes)

# 测试做逻辑运算 + - * div  mod 关系， 逻辑， and or
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[node()="¥7280.00" and not(@class="item-line item-line--bottom")]/span/text()')
# print(len(nodes), nodes)
# 多个节点合并
# tree = doc.getroottree()
# # nodes = tree.xpath('//div/span/a/@title | //h4/a/text()')
# # print(len(nodes), nodes)

# xpath轴
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[text()="马哥教育"]/parent::*/parent::*/parent::*/h4/a/@title')
# print(len(nodes), nodes)

# # 节点的类型测试  comment注释节点
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body//div[comment()]')
#
# print(len(nodes), nodes)

# xpath函数

# tree = doc.getroottree()
# nodes = tree.xpath(
#     '//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[substring(text(),1,2)="马哥"]')
# nodes = tree.xpath(
#     '//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[starts-with(text(),"马哥")]')
#
# print(len(nodes), nodes)


