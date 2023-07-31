#python program to check leap year

#take input from user
n = int(input("Enter the year : "))

year = n % 4

if year == 0:
   print ("n is leap year")

else:
   print ("n is not leap year")
