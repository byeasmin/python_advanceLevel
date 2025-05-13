basket = [1, 11, 32, 67, 8, 9, 90, 34]
print(basket.sort()) #output will be none

basket.sort() #method
print(basket)


basket1 = [10, 43, 67, 54, 12, 8]
print(sorted(basket1)) # output will be [8, 10, 12, 43, 54, 67], cz this is function
print(basket1)

new_basket1=basket1[:]
new_basket1.sort() #method
print(new_basket1)



# copy array/list

basket2 = [89,56,47,3,32,1,5]
new_basket2 = basket2.copy()
print(new_basket2)





'''
output :
None
[1, 8, 9, 11, 32, 34, 67, 90]
[8, 10, 12, 43, 54, 67]
[10, 43, 67, 54, 12, 8]
[8, 10, 12, 43, 54, 67]
[89, 56, 47, 3, 32, 1, 5]
'''