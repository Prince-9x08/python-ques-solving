import math
'''===question.1==='''
# n="prince prajapati"
# print(len(n))
# print(type(n))
'''===question.2==='''
# s="datascience"
# print(s[0] , s[-1])
'''===question.3==='''
# p="pymaster"
# print(p[-3])
'''===question.4==='''
# a="PROGRAMMING"
# print(a[3:7:])
'''===question.5==='''
# i="INDIA"
# print(i[::-1])
'''===question.6==='''
# str_1="i love python programming"
# print("python" in str_1)
'''===question.7==='''
# print("hello" +" "+ "world")
'''===question.8==='''
# print("*"*20)
'''===question.9==='''
# alp="ABCDEFGHI"
# print(alp[::2])
'''===question.10==='''
# py="pymaster india"
# print(py[9:len(py):])

'''================== NEW QUESTIONS =================='''
# s=("pymaster india".upper())
# print(s.title())
'''==q.2=='''
# p=" clean this "
# s=(p.strip(" "))
# print(len(s))
'''==q.3=='''
# string='12345'
# print(string .isdigit())
# string_1="hello123"
# print(string_1.isalpha())
'''==q.4=='''
# str_2='This is bad code with bad habits'
# print(str_2.replace("bad","good"))
'''==q.5=='''
# str_3="one:two:three"
# print(str_3.split(":"))
'''==q.6=='''
# str_4=['Python', 'is', 'fun'] 
# print(' '.join(str_4))
'''==q.7=='''
# p="python"
# print(p.startswith("py") and p.endswith("on"))
'''==q.8=='''
# name="PRINCE"
# print(name.rjust(30))
'''==q.9=='''
# print("7".zfill(4))
'''==q.10=='''
# name="PRINCE"
# marks=80.8
# print(f"my nam is {name} ,\n my marks are {marks}")
'''=====================mid-questions====================='''
# print('PyMaster India'.find("India"))
# print('PyMaster India' .index("India"))
'''==q.2=='''
# print("banana".count("an") , "banana".count("a"))
'''==q.3=='''
# csv='Rajeev,25,Varanasi,Python'
# lst=(csv.split(","))
# print(lst)
'''=====================CHALLENGE-QUESTIONS====================='''
'''==q.1=='''
# r=int(input("enter the radius of circle:"))
# print(f"the area of circle is {3.14*r**2}")
'''==q.2=='''
# c=int(input("enter the temp in celsius:"))
# print(f"the temp in farhenhiet will be {c*9/5+32}")
'''==q.3=='''
# sec=int(input("enter the no. of seconds: "))
# print(f"it wil be {sec//3600} hours"
#      f" {sec%60} minutes")
'''---------------------------------------------------'''
#program to check if number is =ve,-ve or  0 

# x=float(input("enter your number:"))

# if x>0 :
#     print("the number is positive")
# elif x==0 :
#     print("the number is zero")
# else :
#     print("the number is negative")

# print("thanks for using this ! ")

'''==program to find the number is even or odd=='''
# num_1=float(input("enter your number:"))

# if num_1 %2 ==0:
#     print("the number is even")
# else :
#     print("the number is odd")

# print("thanks  for using this program")
'''===program to give grades based on marks==='''
# a=int(input("enter the student's marks:"))

# if a>=90:
#     print("A")
# else:
#     if a>=80:
#         print("B")
#     else:
#         if a>=70:
#             print("C")
#         else:
#             if a>=60:
#                 print("D")
#             else:
#                 if a>=40:
#                     print("f")
    
'''==program to check which num is bigger from the 3 given==='''

# num_1=int(input("give the first num:"))
# num_2=int(input("give the second num:"))
# num_3=int(input("give the third num:"))

# if num_1>num_2:
#     if num_1>num_3:
#         print(f"largest num is {num_1}")
#     else:
#         print(f"largest num is {num_3}")
# else:
#     if num_2>num_3:
#         print(f"largest num is {num_2}")
#     else:
#         print(f"largest num is {num_3}")

# print("thanks for using the programme :)")

'''==a simple ATM check=='''
# y=5000
# x=int(input("enter the amount you want to withdraw :"))

# if x<=y :
#     print(f"withdraw successfull"
#           f" \namount withdrawn={[x]}"
#            f"\nnew balance={[y-x]}")
# else:
#     print(f"your account has insufficient funds"
#           f" \nbalance={[y]}")

'''===traffic light==='''
# light_colour=input("enter the traffic light colour:")

# match light_colour:
#     case "red":
#         print("STOP!")
#     case "yellow":
#         print("BE READY!")
#     case "green":
#         print("YOU CAN GO!")

'''===printing sum of numbers from 1-100=== '''
# total=0

# for i in range(1,101,1):
#     total=total+i
#     print(total)
    
'''==only even numbers from 1 to 20 using continue=='''

# for i in range(1,21,1):
#     if i % 2 !=0:
#         continue
#     else:
#         print(i)

'''==checking if given num is prime=='''

# x=int(input("enter your number:"))

# for i in range(2,x):
#     if x % i == 0:
#         print(f"the number {[x]} is not prime number")
#         break
# else:
#      print(f"the number {[x]} is prime number")    

'''===program to display the factors of "n"==='''

# n=int(input("give the number:"))
# i=1

# while i<=n:
#      if n % i == 0:
#           print(f"{i}")
#      i+=1
    
'''==program to display table of "n" using for loop=='''

# n=int(input("enter the number:"))

# for i in range(1,11,1):
#     print(f"{n} x {i} = {n*i}")

'''==program to display table of "n" using while loop=='''

# n=int(input("enter the number:"))
# i=1

# while i <=10:
#     print(f"{n} x {i} = {n*i}")
#     i+=1

'''==program for star patterns=='''
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print("\n")

'''---printing alphabets as star patterns---'''
# a=("A","B","C","D","E")
# for i in range(1,6):
#     for j in range(i):
#         print(a[j],end=" ")
#     print("\n")
     
# a=['prince',31,True,False,12.5]

# for i in range(len(a)):
#     print(a[i])

# print(a[::-1])

'''====practice problems==='''
# code_list=["python","java","c","c++","js"]
# print(code_list[0])
# print(code_list[-1])

# marks = [45, 67, 89, 23, 90, 56, 78]

# print(marks[0:3])
# print(marks[:3:-1])
# print(marks[::2])
# print(marks[::-1])

# todos = ["wake up", "study"] 

# todos.append("exercise")
# todos.insert(0,"meditate")
# todos.remove("study")
# todos.insert(len(todos),"sleep")
# print(todos)
'''--------------------------'''
# marks_list=[
#     ["prince",80.8],
#     ["ankit",80.4],
#     ["kunal",75.2]
# ]
    
# print(marks_list[1][0])
# print(marks_list[2][1])
'''------------------------'''
data = [101, "Varanasi", 25.3, 82.9]
a,b,c,d=data
print(a,b,c,d)