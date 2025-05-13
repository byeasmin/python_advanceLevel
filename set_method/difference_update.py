my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}




print(my_set.difference(your_set))
print(my_set)

print(my_set.difference_update(your_set))
print(my_set)









'''
output : 
{1, 2, 3}
{1, 2, 3, 4, 5}
None
{1, 2, 3}
'''

