import numpy as np
import random as rnd
import csv

csvColumns = ["image", "numberOfFish", "cod", "haddock", "hake", "horseMackerel", "whiting", "saithe", "taken"]
csvFile = "imageCatalogues.csv"
with open(csvFile, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=csvColumns)
    writer.writeheader()

species = ["cod", "haddock", "hake", "horseMackerel", "whiting", "saithe"]
usedIDs = [[], [], [], [], [], []] 
amount = [102, 119, 52, 58, 103, 13]
catalogue = dict(zip(species, amount))
catalogueUsed = dict(zip(species, usedIDs))
fishPerImage = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#fishPerImage = [4, 5, 6]
numberOfImages = 10
noImages = 0


for number in fishPerImage:
    print("Number of fish per image: ", number)
    for i in range(numberOfImages):
        noImages += 1
        imageCatalogue = dict(zip(csvColumns, [noImages, number, [], [], [], [], [], [], "no"]))
        for j in range(number):
            species, amount = rnd.choice(list(catalogue.items()))
            specimens = set(range(1, amount+1))
            specimensUsed = set(catalogueUsed[species])
            validSpecimens = list(specimens - specimensUsed)
            if ( len(validSpecimens) == 0 ):
                #print(len(specimensUsed))
                #specimensUsed.clear()
                print(species, "RESET RESET RESET")
                catalogueUsed[species].clear()
                validSpecimens = list(specimens)
                

            ID = rnd.choice(validSpecimens)    
            #print(ID,species)
            catalogueUsed[species].append(ID)
            imageCatalogue[species].append(ID)
            #print(imageCatalogue)

        print(imageCatalogue)
        with open(csvFile, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=csvColumns)
            writer.writerow(imageCatalogue)        

"""
print("=========================")
with open(csvFile, 'r') as file:
    for line in csv.DictReader(file):
        print(line)
"""
        
        
        
