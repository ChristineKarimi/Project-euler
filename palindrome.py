#Problem:A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.Find the largest palindrome made from the product of two 3-digit numbers.
 
 #Solution: 

def palindrome():
   list_a= range(100,1000)
   list_b= range(100,1000)
   pali=[]
   for i in list_a:
       for x in list_b:
           y = i * x      
           y = str(y)          
if y == y[::-1]:
        pali.append(y)    
               
        return max(pali)print(palindrome())