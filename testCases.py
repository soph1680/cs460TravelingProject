from main import buildGraph

# build the travel graph
travel = buildGraph()


#test case 1: san diego to san jose
print("Test Case 1: San Diego to San Jose")
bestCost, cheapestPath = travel.dijkstra("San Diego", "San Jose", weight="cost")
bestTime, fastestPath = travel.dijkstra("San Diego", "San Jose", weight="time")

print(f"\nCheapest path cost: ${bestCost:.2f}")
for src, dst, cost, time, mode in cheapestPath:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")

print(f"\nFastest path time: {bestTime} min")
for src, dst, cost, time, mode in fastestPath:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")\

#test case 2: los angeles to sacramento 
bestCost, cheapestPath = travel.dijkstra("Los Angeles", "Sacramento", weight="cost")
bestTime, fastestPath = travel.dijkstra("Los Angeles", "Sacramento", weight="time")

print(f"\nCheapest path cost: ${bestCost:.2f}")
for src, dst, cost, time, mode in cheapestPath:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")

print(f"\nFastest path time: {bestTime} min")
for src, dst, cost, time, mode in fastestPath:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")



#test case 2: los angeles to sacramento 
print(f"\nTest Case 2: Los Angeles to Sacramento")
bestCost2, cheapestPath2 = travel.dijkstra("Los Angeles", "Sacramento", weight="cost")
bestTime2, fastestPath2 = travel.dijkstra("Los Angeles", "Sacramento", weight="time")

print(f"\nCheapest path cost: ${bestCost2:.2f}")
for src, dst, cost, time, mode in cheapestPath2:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")

print(f"\nFastest path time: {bestTime2} min")
for src, dst, cost, time, mode in fastestPath2:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")



#test case 3: oakland to san diego 
print(f"\nTest Case 3: Oakland to San Diego")
bestCost3, cheapestPath3 = travel.dijkstra("Oakland", "San Diego", weight="cost")
bestTime3, fastestPath3 = travel.dijkstra("Oakland", "San Diego", weight="time")

print(f"\nCheapest path cost: ${bestCost3:.2f}")
for src, dst, cost, time, mode in cheapestPath3:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")

print(f"\nFastest path time: {bestTime3} min")
for src, dst, cost, time, mode in fastestPath3:
    print(f" {src} -> {dst}: {mode}, ${cost:.2f}, {time} min")

#brute force testing to compare if it matches dijkstra
bfCost = travel.bruteForce("Oakland", "San Diego", weight="cost")
print(f"\nBrute-Force: ${bfCost: .2f}")
