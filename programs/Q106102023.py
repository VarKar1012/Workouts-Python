my_list = ['tool', 23, 3.4, 'bar', 55, 'toolbar']
out = list(filter(lambda x: type(x) == str, my_list))
out = list(filter(lambda x: isinstance(x, str), my_list))
# out = [i for i in my_list if type(i) == str]
print(out)