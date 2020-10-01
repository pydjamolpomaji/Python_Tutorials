import random

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,12))
# print(random.randint(0,1))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
greetings = ['Hello', 'Hi', 'Hey', 'Good Morning', 'Good AfterNoon', 'Good Night']
value = random.choice(greetings)
print(value + ' Python Programmers....!')
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
colours = ['Red', 'Black', 'White']
result = random.choices(colours, weights=[3, 6, 1], k=10)
print(result)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
MyList = list(range(1, 25))
random.shuffle(MyList)
print('Length of the list is', len(MyList), ':', MyList)
hand = random.sample(MyList, k=5)
print(hand)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
FirstName = ['Neelam', 'Akash', 'Santosh', 'Shruti', 'Nikita', 'Pravin', 'Nagesh', 'Mahadev', 'Shrishail', 'Shweta',
             'Sonali', 'Sachin', 'Kiran', 'Rakesh', 'Rohit', 'Rahul', 'Sagar', 'Suraj', 'Shrikant', 'Mahendra']

LastName = ['Agarkhed', 'Sutar', 'Surwase', 'Arya', 'Patil', 'Parveen', 'Kulagi', 'Sharam', 'Birajdar', 'Adawade',
            'Awatade', 'Boinwad', 'Tingre', 'Dhoni', 'Pandya']

StreetName = ['Ameerpet', 'Karnin Nagar', 'Basav Nagar', 'Begampet', 'Himayat Nagar', 'HighTechCity', 'Punjagutta',
              'BalaNagar']

CityName = ['Hyderabad', 'Mumbai', 'Pune', 'Benglore', 'Delhi', 'Solapur', 'Nashik', 'Amaravati', 'Latur', 'Aurangabad',
            'Chennai']

StateName = ['Maharashtra', 'Karnatka', 'Telangana', 'Punjab', 'Uttarakhand', 'Aasam', 'Bihar', 'UttarPradesh',
             'Zarkhand']

for num in range(5):
    First = random.choice(FirstName)
    Last = random.choice(LastName)
    Phone = f'{random.randint(750, 999)}-143-{random.randint(1432, 9999)}'
    StreetNum = random.randint(100, 999)
    Street = random.choice(StreetName)
    City = random.choice(CityName)
    State = random.choice(StateName)
    PinCode = random.randint(143214, 999999)
    Address = f'{StreetNum},{Street},A/P {City},{State},\nPincode - {PinCode}'
    EmailId = First.lower() + Last.lower() + '@gmail.com'
    print(f'{First} {Last}\n{Phone}\n{Address}\n{EmailId}\n')

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
