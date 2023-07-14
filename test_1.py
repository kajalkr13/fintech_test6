num = int(input("Enter a number: "))    
A = 1    
if num > 0: 
    for i in range(1,num + 1):    
        A = A*i    
    print("The factorial of",num,"is",A)    
else:  
     print(" Factorial does not exist for this numbers")  
