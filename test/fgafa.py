from markdown import extensions
from markdown.treeprocessors import Treeprocessor
import markdown

class BootstrapTreeprocessor(Treeprocessor):
    """
    """

    def run(self, node):
        for child in node.getiterator():
            # 如果是 table
            if child.tag == 'table':
                child.set("class", "table table-bordered table-dark")
            elif child.tag == 'h2':
                child.set("class", "h5 text-secondary mb-4")
            # elif child.tag == 'img':
            #    child.set("class","img-fluid")
        return node


class BootStrapExtension(extensions.Extension):
    """
    """

    def extendMarkdown(self, md):
        """
        """
        md.registerExtension(self)
        self.processor = BootstrapTreeprocessor()
        self.processor.md = md
        self.processor.config = self.getConfigs()
        md.treeprocessors.add('bootstrap', self.processor, '_end')

s="""|**name**|**age**|
|---|---|
|tim| 16|
|tom| 17|
"""
print(markdown.markdown(s,extensions=['markdown.extensions.toc',
                                        'markdown.extensions.fenced_code',
                                        'markdown.extensions.tables',BootStrapExtension()]))