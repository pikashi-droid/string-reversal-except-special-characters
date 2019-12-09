#to reverse a string without affecting special characters
a=input("eter your string to be reversed: ")
b=len(a)
def isalpha(x):
    return(x.isalpha())

def swap(a,b):
    return (b,a)

def tostring(a):
    string=''.join(a)
    return(string)

def reverse(s):
    l=list(s)
    p1=int(len(s)-1)
    p2=0
    
    if not (isalpha(l[p1])):
        p1-=1
        
    if not (isalpha(l[p2])):
        p2+=1
        
    else:
        l[p1],l[p2]=swap(l[p1],l[p2])
        p1-=1
        p2+=1
    
            
        
    return (tostring(l))

result=reverse(a)
print(result)