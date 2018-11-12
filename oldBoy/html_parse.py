import re_module
from pyquery import PyQuery as pq

with open(r'E:\pycharm_data\data_folder\test.html') as f:
    ftxt = ''
    d={}
    for i in f:
        i=i.replace("\r\n",'')

        try:
            res = pq(i)
            ps = res('TD').eq(0)
            # print(ps)
            ps1 = ps('TD').find('input').attr('name')
            if ps1:
                print(ps1)
            else:
                ps1 = ps('TD').find('input').eq(1).attr('name')
                print(ps1)

            ps2 = res('TD').eq(1).text()
            if ps2:
                print(ps2)
            else:
                ps2= res('TD').text()

            d[ps1] = ps2
        except:
            pass
# print(d)
d.pop(None)
for k,v in d.items():
    print(k,v)


# res = res('td').text()
# res1 = res('TD').find('input').eq(0).attr('name')
# res2 = res('TD').text()
# res3 = res('TD').eq(1).text()
# print(res)

# se= re.search(r'\<TD*type="CHECKBOX" name="([A-Z_]+)"*\>',s)
# print(se)
#
# i='<td nowrap="nowrap"><img src="images/title_arrow.gif"/><input type="checkbox" style="visibility:hidden"/>Repository URL:<input value="" size="20" maxlength="100" type="TEXT" name="WORKGROUP_OPTION_ANNOTATIONS_REPOSITORY" id="WORKGROUP_OPTION_ANNOTATIONS_REPOSITORY"/></td>'
# res = pq(i)
# ps1 = res('TD').eq(0)
# print(ps1)
# ps1 = ps1('input').eq(1).attr('name')
# print(ps1)
# # if ps1:
# #     print(ps1)
# # else:
# #     # ps1 = ps1('input').eq(1).attr('name')
# #     print(234)
#
