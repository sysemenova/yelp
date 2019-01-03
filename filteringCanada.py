import json

# Files. h is hispanic, o is not. r is reading, w is writing.
rh = open("HispanicFiltered.txt", mode = "r", encoding = "Latin-1")
wh = open("HispanicUS.txt", mode = "w", encoding = "Latin-1")

ro = open("NonHispanicFiltered.txt", mode = "r", encoding = "Latin-1")
wo = open("NonHispanicUS.txt", mode = "w", encoding = "Latin-1")

# Things we want to exclude (may want to make this include instead)
# For now this is okay
allStates =     ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                 "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                 "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                 "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                 "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

statesIn = []

# Hispanic
line = rh.readline()
while line:
    curJson = json.loads(line)
    state = curJson["state"]

    if state != None:
        if state in allStates:
            # If not(state is in the list of things we don't want)
            wh.write(line)
    line = rh.readline()

# Non hispanic
line = ro.readline()
while line:
    curJson = json.loads(line)
    state = curJson["state"]

    if state != None:
        
        if state in allStates:
            # If if it's in the state list
            wo.write(line)
            if not(state in statesIn):
                statesIn.append(state)
            
    line = ro.readline()

print(statesIn)
