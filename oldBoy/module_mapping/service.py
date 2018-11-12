# from src import commons
#
# # func_name = 'add'
# # func_name = 'delete'
# func_name = 'modify'
#
# func = getattr(commons,func_name)
# func()

module = 'src.commons'
func_name = 'modify'

import  importlib

m = importlib.import_module(module)
print(m)
func=getattr(m,func_name)
func()

