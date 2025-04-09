
statesalestax = [
    4.00,
    0.00,
    5.60,
    6.00,
    6.00,
    2.90,
    6.35,
    0.00,
    6.00,
    4.00,
    4.00,
    6.00,
    6.25,
    7.00,
    6.00,
    6.50,
    6.00,
    4.45,
    5.50,
    6.00,
    6.25,
    6.00,
    6.875,
    7.00,
    4.225,
    0.00,
    5.50,
    6.85,
    0.00,
    6.625,
    5.125,
    4.00,
    4.75,
    5.00,
    5.75,
    4.50,
    0.00,
    6.00,
    7.00,
    6.00,
    4.50,
    7.00,
    6.25,
    4.70,
    6.00,
    5.30,
    6.50,
    6.00,
    5.00,
    4.00
]


states = [
    "Alabama -1",
    "Alaska -2",
    "Arizona -3",
    "Arkansas -4",
    "California -5",
    "Colorado -6",
    "Connecticut -7",
    "Delaware -8",
    "Florida -9",
    "Georgia -10",
    "Hawaii -11",
    "Idaho -12",
    "Illinois -13",
    "Indiana -14",
    "Iowa -15",
    "Kansas -16",
    "Kentucky -17",
    "Louisiana -18",
    "Maine -19",
    "Maryland -20",
    "Massachusetts -21",
    "Michigan -22",
    "Minnesota -23",
    "Mississippi -24",
    "Missouri -25",
    "Montana -26",
    "Nebraska -27",
    "Nevada -28",
    "New Hampshire -29",
    "New Jersey -30",
    "New Mexico -31",
    "New York -32",
    "North Carolina -33",
    "North Dakota -34",
    "Ohio -35",
    "Oklahoma -36",
    "Oregon -37",
    "Pennsylvania -38",
    "Rhode Island -39",
    "South Carolina -40",
    "South Dakota -41",
    "Tennessee -42",
    "Texas -43",
    "Utah -44",
    "Vermont -45",
    "Virginia -46",
    "Washington -47",
    "West Virginia -48",
    "Wisconsin -59",
    "Wyoming -50"
]


def datagather():
    ifstates = input("are you in the united states? (Y/N) ")


    if ifstates == "N":
        print("this program is only applys to the unites states")
        return None

    else:

        print("hello what state are you in?")
        print("the options are")
        for item in states:
             print(item)
        
        stateinput = input("input state ")  
    
        for i, state in enumerate(states):
            if stateinput.lower() in state.lower():
                return i
        stateinput = input("input state ")
        return stateinput
    
def taxcalc(state):
    if state is not None:  
        statetax = statesalestax[state]
        pretax = float(input("what is the cost of the transaction $"))
        tax = pretax * (statetax / 100)
        state_name = states[state].split(" -")[0] 
        print(f"The tax on a ${pretax} purchase in {state_name} is ${tax}")



print("this program is made for processing sales tax on a state level")


state = datagather()
taxcalc(state)
