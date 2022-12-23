n = int(input())
dict_num = {}
for i in range(1,n+1):
    dict_num[i] = round((1+1/i)**i,2)
print(dict_num)
print(sum(dict_num.values()))
