import pygame

'''
从文本文件生成一个文本元素
'''


class TextComponent:

    def __init__(self, textPath):
        # 读入对应的文本文件
        with open(textPath, 'r') as tf:
            self.textList = tf.readlines()
        # 设置文本元素的最大显示列数和最大显示行数，初始化默认为None，即不做限制，生成的Surface也就不限长宽
        self.maxColBF = None
        self.maxRowBF = None
        # 设置文本元素的最大行字数，默认无限制，也就是不进一步切分文本
        self.colLimit = None
        # 设置文本元素的字体，字号，字色，字型，None就是跟随界面的全局设定
        self.fontType = None  # 字体
        self.fontSize = None  # 字号
        self.fontColr = None  # 字色
        self.fontStyl = {'Italic': None, 'Bold': None, 'Underline': None}  # 字型
        # 设置滚动速度，也就是当限制最大显示列数和行数时，如果进行两方向的滚动，每次滚动几个字符的距离。
        self.scrllSpd = {'x': 1, 'y': 1}
        # 设置文本元素的页边距 [Top, Left]，None就是跟随界面的全局设定
        self.marginPx = {'top': None, 'left': None}
        # 设置文本元素的行距，None就是跟随界面的全局设定
        self.lineDist = None

    def divide(self):
        if self.colLimit:
            newTextList = []
            for paragraph in self.textList:
                leftedContent = paragraph
                while len(leftedContent) > self.colLimit:
                    newTextList.append(leftedContent[0:self.colLimit])
                    leftedContent = leftedContent[self.colLimit:]
                newTextList.append(leftedContent)
            self.textList = newTextList
        else:
            print('警告：没有设置最大行字数，所以没有进行段落文本划分。')

    def 




