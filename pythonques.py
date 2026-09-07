'''===program to find smallest num in list==='''

# nums = [34, 12, 78, 5, 60]

# for i in nums:
#     smallest=i
#     for j in  nums:
#         if j<=smallest:
#             smallest=j
# print(f"the smallest num in list is: {smallest}")

'''====finding prime no. in rnage of 1 to 50==='''
# prime=[]

# for i in range (2,51):
#     for j in range (2,i):
#         if i%j==0:
#             break
#     else:
#         prime.append(i)
# print(f"the prime nums are {prime}")

# print(f"the total no. of primes are {len(prime)}")

'''===Remove Duplicates (keep unique only)==='''

# items = [1, 2, 2, 3, 4, 4, 4, 5]

# no_dup=[]

# for ele in items:
#     if ele not in no_dup:
#         no_dup.append(ele)
# print(no_dup)

'''===Second Largest Number==='''

# nums = [23, 67, 12, 89, 45, 74] 

# largest=(nums[0])
# second_largest=(nums[0])
# for ele in nums:
#     if ele > largest:
#         second_largest=largest
#         largest=ele
#     elif ele > second_largest:
#         second_largest=ele
# print(f"the second largest term is:{second_largest}")
    
'''===Most Frequent Number==='''
# items = [3, 1, 3, 2, 3, 1, 2, 3] 

# most_frq=0
# occurence=0

# for i in items:
#     count=0
#     for j in items:
#         if i==j:
#             count+=1
#         if count>occurence:
#             most_frq=i
#             occurence=count
# print(f"most occuring term is:{most_frq}\n"
#       f"no. of occurence:{occurence}")
