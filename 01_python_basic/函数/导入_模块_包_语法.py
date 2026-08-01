"""
import 模块
import 模块 as 别名
from 模块 import 东西
from 模块 import 东西 as 别名
from 模块 import *
import 包.模块
from 包 import 模块
"""

# 导入整个模块（别名）
import math
import math as m

# 从模块导入指定函数 / 类 / 变量（别名）
from math import sqrt, pi
from math import sqrt as sq

# 导入模块里的所有内容
from math import *

# 导入子模块/包
import os.path
from os import path
from os.path import exists