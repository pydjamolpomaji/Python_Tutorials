# Program 1 :-
# Python Code to Convert List of Tuple into Dictionary Using Function.
def Convert(Tuple, Dictionary):
    for Name, RollNo in Tuple:
        Dictionary.setdefault(Name, []).append(RollNo)
    return Dictionary


List_of_Tuple = [("Akash", 101), ("Gaurav", 102), ("Anand", 103),
                 ("Divya", 104), ("Neha", 105), ("Nikita", 106), ("Neelam", 107)]

Dictionary = {}
print('Dictionary is :', Convert(List_of_Tuple, Dictionary))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Python Code to convert List of Tuples into Dictionary Using for loop.
List_of_Tuple = [("Akash", 101), ("Gaurav", 102), ("Anand", 103),
                 ("Divya", 104), ("Neha", 105), ("Nikita", 106), ("Neelam", 107)]
Dictionary = dict()

for Name, RollNo in List_of_Tuple:
    Dictionary.setdefault(Name, []).append(RollNo)
print('Dictionary is :', Dictionary)


# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 3 :-
# Python Code to convert List of Tuples into Dictionary
def listtodict(List, Dictionary):
    di = dict(List)
    return di


List = [("Akash", 101), ("Gaurav", 102), ("Anand", 103),
        ("Divya", 104), ("Neha", 105), ("Nikita", 106), ("Neelam", 107)]
Dictionary = {}
print("Dictionary is :", listtodict(List, Dictionary))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
