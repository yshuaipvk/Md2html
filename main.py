import codecs
from importlib.machinery import all_suffixes
from operator import index
import markdown
import re
import os


inputFile = "./source/test.md"
Templates = './templates/'



def md2html(file):
    """将markdown转换为html
    Args:
        file (_type_): markdown文件地址
    Returns:
        _type_: _description_
    """
    exts = ['markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code']
    with codecs.open(file,mode='r',encoding="utf-8") as f:
        text = f.read()
        html = markdown.markdown(text,extensions=exts)
    return html

def loadHtml(html):
    """加载html文件

    Args:
        html (_type_): _description_

    Returns:
        _type_: _description_
    """
    with codecs.open(html,mode='r',encoding="utf-8") as f:
        baseHtml = f.readlines()
        f.close()
    return baseHtml

def addTitle(baseHtml,title):
    """替换添加html的标题

    Args:
        baseHtml (_type_): _description_
        title (_type_): _description_

    Returns:
        _type_: _description_
    """
    newHtml = []
    for i,line in enumerate(baseHtml):
        if re.search("{% block title %}{% endblock %}",line):
            line = line.replace("{% block title %}{% endblock %}",title)
        newHtml.append(line) 
    return newHtml

def addContent(baseHtml,targets,flag):
    """向html中添加特定的内容
    Args:
        baseHtml (_type_): 基础html
        targets (_type_): 需要添加的内容
        flag (_type_): 添加内容的占位符

    Returns:
        _type_: _description_
    """
    newHtml= []
    for i,line in enumerate(baseHtml):
        if re.search(flag,line):
            for j,target in enumerate(targets):
                newHtml.append(target)
        else:
            newHtml.append(line)
    return newHtml

def genHtmlFile(file,html):
    """将html写入文件
    Args:
        file (_type_): _description_
        html (_type_): _description_
    """
    with codecs.open(file,mode='w',encoding='utf-8') as f:
        f.truncate(0)
        f.writelines(html)
        f.close()


def addList(baseHtml,postDir,sourceDir):
    """根据markdown文件名称生成article list的html
        用于替换base.html中的内容
    Args:
        baseHtml (_type_): listBase.html中的内容,定于了article的格式
        postDir (_type_): 文章内容html文件所在位置
        filenames (_type_): markdown文件名称
    Returns:
        article list的html
    """
    new_lines = []
    filenames = os.listdir(sourceDir)
    for line in baseHtml:
        if re.search("{{article_list}}",line):
            for _,filename in enumerate(filenames):
                if re.findall(".md",filename):
                    filenam = os.path.splitext(filename)[0]
                    new_line = line.replace("{{title}}",filenam)
                    htmldir = postDir+"/"+filenam+'.html'
                    new_line = new_line.replace("{{article_list}}",htmldir)
                
                    new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines

def genBase():
    basehtml = loadHtml(Templates+"base.html")
    headerhtml = loadHtml(Templates+'header.html')
    footerhtml = loadHtml(Templates+'footer.html')
    basehtml = addContent(basehtml,headerhtml,flag="{% include 'header.html' %}")
    basehtml = addContent(basehtml,footerhtml,flag="{% include 'footer.html' %}")
    return basehtml

c = './source'


a = os.listdir(c)
for b in a:
    path = os.path.join(c,b)
    if not os.path.isdir(path) and re.findall('.md',b):
        filename = os.path.splitext(b)[0]
        html = md2html(path)
        basehtml = genBase()
        basehtml = addTitle(basehtml,filename)
        basehtml = addContent(basehtml,html,flag="{% block content %}{% endblock content %}")
        genHtmlFile(os.path.join('./post',filename+'.html'),basehtml)

listHtml = loadHtml(Templates+'list.html')
listHtml = addList(listHtml,'./post','./source')

indexbase = genBase()
indexbase = addTitle(indexbase,'首页')
indexbase = addContent(indexbase,listHtml,flag="{% block content %}{% endblock content %}")
genHtmlFile("index.html",indexbase)