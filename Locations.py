import json
import os
mapping_list = []
hispanic = open("HispanicUS.txt", "r")
nonhispanic = open("NonHispanicUS.txt", "r")
newFile = open("hi.txt", "w")

def readAndWrite (file, boolean):
    line = file.readline()
    while line:
        js = json.loads(line)
        code = js["postal_code"]
        rating = js["stars"]
        rating = str(rating/5)
        newFile.write(code + ", " + str(boolean) + ", " + rating + "\n")
        line = file.readline()

readAndWrite(hispanic, 1)
readAndWrite(nonhispanic, 0)
newFile.close()


