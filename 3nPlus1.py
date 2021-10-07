def collatz(numb):
    if numb%2==0:
        return numb/2
    elif numb%2==1:
        return 3*numb+1
    else:
        print ("error")
        
numb=int(input("eneter the starting number:"))
print ("COLLATZ SEQ")
print(numb)
while (numb !=1):
    numb=collatz(numb)
    print(numb)
    
    
    
    


      
        
        
    
	
