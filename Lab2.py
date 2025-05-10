#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_2 
# Fiz Buzz Project
for num in range(1,9):
   if num % 3==0 and num % 5==0: #check given number is divisible by both 3 & 5 
      print("Fizz Buzzz")
   elif num%3==0:
      print("Fizzz")
   elif num%5==0:
      print("Buzzz")
   else:
      print(num)