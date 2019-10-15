# dic = {(1,2,3):的数据类型都可以做字典的键值'haha'}
# # print(dic)      #不可变
# dic = {'上帝':'耶和华','神':'巨人'}
# dic['矮子']='小芳'
# print(dic)
# dic.setdefault('百姓','人民')#字典里面已经有的键值，不会添加。如果不在的话，会进行添加。
# print(dic)
# 字典是没有remove方法的
# pop
# del
# clear


# dic.pop('百姓')
# print(dic)
# str = '    你是.个鬼'
# print(str.strip())
# print(str.split('.'))

# del dic['神']
# print(dic)
# dic.clear()
# print(dic)

# ret=dic.popitem()#随机删除
# print(dic)
# print(ret)
# dic = {'上帝':'耶和华','神':'巨人'}
# dic['神']='夸父'
# # print(dic)
# dic1 = {'造人':'女娲','神':'伏羲'}
# dic.update(dic1)#把两个字典合并，更新
# print(dic)

# 查
# for i in dic:
#     print(i,dic[i])

# print(dic['造人'])#查不到，会报错
# print(dic.get('师傅','没有'))#查不到就显示指定内容，
# print(dic.setdefault('神'))  #setdefault(）也可以查找，同时也可以添加。没有的话返回None
# for i in dic.keys():
#     print(i)
# for j in dic.values():
#     print(j)#获取到字典的值

# print(dic.items())
# for i in dic.items():
#     print(i)

# 解构
# a,b = (1,2) #按位置赋值给变量
# c,d = [3,4]
# print(a,b)
# print(c,d)
# e,f = '江山'
# print(e,f)

# s = 'k:1|k1:2|k2:3|k3:4'
# new_li = s.split('|')
# print(new_li)
# dic = {}
# for i in new_li:
#     key,value=i.split(':')
#     dic[key]=value
# print(dic)

# dic =  {'k':[],'k1':[]}
# li = [11,22,33,44,55,66,77,88,99]
# for i in li:
#     if i==66:
#         continue
#     elif i>66:
#         dic.setdefault('k').append(i)
#     else:
#         dic.setdefault('k1').append(i)#注意setdefault()的用法
# print(dic)

goods = [{"name":"电脑","price":1999},
         {"name":"鼠标","price":10},
         {"name":"游艇","price":20},
         {"name":"美女","price":998}]
for i in goods:
    print(goods.index(i)+1,i["name"],i["price"])
while 1:
    str_input = input('请输入商品序号，输入Q/q退出！')
    if str_input.isdigit() and 0<int(str_input)<=len(goods):
        print(goods[int(str_input)-1]['name'],goods[int(str_input)-1]['price'])
    else:
        break