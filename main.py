from project import TravelGraph
 

def buildGraph():
    travel = TravelGraph()
 
    travel.addEdge("San Diego", "Los Angeles", 21.95, 150, "car")
    travel.addEdge("San Diego", "Los Angeles", 36.00, 165, "train")
    travel.addEdge("San Diego", "Los Angeles", 276.00, 125, "plane")

    travel.addEdge("Los Angeles",  "Santa Barbara",  17.21,  90, "car")
    travel.addEdge("Los Angeles",  "Santa Barbara",  29.00, 100, "train")  # Pacific Surfliner
    travel.addEdge("Los Angeles",  "Santa Barbara",  12.00, 120, "bus")    # Flixbus

    travel.addEdge("Los Angeles",  "Riverside",      10.32,  60, "car")
    travel.addEdge("Los Angeles",  "Riverside",       8.00,  75, "bus")    # Flixbus
 

    travel.addEdge("Los Angeles",  "Bakersfield",    18.93, 100, "car")
    travel.addEdge("Los Angeles",  "Bakersfield",    15.00, 120, "bus")    # Greyhound

    travel.addEdge("Santa Barbara","San Luis Obispo", 17.21,  90, "car")
    travel.addEdge("Santa Barbara","San Luis Obispo", 22.00, 110, "train") # Pacific Surfliner
    travel.addEdge("Santa Barbara","San Luis Obispo", 10.00, 105, "bus")   # Flixbus
 

    travel.addEdge("Riverside",    "Bakersfield",    20.65, 110, "car")
    travel.addEdge("Riverside",    "Bakersfield",    16.00, 130, "bus")    # Greyhound
 

    travel.addEdge("Bakersfield",  "Fresno",         18.93,  90, "car")
    travel.addEdge("Bakersfield",  "Fresno",         14.00, 110, "bus")    # Greyhound
 
    travel.addEdge("Bakersfield",  "San Luis Obispo", 22.37, 120, "car")
    travel.addEdge("Bakersfield",  "San Luis Obispo", 18.00, 145, "bus")   # Greyhound
 
    travel.addEdge("Fresno",       "San Jose",        31.83, 180, "car")
    travel.addEdge("Fresno",       "San Jose",        24.00, 210, "bus")   # Greyhound

    travel.addEdge("Fresno",       "Sacramento",      31.83, 170, "car")
    travel.addEdge("Fresno",       "Sacramento",      22.00, 200, "bus")   # Greyhound
 
    travel.addEdge("San Jose",     "San Francisco",    8.60,  60, "car")
    travel.addEdge("San Jose",     "San Francisco",   10.00,  70, "train") # Caltrain
    travel.addEdge("San Jose",     "San Francisco",    7.00,  75, "bus")   # Flixbus
 
    travel.addEdge("San Jose",     "Sacramento",      22.37, 120, "car")
    travel.addEdge("San Jose",     "Sacramento",      28.00, 135, "train") # Amtrak Capitol Corridor
    travel.addEdge("San Jose",     "Sacramento",      18.00, 150, "bus")   # Flixbus
 

    travel.addEdge("San Francisco","Oakland",           2.58,  25, "car")
    travel.addEdge("San Francisco","Oakland",           4.50,  30, "train") # BART
    travel.addEdge("San Francisco","Oakland",           3.00,  35, "bus")   # AC Transit
 
    travel.addEdge("Oakland",      "Sacramento",      13.77,  75, "car")
    travel.addEdge("Oakland",      "Sacramento",      23.00,  90, "train") # Amtrak Capitol Corridor
    travel.addEdge("Oakland",      "Sacramento",      15.00, 100, "bus")   # Flixbus
 
    return travel
 
