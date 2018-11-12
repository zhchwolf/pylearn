import re

# 检查是否有非法字符和括号不成对。
def check_str(s):
    check_flag = True
    if re.findall('[a-zA-Z]',s):
        print('invalid number')
        check_flag = False
    if s.count('(') != s.count(')'):
        print('括号不成对')
        check_flag = False
    return check_flag

# 格式化字符串，消除空格、重复和不必要的符号。
def format_str(s):
    s=s.replace(' ','')
    s=s.replace('+-','-')
    s=s.replace('++','+')
    s=s.replace('--','+')
    s=s.replace('-+','-')
    s=s.replace('*+','*')
    s=s.replace('/+','/')
    return s

# 查找最内层括号的内容，带括号。
def inner_str(s):
    s=re.search('\([^()]+\)',s).group()
    return s

# 乘除运算
def mutl_div(s):
    while re.search('\d+\.?\d*[*/]-?\d+\.?\d*',s):
        str_md = re.search('\d+\.?\d*[*/]-?\d+\.?\d*',s).group()
        print(str_md)
        if '*' in str_md:
            x, y = str_md.split('*')
            res = str(float(x) * float(y))
            s=format_str(s.replace(str_md,res))
        elif '/' in str_md:
            x, y = str_md.split('/')
            res = str(float(x) / float(y))
            s=format_str(s.replace(str_md,res))
    return s
#加减运算
def add_sub(s):
    while re.search('-?\d+\.?\d*[+-]-?\d+\.?\d*',s):
        str_as = re.search('-?\d+\.?\d*[+-]-?\d+\.?\d*',s).group()
        if '+' in str_as:
            x,y=str_as.split('+')
            res=float(x)+float(y)
            s=format_str(s.replace(str_as,str(res)))
        elif '-' in str_as:
            x,y=str_as.split('-')
            res=float(x)-float(y)
            s=format_str(s.replace(str_as,str(res)))
    return s

def my_calc():
    s = input('input any arithmetic:')
    print('You input is:%s' %s)
    if check_str(s):
        print('resource:', s)
        print('eval:', eval(s))
        s = format_str(s)
        while re.search('\(',s):
            sub_s=inner_str(s)
            print(sub_s)
            res_s=mutl_div(sub_s)
            print(res_s)
            res_s=add_sub(res_s)
            print(res_s)
            s= format_str(s.replace(sub_s,res_s[1:-1]))
            print(s)
        else:
            res_s=mutl_div(s)
            res_s=add_sub(res_s)
        print('precise value:',res_s,'\napproximate value:',round(float(res_s),2))

if __name__ == '__main__':
    my_calc()

