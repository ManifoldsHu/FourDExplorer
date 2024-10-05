# -*- coding: utf-8 -*- 

import re
import unittest
import sys 
import os 

ROOTPATH = os.path.split(os.path.dirname(__file__))[0]
if not ROOTPATH in sys.path:
    sys.path.append(ROOTPATH)
from bin.HDFManager import reValidHDFName


# 单元测试类
class TestHDF5NameValidation(unittest.TestCase):

    def test_valid_names(self):
        # 有效的名字
        valid_names = [
            'Dataset1',           # 简单英文字母和数字
            '数据集_测试',         # 中文字符和下划线
            'my-dataset+123',      # 连字符和加号
            'Valid Name',          # 中间有空格
            '数据-集+测试',        # 中文加符号
            '合法的Dataset',        # 中英文混合
            'Dataset_123',         # 下划线
            'Dataset-Name',        # 连字符
            'Data Set 1',          # 中间有空格
            'ValidName123_',       # 下划线结尾
            'A_Valid-Name+With123', # 含符号的多语言组合
            'Data123',             # 单一数字组合
            '合法_123',            # 中文和数字
            'Name With Space',     # 中间有空格
            '数据123',              # 中文和数字组合
            'Under_score_Test',     # 下划线组合
            'Valid+Dataset-1',     # 加号与连字符组合
            '测试组_123_valid',      # 中文、数字和字母组合
            '9Mixed_Language_123',  # 混合多种语言
            'Valid-Name_123',      # 连字符和下划线混合
            'a.b.c'                 # 点号组合
            '..validName',        # 连续点号
            'Name..valid',        # 连续点号在中间
            '.+_F3valid)ame1',         # 以点号开头
            '.3LeadingDot',          # 以点号开头
            '~'                     # tilde
            '`~ q'                  # 反引号
        ]

        for name in valid_names:
            with self.subTest(name=name):
                self.assertIsNotNone(reValidHDFName.fullmatch(name), f"Valid name failed: {name}")

    def test_invalid_names(self):
        # 无效的名字
        invalid_names = [
            'Invalid/Name',         # 包含正斜杠
            'Invalid\\Name',        # 包含反斜杠
            'Invalid*Name',         # 包含星号
            'Invalid|Name',         # 包含竖线
            'Invalid"Name',         # 包含双引号
            'Invalid\'Name',        # 包含单引号
            'Invalid:Name',         # 包含冒号
            'Name.',                # 以点号结尾
            ' InvalidName',         # 以空格开头
            'InvalidName ',         # 以空格结尾
            'Invalid<Name',         # 包含小于号
            'Invalid>Name',         # 包含大于号
            'Invalid?Name',         # 包含问号
            'Name\n',               # 包含控制字符 (换行)
            'Name\t',               # 包含控制字符 (制表符)
            'Name\r',               # 包含控制字符 (回车)
            r'Name\n',              # 包含反斜杠和控制字符
            r'Name\t',              # 包含反斜杠和控制字符
            'Invalid/Name*Test',    # 包含多种非法字符组合
            'Invalid\\*?|',         # 全是非法字符
            ' Invalid\tName',       # 以空格和控制字符开头
            'Name_with\nnewline',   # 含换行符
            'Tab\tName',            # 含制表符
            'Colon:Name',           # 含冒号
            'Slash/Name',           # 含正斜杠
            'Backslash\\Name',      # 含反斜杠
            'Name_with*"quote',     # 含星号和引号
            'Invalid Name ',        # 尾部空格
            'TrailingDot..',        # 以点号结尾
            '.'                     # 仅一个点号
            '..',                   # 连续点号
            'valid[Name]',        # 包含方括号
            '[1,2',               # 不匹配的方括号，包含逗号
            ']',                    # 仅方括号
            '[',                    # 左方括号
            ']{',                   # 右方括号和左花括号
            '}[]',                  # 左右方括号组合
            '{}',                   # 空括号
            '{',                    # 左括号
            '[]',                   # 空方括号
            '][',                   # 反方括号
            '[[[]]]]][[[]]',        # 很多方括号
            '}',                    # 右括号
            '{validName}',          # 包含花括号
            'Name{valid}',          # 花括号在结尾
            'invalid{Name}123',     # 花括号和数字组合
            '数据{集}测试',          # 中文和花括号组合
            'Invalid{Name} With Space',# 花括号和空格组合
            'Invalid{Name}..valid', # 花括号和连续点号组合
        ]
        
        for name in invalid_names:
            with self.subTest(name = name):
                self.assertIsNone(reValidHDFName.fullmatch(name), f"Invalid name passed: {name}")
        name = 'Name\n'
        print(repr(name))


# 运行测试
if __name__ == '__main__':
    unittest.main()