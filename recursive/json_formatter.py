# -*- encoding: utf-8 -*-


class JsonFormatter:
    def __init__(self, intend=4, name="", encoding="utf-8"):
        '''
        intend: 缩进空格数
        name: 文件名
        encoding: 文件编码
        '''
        self.name = name
        self.intend = intend
        self.encoding = encoding
        self.stack = []
        self.obj = None
        self.source = self.get_source(name, self.encoding)
        self.prepare()

    @staticmethod
    def json_str(s):
        '''
        给字符串套上双引号
        '''
        return '"' + s + '"'

    @staticmethod
    def get_source(name, encoding="utf-8"):
        with open(name, 'r', encoding=encoding) as f:
            # 当不给split函数传递任何参数时，分隔符sep会采用任意形式的空白字符：空格、tab、换行、回车以及换页符
            return ''.join(f.read().split())

    def prepare(self):
        try:
            self.obj = eval(self.source)
        except:
            # json string 一定满足python dict和list的组合
            raise Exception('Invalid json string!')

    def line_intend(self, level=0):
        return '\n' + ' ' * self.intend * level

    def parse_dict(self,obj=None,intend_level=0):
        if intend_level == 0:
            # 这个判断是为了防止文件开头出现空行
            self.stack.append('{')
        else:
            self.stack.append(self.line_intend(intend_level)+'{')
        intend_level += 1
        i = 0
        for key, value in obj.items():
            key = self.json_str(str(key))
            self.stack.append(self.line_intend(intend_level)+key+':')
            self.parse(value, intend_level)
            if i != len(obj.items())-1:
                # 这个处理是为了防止最后一对kv后面还有个逗号，这样会造成json.load()函数无法读取
                self.stack.append(',')
            i += 1
        self.stack.append(self.line_intend(intend_level-1)+'}')

    def parse_list(self, obj=None, intend_level=0):
        if intend_level == 0:
            self.stack.append('[')
        else:
            self.stack.append(self.line_intend(intend_level)+'[')
        intend_level += 1
        for i, item in zip(range(0, len(obj)), obj):
            self.parse(item, intend_level)
            if i != len(obj)-1:
                self.stack.append(',')
        self.stack.append(self.line_intend(intend_level-1)+']')

    def parse(self, obj, intend_level=0):
        if obj is None:
            self.stack.append('null')
        elif obj is True:
            self.stack.append('true')
        elif obj is False:
            self.stack.append('false')
        elif isinstance(obj, (int, float)):
            self.stack.append(str(obj))
        elif isinstance(obj, str):
            self.stack.append(self.json_str(obj))
        elif isinstance(obj, (list, tuple)):
            self.parse_list(obj, intend_level)
        elif isinstance(obj, dict):
            self.parse_dict(obj, intend_level)
        else:
            raise Exception('Invalid json type %s!' % obj)

    def render(self):
        self.parse(self.obj, 0)
        res_file = self.name
        res = ''.join(self.stack)
        with open(res_file, 'w', encoding=self.encoding) as f:
            f.write(res)

if __name__ == "__main__":
    jf = JsonFormatter(name="json.txt")
    jf.render()

