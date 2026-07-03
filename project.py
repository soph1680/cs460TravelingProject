import heapq
from collections import defaultdict

# Testing from San Diego -> Los Angeles -> San Jose
class TravelGraph:
    def __init__(self):
        # Adjacency list storing neighbors and edge details
        self.graph = defaultdict(list)

    def addEdge(self, src, dst, cost, time, mode):
        # Add edge in both directions since travel is bidirectional
        self.graph[src].append((dst, cost, time, mode))
        self.graph[dst].append((src, cost, time, mode)) 

    def dijkstra(self, start, end, weight="cost"):
        # intalize all distances to infinity
        dist = defaultdict(lambda: float("inf"))
        dist[start] = 0
        # track previous nodes for reconstruction
        prev = {}
        # min-heap priority queue
        pq = [(0, start)]
        # if seen does not to repeat further
        seen = set()
        while pq:
            w, node = heapq.heappop(pq)

            # skip if seen
            if node in seen:
                continue
            seen.add(node)

            # stop if the destination is there
            if node == end:
                break

            # check all neighbors
            for neighbor, cost, t, mode in self.graph[node]:
                edgeWeight = cost if weight == "cost" else t
                newDist = w + edgeWeight

                # update if shorter path found
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    prev[neighbor] = (node, cost, t, mode)
                    heapq.heappush(pq, (newDist, neighbor))

        if end not in prev:
            return None, []

        # Reconstruct path by walking backwards from end to start
        legs, cur = [], end
        while cur != start:
            parent, cost, t, mode = prev[cur]
            legs.append((parent, cur, cost, t, mode))
            cur = parent
        legs.reverse()

        return dist[end], legs

    def allPaths(self, start, end, visited=None):
        # Recursively find all simple paths for brute-force validation
        if visited is None:
            visited = {start}
        if start == end:
            yield []
            return
        for neighbor, cost, t, mode in self.graph[start]:
            if neighbor not in visited:
                for rest in self.allPaths(neighbor, end, visited | {neighbor}):
                    yield [(start, neighbor, cost, t, mode)] + rest 
    def bruteForce(self, start, end, weight="cost"):
        # Check every possible path to confirm Dijkstra found the true minimum
        key  = (lambda l: l[2]) if weight == "cost" else (lambda l: l[3])
        bestW = float("inf")
        for path in self.allPaths(start, end):
            total = sum(key(l) for l in path)
            if total < bestW:
                bestW = total
        return bestW
