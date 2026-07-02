# first_name="anmol"
# last_name="mishra"
# full_name=f" {first_name} {last_name}"
# print(full_name.title())
# print("\tpython")
# print("languages:\npython \nc \nc+")
# print(2+3*4)
#using _to seperate digit

# universe_age=14_000_000

#multi assignment

# x,y,z=2,3,4
# # print(x+y+z)
#using constant
# FAV_NUM=200
# print(f"My fav name is {FAV_NUM} ")
# bicycles=['anmol','mishra','bikky']
# # for bicycle in bicycles:
# #     print(bicycle.title())
# # # print(bicycles[0].title())\
# # bicycles[0]='roma'
# # print(bicycles[0])
# # python=' anmol '
# # print(python)\
# bicycles.append('aftaab')
# # print(bicycles)
# gods=[]
# gods.append('shiva')
# gods.append('vishnu')
# gods.append('bhrama')
# print(gods)
# programmings=['c','python','java']
# programmings.insert(1,'R')

# del programmings[0]
# print(programmings)
# motorcycles=['apache','pulsar','yamaha']
# poped_motor=motorcycles.pop()
# # print(motorcycles)
# # print(poped_motor)
# # motorcycles.remove("pulsar")
# # print(motorcycles)
# cars=['bmw','audi','gvagon','defender']
# # # cars.sort(reverse=False)
# # cars_1=sorted(cars,reverse=True)
# # print(len(cars_1))
# # print(cars)
# print(cars[4])
# for num in range(5):
#     print(num)
# numbers=list(range(1,6,2))
# print(numbers)
# even=list(range(2,11,2))
# print(even)
# squares = []
# for value in range(1,11):
#     square=value**2
#     squares.append(square)
# print(squares)
# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# squares=[x**2 for x in range(1,11)]
# print(squares)
# even_num=[x+2 for x in range(1,11) if x%2==0]
# print(even_num)
#slicing llist
# friends=['anmol','aftab','rajmudin','roma']
# # print(friends[0:2])
# # print(friends[:])
# print(friends[-1:])
# print(friends[:-1])
#prsint 1 to 20
# for num in range(1,21):
#      print(num,end="")
# million=[x for x in range(1,1000001)]
# print(min(million))
# print(max(million))
# print(sum(million))
# for odd in range(1,21,2):
#     print(odd)
#     # print("\t")
# multiples_3=[x*3 for x in range(1,11)]
# print(multiples_3)
# cubes=[x**3 for x in range(1,11)]
# print(cubes)
# bubu_fav_foood=['manchurian','pizza','momo','popcorn']
# print(bubu_fav_foood[0:4:2])
# players=['virat','sachiin','rohit','hardik','abd']
# # print(players)
# for player in players[1:3]:
#     print(player.title())
# my_foods=['chowmin','burger','carrot','cucumber']
# # friend_food=my_foods[:]
# # print(friend_food)
# # friend_food=my_foods
# # my_foods.append("mushroom")
# # friend_food.append("momo")
# # print(my_foods)
# # print('\n')
# # print(friend_food)
# for food in my_foods[:3]:
#     print(f'The first three item are:{food}')
# my_pizzas=['cheese','chicken','veg','mutton']
# friend_pizzas=my_pizzas[:]
# my_pizzas.append("mushroom")
# friend_pizzas.append("garlic")
# print("my pizza are:")
# for pizza in my_pizzas:
#     print(pizza)
# print("my friend pizza are:")
# for pizza in friend_pizzas:
#     print(pizza)
# amol=['abc','abc','fgh']
# print(amol)


#using tuples
# dimensions=(200,50)
# # print(dimensions[1])
# dimensions[0]=100
# friend=(2,)
# print(type(friend))

# dimensions=(2,3,4,5)
# for dimension in dimensions:
#     print(dimension)
# dimension=(200,30)
# print(dimension)
# dimension=(300,40)
# print(dimension)

#next chapter
#if statement
# cars=['audi','bmw','toyota','lamborgini','rollsroyal']
# for car in cars:
#     if car=='bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# my_tup=(2,)
# print(type(my_tup))
# num=19
# if num!=29:
#     print("ur answer is incorrect")

# check for driving license
# age = 12
# age_1=18-age
# if age >= 18 and age <=60:
#     print("you are elglible for driving a car")
# else:
#     print(f"try after {age_1} years")

#checking for list
# pizzas=['macroni','cheese','veg','nonveg']
# if 'macroni' in pizzas:
#     print('i got ur order')
# else:
#     print("you didn't get ur oder")

# banned_list=['anmol','puskar','shivam','rajmudin','aftab']
# if 'puskar' not in banned_list:
#     print('you can post in this page')
# else:
#     print('you cannot post ')

# car='audi'
# if car == 'subaru':
#     print(f'The car is subaru')
# else:
#     print("false")

# check for equaliltiy and inequality
# name='anmol'
# if name.lower() == 'anmol':
#     print("username is already in the list")

# names=['anmol','roma','puskar','shivam']
# if 'romma' in names:
#     print("you are member of our team")
# else:
#     print("your package is expired")


# friends=['roma','aftab','dhoriya','bibham']
# if 'roma' not in friends:
#     print("you are safe")
# else:
#     print('you are not in safe')

# admission fees
# age=4
# if age == 4:
#    charge=0
# elif age > 4 and age < 18:
#    charge=25
# else:
#    charge=40
# print(f'The charge for admission is {charge}')

#exercise
#5-3

# alien_color='green'
# if alien_color == 'green':
#    print('you earned 5 points')

# fav_fruits=['banana','apple','carot']
# if 'banana' in fav_fruits:
#     print('i really like banana')

# pizzas=['mushroom','extra cheese','green peppers']
# for pizza in pizzas:
#     if pizza == 'green peppers':
#         print(f'sorry,we are out of stock')
#     else:
# #         print(f'The {pizza} stuffing is added')
# requested_toppings=[]
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'adding {requested_topping}')
# else:
#     print('are you sure you want a plain pizzas?'
# available_toppings=['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
# request_toppings=['mushroom','french fries','extra cheese']
# for request_topping in request_toppings:
#     if request_topping in available_toppings:
#         print(f"adding {request_topping}")
#     else:
#         print(f'sorry we don"t have {request_topping}')
# print("finished")

# exercise
# usernames=['admin','anmol','puskar','roma','aftab']
# for username in usernames:
#     if username=='admin':
#         print(f'Hello,{username} .would you like to see report?')
#     else:
#         print(f'Hello {username}, Thank you for loggin in')

# usernames=['anmol','puskar']
# if usernames:
#     for username in usernames[:]:
#         delt_user=usernames.pop()
#         print(f'{delt_user},you are removed from list')
# else:
#     print('sorry we need to find some users!')

# current_users=['anmol','puskar','aftab','bikky','roma','ashish']
# new_users=['rajmudin','bibham','anmol','roma','sahil']
# for name in new_users:
#     if name.lower() in current_users:
#         print(f"hello {name} ,plz give another name,it is already available")

# ordinal number
# natural_num=[x for x in range(1,10)]
# print(natural_num)

# using dictionary
# alien_0={
#     'color':'green',
#     'height': 5,
#     'points': 10
# }
# print((alien_0['color']))
# new_points=alien_0['points']
# print(f'hey you got {new_points}')
# alien_0['x_position']=25
# alien_0['y_position']=0
# print(alien_0)
# alien_0={}
# alien_0['color']='green'
# alien_0['points']=5
# print(alien_0)
# my_t=('anmol',)
# print(type(my_t))

# alien_0={'color':'green'}
# print(f"The color you get is {alien_0['color']}")

# alien_0={'x_position':0,'y_position':25,'speed':'medium'}
# #move alien to the right
# if alien_0['speed'] == 'slow':
#     x_increment=1
# elif alien_0['speed'] == 'medium':
#     x_increment=2
# else:
#     #this must be a fast moving alien
#     x_increment=3
# #the new position is the old postion plus the incremnet
# alien_0['x_position']=alien_0['x_position']+x_increment
# print(f"New position:{alien_0['x_position']}")

#remove key-value pair
# alien_0={'color':'green','points':5}
# del alien_0['color']
# print(alien_0)

# fav_lang={
#     'jen':'python',
#     'saraha':'c',
#     'edward':'rust',
#     'phil':'python'
# }
# print(fav_lang.get('jenn'))

# person = {
#     'first_name':'anmol',
#     'last_name':'mishra',
#     'age':21,
#     'city':'janakpurdham'
# }
# print(person['first_name'])
# print(person['age'])
# print(person['city'])

# user_0 = {
#     'username' : 'anmol',
#     'last_name' :'mishra',

# }
# for key , value in user_0.items():
#     print(f"\n key : {key}")
#     print(f"value : {value}")

# fav_lang={
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phill' : 'python',
#     }
# for name in fav_lang.keys():

# fav_lang={
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phill' : 'python',
#     }
# for programming in fav_lang.keys():
#     print(programming.title())

# fav_lang={
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phill' : 'python',
#     }
# for programming in fav_lang:
#     print(programming.title())

# fav_lang={
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'jen' : 'python',
#     }
# for name in set(fav_lang.values()):
#     print(name.title())

# fav_lang={'python','c','python'}
# print(fav_lang)
# rivers={
#     'ganga' : 'india',
#     'nile' : 'egypt',
#     'koshi' : 'nepal',
# }
# for river , country in rivers.items():
#     print(f'The {river.title()} runs through {country.title()}')

# fav_lang= {
#     'anmol' : 'c',
#     'bikky': 'python',
#     'aftab' : 'java',
#     'roma' : 'c+'
#     }
# fav_language_lst=['ashish','shiva','anmol','roma','shambhu']
# for name in fav_language_lst:
#     if name in fav_lang.keys():
#         print(f'Thank {name},for your poll')
#     else:
#         print('you are invited for the poll')


# alien_0={'color' : 'green','points' : 5}
# alien_1={'color' : 'yellow','points' : 10}
# alien_2={'color' : 'red','points' : 15}

# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

# aliens=[]

# for num in range(30):
#     new_alien={'color' : 'green', 'points' : 5,'speed' : 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)

# print(len(aliens))

# Make 30 green aliens.
# aliens = []
# for alien_number in range (30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# fav_lan={
#     'jen' : ['python','rust'],
#     'sarah' : ['c'],
#     'edward' : ['rust', 'gos'],
#     'phill' : ['python','haskell']

# }
# for name, languages in fav_lan.items():
#     print(f"\n {name.title()}'s favorite lanaguage are:")
#     for language in languages:
#         print(f"\t{language.title()}")
# users={
#     'mr.anmol' : {
#         'first' : 'anmol',
#         'last' : 'mishra',
#         'location' : 'jnk',
#     }, 
#     'ms.roma':{
#         'first' : 'roma',
#         'last' : 'mishra',
#         'location' : 'aus'
#     },

# }
# for username,user_info in users.items():
#     print(f'\n username : {username}')
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")
# name=input('please enter ur name:')
# print('your name is :',name)
# age=int(input('enter ur age'))
# if age >= 18:
#     print('you can vote')

#multiply
# num=int(input('enter a num'))
# if num % 10 == 0:
#     print('it is multiple of 10')

#print 10 num
# num=1
# while num <= 10:
#     print(num)
#     num+=1

# prompt="\n tell me something i will repeat it back to you"
# prompt+="enter 'quit to end"
# message= ""
# while message != 'quit':
#     message=input(prompt)
#     print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# current_num = 0
# while current_num < 10:
#     current_num+=1
#     if current_num %2==0:
#         continue
#     print(current_num)
# prompt='\nenter what u want to add in pizza'
# prompt+='\nenter quit to stop\t'
# message=''
# while message != 'quit':
#     message=input(prompt)
#     print(f"your toppings is added:{message}")

# age=int(input('enter ur age:'))

#confirmed user.py
# unconfirmed_users=['anmol','roma','puskar','aftab']
# confirmed_users=[]
# while unconfirmed_users:
#     current_user=unconfirmed_users.pop()
#     print(f"verifying user:{current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

#using responses
# responses={}
# #set a flag to indicate that polling is active.
# polling_active=True
# while polling_active:
#     name=input('\n what is your name?')
#     response=input('which mountain would you like to climb someday?')
# #store the response
#     responses[name]=response
#     #find out if anyone else is going to take the poll.
#     repeat=input('would you like to let another person respond?(yes/no)')
#     if repeat == 'no':
#         polling_active=False

# #polling is complete.show the results.
# print("\n--------poll Results------")
# for name,response in responses.items():
#     print(f"{name} would like to climb {response}.")

#test yourself
# sandwich_orders=['cheese','yogort','chicken','veg']
# finished_sandwiches=[]
# while sandwich_orders:
#    current=sandwich_orders.pop()
#    print(f"I made your {current} sandwich")
#    finished_sandwiches.append(current)
# print("-----finished-----")

# sandwich_orders=['pastrami','veg','chicken','pastrami','cheese','yogourt']
# print('heyh,we are run out of "pastrami"')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print("finised sandwitch:",sandwich_orders)
