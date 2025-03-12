#greets user for explanation 

statesalestax = {
    "Alabama": 4.00,
    "Alaska": 0.00,
    "Arizona": 5.60,
    "Arkansas": 6.00,
    "California": 6.00,
    "Colorado": 2.90,
    "Connecticut": 6.35,
    "Delaware": 0.00,
    "Florida": 6.00,
    "Georgia": 4.00,
    "Hawaii": 4.00,
    "Idaho": 6.00,
    "Illinois": 6.25,
    "Indiana": 7.00,
    "Iowa": 6.00,
    "Kansas": 6.50,
    "Kentucky": 6.00,
    "Louisiana": 4.45,
    "Maine": 5.50,
    "Maryland": 6.00,
    "Massachusetts": 6.25,
    "Michigan": 6.00,
    "Minnesota": 6.875,
    "Mississippi": 7.00,
    "Missouri": 4.225,
    "Montana": 0.00,
    "Nebraska": 5.50,
    "Nevada": 6.85,
    "New Hampshire": 0.00,
    "New Jersey": 6.625,
    "New Mexico": 5.125,
    "New York": 4.00,
    "North Carolina": 4.75,
    "North Dakota": 5.00,
    "Ohio": 5.75,
    "Oklahoma": 4.50,
    "Oregon": 0.00,
    "Pennsylvania": 6.00,
    "Rhode Island": 7.00,
    "South Carolina": 6.00,
    "South Dakota": 4.50,
    "Tennessee": 7.00,
    "Texas": 6.25,
    "Utah": 4.70,
    "Vermont": 6.00,
    "Virginia": 5.30,
    "Washington": 6.50,
    "West Virginia": 6.00,
    "Wisconsin": 5.00,
    "Wyoming": 4.00
}


def datagather():
    ifstates = input("are you in the united states? Y/N")
    if ifstates == N:
        print("this program is only applys to the unites states")
    else:
        print("hello what state are you in?")
        print("the options are")
        for key in statesalestax.keys():
             print(key)
    stateinput = input("input state ")
    return stateinput
#ugly but it works 
def taxcalc(state):
    statetax = statesalestax[state]
    pretax = float(input("what is the cost of the transaction $"))
    tax = pretax * (statetax / 100)
    print(f"The tax on a {pretax} purchase in {state} is ${tax}")



print("this program is made for processing sales tax on a state level")


state = datagather()
taxcalc(state)
