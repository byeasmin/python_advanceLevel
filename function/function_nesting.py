def sum(num1, num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func(num1, num2)

total=sum(10,2)
print(total)






'''
Output :
12
'''