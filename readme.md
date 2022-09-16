# 一个静态博客生成脚本

缓慢搭建中。。。。。。


## 1.搭建思路

### 1.1 内容
目前内容分为三部分
1) 列表
2) 分类
3) 文章详情

### 1.2 结构
框架分为几个模块
1) templates: 网页模板
2) post：存放生成的html文件和图片文件夹
3) source 存放需要转换的markdown文件
4) index.html 生成的主页文件
5) main.py 脚本文件

### 1.3 步骤

#### 1.3.1 构建模板
./templates/base.html 是构建网页的基础模板，里面定义了网页的风格，头，尾及内容，通过替换对应的占位符即可定义
具体做法如下
* 加载base.html
* 添加标题("{% block title %}{% endblock %}")
* 添加头("{% include 'header.html' %}")
* 添加尾("{% include 'footer.html' %}")
* 添加内容("{% block content %}{% endblock content %}")

#### 1.3.2 生成列表网页

./templates/list.html 中设定了列表网页的模板，解析markdown文件标题，替换list.html的占位符即生成了列表内容，将列表内容替换为模板中的内容即可

* 加载list.html
* 遍历source文件夹下所有md文件,获取文章标题
* 替换list.html中"<a href={{article_list}}  {{title}}</a>"
* 加list.html添加到模板中
* 创建index.html

#### 1.3.3 生成文章内容网页
./templates/content.html 中设定了列表网页的模板，解析markdown文件内容，替换content.html的占位符即生成了内容，将内容替换为模板中的内容即可

* 加载content.html
* 遍历source文件夹下所有md文件,获取文章内容，文件名
* **将文章内容转换为html**
* 替换content.html中的占位符
* 将content.html添加到模板中
* 创建"./post/文件名.html"

