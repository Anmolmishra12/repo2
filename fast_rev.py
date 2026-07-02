# cars=['ducati','bmw','lambergini','nano']
# # print("before modifying:",cars)
# # cars[0]='defender'
# # print("\n after modifying:",cars)
# # cars.sort(reverse=True)
# cars.reverse()
# print(cars)

# even=list(range(2,20,2))
# print(even)

# list comprehension
# square=[x**2 for x in range(1,11)]
# print(square)

# multiple_2=[x for x in range(2,22) if x%2==0]
# print(multiple_2)

# slicing the list
friends=['aftab','anmol','ashish','bikky','rajmudin','roma']
# for friend in friends[-3:]:
#     print(f"hey {friend.title()}")
friends1=friends[:]
friends1.append('shiva')
friends.append('gauri')
print(friends1)
print(friends)