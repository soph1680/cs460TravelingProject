from project import TravelGraph
 
#money in dollars, time in minutes 
def buildGraph():
    travel = TravelGraph()
 
    travel.addEdge("San Diego", "Los Angeles", 21.95, 150, "car")
    travel.addEdge("San Diego", "Los Angeles", 36.00, 165, "train")
    travel.addEdge("San Diego", "Los Angeles", 44.98, 215, "bus")

    travel.addEdge("Los Angeles", "Santa Barbara", 17.21, 90, "car")
    travel.addEdge("Los Angeles", "Santa Barbara", 29.00, 100, "train") 
    travel.addEdge("Los Angeles", "Santa Barbara", 12.00, 120, "bus")  

    travel.addEdge("Los Angeles", "Riverside", 10.32, 60, "car")
    travel.addEdge("Los Angeles", "Riverside", 8.00, 75, "bus")   
 

    travel.addEdge("Los Angeles", "Bakersfield", 18.93, 100, "car")
    travel.addEdge("Los Angeles", "Bakersfield", 22.00, 120, "bus")   

    travel.addEdge("Santa Barbara", "San Luis Obispo", 17.21,  90, "car")
    travel.addEdge("Santa Barbara", "San Luis Obispo", 22.00, 110, "train")
    travel.addEdge("Santa Barbara", "San Luis Obispo", 10.00, 105, "bus") 
 

    travel.addEdge("Riverside",  "Bakersfield", 20.65, 110, "car")
    travel.addEdge("Riverside",  "Bakersfield", 16.00, 130, "bus")  
 

    travel.addEdge("Bakersfield",  "Fresno", 18.93,  90, "car")
    travel.addEdge("Bakersfield",  "Fresno", 14.00, 110, "bus")  

    travel.addEdge("Bakersfield",  "San Luis Obispo", 22.37, 120, "car")
    travel.addEdge("Bakersfield",  "San Luis Obispo", 18.00, 145, "bus")  

    travel.addEdge("Fresno", "San Jose", 31.83, 180, "car")
    travel.addEdge("Fresno", "San Jose", 24.00, 210, "bus")  

    travel.addEdge("Fresno", "Sacramento", 31.83, 170, "car")
    travel.addEdge("Fresno",  "Sacramento", 2.00, 200, "bus")   
 
    travel.addEdge("San Jose", "San Francisco", 8.60, 60, "car")
    travel.addEdge("San Jose", "San Francisco", 10.00, 70, "train")
    travel.addEdge("San Jose", "San Francisco", 17.00, 75, "bus")   
 
    travel.addEdge("San Jose", "Sacramento", 22.37, 120, "car")
    travel.addEdge("San Jose", "Sacramento", 28.00, 135, "train")
    travel.addEdge("San Jose", "Sacramento", 18.00, 150, "bus") 
 

    travel.addEdge("San Francisco","Oakland", 2.58, 25, "car")
    travel.addEdge("San Francisco","Oakland", 4.50, 30, "train") 
    travel.addEdge("San Francisco","Oakland", 10.00, 35, "bus") 
 
    travel.addEdge("Oakland", "Sacramento", 13.77,  75, "car")
    travel.addEdge("Oakland", "Sacramento", 23.00,  90, "train") 
    travel.addEdge("Oakland",  "Sacramento", 15.00, 100, "bus")  
 
    return travel
 
