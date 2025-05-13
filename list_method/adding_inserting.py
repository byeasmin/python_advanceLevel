#adding

basket=[1,2,3,4,5,6,7,8]
new_basket=basket.append(100)
print(basket)
print(new_basket) #output : none

basket.append(20)
new_basket=basket
print(new_basket)




#insert value

basket.insert(4, 1000)
new_basket=basket
print(new_basket)



#extend

basket.extend([100])
new_basket=basket
print(new_basket)








'''
output : 
[1, 2, 3, 4, 5, 6, 7, 8, 100]
None
[1, 2, 3, 4, 5, 6, 7, 8, 100, 20]
[1, 2, 3, 4, 1000, 5, 6, 7, 8, 100, 20]
[1, 2, 3, 4, 1000, 5, 6, 7, 8, 100, 20, 100]
'''