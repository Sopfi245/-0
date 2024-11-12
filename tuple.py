# module_1_5.py
immutable_var = 1,2,'juice',True
print(immutable_var)
try:immutable_var[1] = 'water'
except TypeError as f:
 print('Ошибка :',f)

mutable_list = [1,2,3,4,5,]
print('Было :',mutable_list)
mutable_list[2]=45
print('Стало :',mutable_list)