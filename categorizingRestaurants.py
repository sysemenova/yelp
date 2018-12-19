import json

# The three file variables.
a = open("Restaurants.txt", mode = "r", encoding = "Latin-1")
wh = open("HispanicRestaurants.txt", mode = "w", encoding = "Latin-1")
wo = open("NonHispanicRestaurants.txt", mode = "w", encoding = "Latin-1")


# Restaurants <- important part of categories
# Argentine, Brazilian, Caribbean, Dominican, Haitian, Puerto Rican, Trinidadian
# Catalan, Cuban, Honduran, Latin American, Colombian, Salvadoran, Venezuelan,
# Mexican, Tacos, Nicaraguan, Spanish, Tapas Bars, Tapas/Small Plates,
# *Tex-Mex, 

restaurantTags = ["Argentine", "Brazilian", "Caribbean", "Dominican", "Haitian",
                  "Puerto Rican", "Trinidadian", "Catalan", "Cuban", "Honduran",
                  "Latin American", "Colombian", "Salvadoran", "Venezuelan",
                  "Mexican", "Tacos", "Nicaraguan", "Spanish", "Tapas Bars",
                  "Tapas/Small Plates", "Tex-Mex"]


line = a.readline()
while line:

    curJson = json.loads(line)
    categories = curJson["categories"]
    
    if categories != None:
        if "Restaurants" in categories:
            # If its a restaurant, we'll use it, otherwise, we won't
            if any(x in categories for x in restaurantTags):
                wh.write(line)
            else:
                wo.write(line)

    line = a.readline();

a.close()
wh.close()
wo.close()
