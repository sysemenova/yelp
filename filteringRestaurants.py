import json

# Files. h is Hispanic, o is not. r is reading, w is writing.
rh = open("HispanicRestaurants.txt", mode = "r", encoding = "Latin-1")
wh = open("HispanicFiltered.txt", mode = "w", encoding = "Latin-1")

ro = open("NonHispanicRestaurants.txt", mode = "r", encoding = "Latin-1")
wo = open ("NonHispanicFiltered.txt", mode = "w", encoding = "Latin-1")


# Threshhold: we may want to change it
limit = 10


# Go through Hispanic and filter it
line = rh.readline()
while line:

    curJson = json.loads(line)
    reviewCount = curJson["review_count"]

    if reviewCount >= limit:
        wh.write(line)
    line = rh.readline()


# Go through non Hispanic and filter it
line = ro.readline()
while line:

    curJson = json.loads(line)
    reviewCount = curJson["review_count"]

    if reviewCount >= limit:
        wo.write(line)
    line = ro.readline()


rh.close()
wh.close()
ro.close()
wo.close()
