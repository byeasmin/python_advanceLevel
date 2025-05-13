# set is an unordered collection of unique objects..

my_set = {1,2,3,4,5,6,6,6,6,6}

my_set.add(100)
my_set.add(2)

print(my_set)  # their is no duplicate, everything has to be unique..


my_list=[1,2,3,4,5,5,5]
print(my_list)
print(set(my_list))
# print(my_set[0]) #error occurs, bcz set deos not support indexing.



print(1 in my_set)
print(len(my_set))
print(list(my_set))



new_set=my_set.copy()
print(new_set)
my_set.clear()
print(my_set)









'''
output : 
{1, 2, 3, 4, 5, 6, 100}
[1, 2, 3, 4, 5, 5, 5]
{1, 2, 3, 4, 5}
True
7
[1, 2, 3, 4, 5, 6, 100]
{1, 2, 3, 4, 5, 6, 100}
set()

'''













