#n=4
#fact=1
#i=1
#while i<=n:

    #fact*=i
   # i=i+1


   # print("the factorial is",fact)


#def calfac(n):
 # fact=1
  #for i in range (1,n+1):
     #fact*=i
  #print(fact)

#calfac(7)



def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print (fact(6))



