import codecs
import re
import os


inputFile = "./source/test.md"
Templates = './templates/'

class genIndexPage:
    
    def __init__(self):
        pass
        self.html = self.loadHtml("./templates/base.html") 
        self.html = self.addTitle(self.html,'首页')
        self.html = self.addContent(self.html,'./templates/header.html',"{% include 'header.html' %}")
        self.html = self.addContent(self.html,'./templates/footer.html',"{% include 'footer.html' %}")
        self.html = self.addList(self.html,"./templates/index/list.html",'./source')
        self.genHtml(self.html,"index.html")
        
        
    def addTitle(self,baseHtml,title):
        newHtml = []
        for i,line in enumerate(baseHtml):
            if re.search("{% block title %}{% endblock %}",line):
                new_line = line.replace("{% block title %}{% endblock %}",title)
                newHtml.append(new_line) 
            else:
                newHtml.append(line)
        return newHtml
    
        
    def addList(self,baseHtml,template,originMDfile):
        tempHtml = self.loadHtml(template)
        new_lines = []
        filenames = os.listdir(originMDfile)
        for line in tempHtml:
            if re.search("{{article_list}}",line):
                for _,filename in enumerate(filenames):
                    if re.findall(".md",filename):
                        filenam = os.path.splitext(filename)[0]
                        new_line = line.replace("{{title}}",filenam)
                        htmldir = "./post"+"/"+filenam+'.html'
                        new_line = new_line.replace("{{article_list}}",htmldir)
                        new_lines.append(new_line)
            else:
                new_lines.append(line)
        return self.addContent(baseHtml=baseHtml,target=new_lines,flag="{% block content %}{% endblock content %}")   
        
         
    def loadHtml(self,html):
        with codecs.open(html,mode='r',encoding="utf-8") as f:
            baseHtml = f.readlines()
            f.close()
        return baseHtml
    
    def addContent(self,baseHtml,target,flag):
        
        if not isinstance(target,list):
            if not os.path.isdir(target):
                targetHtml = self.loadHtml(target)
        else:
            targetHtml = target  
        newHtml = []
        for i,line in enumerate(baseHtml):
            if re.search(flag,line):
                for j,target in enumerate(targetHtml):
                    newHtml.append(target)
            else:
                newHtml.append(line)
        return newHtml
    
    def genHtml(self,html,htmlfile):
        with codecs.open(htmlfile,mode='w',encoding='utf-8') as f:
            f.truncate(0)
            f.writelines(html)
            f.close()



class genContentPage:
    
    def __init__(self):
        pass
        self.html = self.loadHtml("./templates/base.html") 
        self.html = self.addTitle(self.html,'首页')
        self.html = self.addContent(self.html,'./templates/header.html',"{% include 'header.html' %}")
        self.html = self.addContent(self.html,'./templates/footer.html',"{% include 'footer.html' %}")
        self.html = self.addList(self.html,"./templates/index/list.html",'./source')
        self.genHtml(self.html,"index.html")
        
        
    def addTitle(self,baseHtml,title):
        newHtml = []
        for i,line in enumerate(baseHtml):
            if re.search("{% block title %}{% endblock %}",line):
                new_line = line.replace("{% block title %}{% endblock %}",title)
                newHtml.append(new_line) 
            else:
                newHtml.append(line)
        return newHtml
    
        
    def addList(self,baseHtml,template,originMDfile):
        tempHtml = self.loadHtml(template)
        new_lines = []
        filenames = os.listdir(originMDfile)
        for line in tempHtml:
            if re.search("{{article_list}}",line):
                for _,filename in enumerate(filenames):
                    if re.findall(".md",filename):
                        filenam = os.path.splitext(filename)[0]
                        new_line = line.replace("{{title}}",filenam)
                        htmldir = "./post"+"/"+filenam+'.html'
                        new_line = new_line.replace("{{article_list}}",htmldir)
                        new_lines.append(new_line)
            else:
                new_lines.append(line)
        return self.addContent(baseHtml=baseHtml,target=new_lines,flag="{% block content %}{% endblock content %}")   
        
         
    def loadHtml(self,html):
        with codecs.open(html,mode='r',encoding="utf-8") as f:
            baseHtml = f.readlines()
            f.close()
        return baseHtml
    
    def addContent(self,baseHtml,target,flag):
        
        if not isinstance(target,list):
            if not os.path.isdir(target):
                targetHtml = self.loadHtml(target)
        else:
            targetHtml = target  
        newHtml = []
        for i,line in enumerate(baseHtml):
            if re.search(flag,line):
                for j,target in enumerate(targetHtml):
                    newHtml.append(target)
            else:
                newHtml.append(line)
        return newHtml
    
    def genHtml(self,html,htmlfile):
        with codecs.open(htmlfile,mode='w',encoding='utf-8') as f:
            f.truncate(0)
            f.writelines(html)
            f.close()


genIndexPage()
