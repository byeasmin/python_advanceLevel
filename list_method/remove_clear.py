basket=[1,2,3,4,5,6,7,8]


#removing value (index remove)

basket.pop()
print(basket)
basket.pop()
print(basket)
basket.pop(0) #index number..
new_basket=basket
print(new_basket)




#removing value (value remove)

basket.remove(3)  #value 3 remove
new_basket=basket
print(new_basket)




#clear value

basket.clear()
new_basket=basket
print(new_basket)





'''
output : 
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6]
[2, 3, 4, 5, 6]
[2, 4, 5, 6]
[]
'''



















