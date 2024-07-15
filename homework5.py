immutable_var = (5, 'word', 0.5, True)
print(immutable_var)
# immutable_var[0] = 4 это неизменяемый тип данных в Python

mutable_list = [23, 'string', '2word', False]
mutable_list.append(90)
mutable_list[0] = 33
print(mutable_list)