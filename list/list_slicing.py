#list slicing..
#list[start:stop:step]


amazon_cart=[
    'sunglasses',
    'notebooks',
    'toys',
    'graps'
]

print(amazon_cart)
print(amazon_cart[1:3])
print(amazon_cart[0::2])  # This is slicing from index 0 to the end, but with a step of 2 (i.e., skip every second item).


amazon_cart1 = ['sunglasses', 'notebooks', 'toys', 'graps', 'watch', 'bottle', 'shoes']
print(amazon_cart1[0::3])


#print(amazon_cart[0])
#print(amazon_cart[1])

#list are mutable...

amazon_cart1[0]='laptop'
print(amazon_cart1)
new_cart=amazon_cart[0:3]
new_cart[0]='gum'
print(new_cart)




new_cart1=amazon_cart1[:]
print(new_cart1)






'''
output : 
['sunglasses', 'notebooks', 'toys', 'graps']
['notebooks', 'toys']
['sunglasses', 'toys']
['sunglasses', 'graps', 'shoes']
['laptop', 'notebooks', 'toys', 'graps', 'watch', 'bottle', 'shoes']
['gum', 'notebooks', 'toys']
['laptop', 'notebooks', 'toys', 'graps', 'watch', 'bottle', 'shoes']

'''







