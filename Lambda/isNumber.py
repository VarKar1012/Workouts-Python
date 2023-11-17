# num = "-23.3454"
# num = "323.34"
# output:
# True
# True

# is_num = lambda q: q.replace('.','',1).isdigit()
# print(is_num(num))

check_num = lambda x: x.replace('.', '', 1).isdigit()
check_neg = lambda x: check_num(x[1:]) if x.startswith('-') else check_num(x)

num = '-23.3454'
print(check_neg(num))
num = '.233454'
print(check_neg(num))
num = '-23'
print(check_neg(num))
num = '-a23.3454'
print(check_neg(num))
num = '23-3454'
print(check_neg(num))
num = '123s'
print(check_neg(num))
