def sum(num1, num2):
    def another_func(num1, num2):
        return num1+num2
    return another_func

total=sum(10,2)
print(total)





'''
Output : 
<function sum.<locals>.another_func at 0x000001C110EB58A0>
'''
