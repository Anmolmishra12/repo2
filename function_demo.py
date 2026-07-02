# def greet_user(username): #function def  #here username is parameter
#     """Display a simple greetings.""" #doc string
#     print(f"Hello,{username.title()}")#function body
# greet_user('aftav')#this name aftab is argument

# def describe_pet(animal_type,pet_name):
#     """display information about a pet"""
#     print(f"\n I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet('jarsigai','cow')
# describe_pet('hamster','harry')

# def display_message():
#     """Display about exercise"""
#     print("Hello eveyone,i am learning python")

# display_message()
# 
# def fav_book(title):
#     """Display about fav book"""
#     print(f"One of my favorite books is {title}")
# fav_book('Atomic habbit')
# def fav_book(name,author):
#     """display information about fav book"""
#     print(f"{name} is my fav book by {author}")

# fav_book(author='james clear',name='atomic habbit')


# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('willie','cat')

"""while writing a default value
 ,we should write first without default value
   parameter at last default value"""

# def make_tshirt(size,text):
#     """display size and text printed on tshirt"""
#     print(f"The size of shirt is {size}")
#     print(f"\n {text} is written on it.")
# make_tshirt(size='30',text='jay madesh')


# def make_tshirt(size='large',text='I love Python.'):
#     """display size and text printed on tshirt"""
#     print(f"{size} size shirt has {text} printed on it")  

# make_tshirt()

# def describe_city(city,country='Nepal'):
#     """dispaly country and city"""
#     print(f"{city} is in {country}")
# describe_city('janakpur')

# describe_city('kathmandu')

# describe_city('pokhara')

# describe_city('Delhi','India')

#return values

# def get_formatted_name(first_name, last_name):
#     """Return  a full name,neatly formaatted"""
#     full_name = f"{first_name}  {last_name} "
#     return full_name.title()

# personal=get_formatted_name('anmol','mishra')
# print(personal)

# def get_formatted_name(first_name, last_name, middle_name=None):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#        full_name = f"{first_name} {middle_name} {last_name}"
       
#     else:
#       full_name=f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('anmol','mishra','kumar')
# print(musician)


# musician = get_formatted_name('bishal','ydav')
# print(musician)

# def build_person(first_name, last_name):
#     """Return a dic of information about a person"""
#     person= {'first' : first_name, 'last' : last_name}
#     return person
# musician = build_person('anmol','mishra')
# print((musician))

# def build_person(first_name, last_name, age=None):
#     """return a dic of information about a person."""
#     person={'first' :first_name , 'last': last_name}
#     if age:
#         person['age']= age
#     return person
# musician= build_person('anmol','mishra')
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """Return a full name,nealty formatted"""
#     full_name= f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("add more name ")
#     print('press q to quit')
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     if f_name == 'q' and l_name == 'q':
#         break
#     else:
#         formatted_name = get_formatted_name(f_name, l_name)
#         print(f"\nHello, {formatted_name}!")

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# def make_album(artist_name,album_title,n_s=None):
#     """Describing a music album"""
#     album={'Name' : artist_name, 'title': album_title}
#     if n_s :
#        album['number_of_song']=n_s
#     return album

# alb=make_album('arjit singh', 'tera soroor',25)
# print(alb)


# def make_album(artist_name,album_title,n_s=None):
#     """Describing a music album"""
#     album={'Name' : artist_name, 'title': album_title}
#     if n_s :
#        album['number_of_song']=n_s
#     return album
# while True:
#     print('plz,enter the details: ')
#     print('(press "q" to quit)')
#     art_name=input("Enter artist name: ")
#     if art_name.lower() == 'q':
#         break
#     alb_title=input("Enter artist album: ")
#     if alb_title.lower() == 'q':
#         break

#     alb=make_album(art_name,alb_title)
#     print(alb)

#passing a list

# def greet_users(names):
#     """print a simple greeting to each user in the list"""
#     for name in names:
#         msg= f"Hello, {name.title()}!"
#         print(msg)
# usernames=['anmol','aftab','rajmudinn','']
# greet_users(usernames)

# unprinted_design = ['phone case', 'robot pendant', 'motorcycle']
# completed_models = []

# while unprinted_design:
#     current_design=unprinted_design.pop()
#     print(f"printing model: {current_design}")
#     completed_models.append(current_design)

# print("\n The following models have bee printed.")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     simulate printing each design,until  none are left.
#     move each design to completed_models after printing    
#     """
#     while unprinted_designs:
#         current_design= unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """show all the models have been printed"""
#     print("\n The following models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# def show_messages(msgs):
#     """show each text msg"""
#     for msg in msgs:
#         print(msg)
# msgs=['hello','romu','babby','bacha']
# show_messages(msgs)



# def send_messages(messages,sent_messages):
#     print('\n-------sending message------')
#     while messages:
#         current_message = messages.pop(0)
        
#         print(f"Sending: {current_message}")
        
#         # Add it to the sent_messages list
#         sent_messages.append(current_message)     


# def profile(first,last,**userinfo):
#     """use of **kwargs to collect non specify keywords"""
#     userinfo['first_name']=first
#     userinfo['last_name'] = last
#     return userinfo
# user_profile=profile('anmol','mishra',location='jnk',age=25)
# print(user_profile)


# def make_pizzas(*toppings):
#     """summarize the pizza we are about to make"""
#     print("\nMaking a pizzza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizzas('mushroom')

# make_pizzas('mushroom','cheese','burger','rum')


# def make_sandwiches(*items):
#     """summarize the sandwich we are about to make:"""
#     print("\nMaing a sandwitch with following items: ")
#     for item in items:
#         print(f"- {item}")
# make_sandwiches('mushroom')
# make_sandwiches('mushroom','veg','chhese','anmol')
# def build_profile(first,last,**user_info):
#     """ Build a profile of yourself by calling build_profile()"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# profile=build_profile('anmol','mishra',location='jnk',age=23)
# print(profile)