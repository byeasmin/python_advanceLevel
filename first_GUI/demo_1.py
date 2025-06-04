# Exercise

picture =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


# 1 iterate over picture..

# plan-1: if 0 -> print ' '
# plan-2: if 1 -> print "*"

#let's start...

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print(' * ',end='')
        else:
            print('   ',end='')
    print(end='\n')


print(end='\n')
print("another....")
print(end='\n')


for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*',end='')
        else:
            print(' ',end='')
    print(end='\n')







'''
Output : 
          *          
       *  *  *       
    *  *  *  *  *    
 *  *  *  *  *  *  * 
          *          
          *          

another....

   *   
  ***  
 ***** 
*******
   *   
   *   

'''