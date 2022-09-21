import codecs
import markdown 

with codecs.open(r'D:\ShareCache\2019000051_袁帅\Md2html\source\test.md',mode='r',encoding="utf-8") as f:
    html = f.read()    
    f.close()

extensions = ['markdown.extensions.toc',
            'markdown.extensions.fenced_code',
             'markdown.extensions.tables']
html = markdown.markdown(html)
print(html)