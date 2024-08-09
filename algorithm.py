import random
from collections import deque


# Random Walk functions
def random_walk(graph, start_node, steps):
    current_node = start_node
    walk = [current_node]
    for _ in range(steps - 1):
        neighbors = list(graph.neighbors(current_node))
        if neighbors:
            current_node = random.choice(neighbors)
            walk.append(current_node)
        else:
            break
    return walk


def random_walk_with_flyback(graph, start_node, steps, p):
    current_node = start_node
    walk = [current_node]
    for _ in range(steps - 1):
        if random.random() < p:
            current_node = start_node  # Fly back to start node
        else:
            neighbors = list(graph.neighbors(current_node))
            if neighbors:
                current_node = random.choice(neighbors)
        walk.append(current_node)
    return walk


def unbiased_BFS(graph, start_node, steps):
    queue = deque([start_node])
    visited = set([start_node])
    walk = [start_node]

    while queue and len(walk) < steps:
        current_node = queue.popleft()
        neighbors = list(graph.neighbors(current_node))
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                walk.append(neighbor)
                if len(walk) >= steps:
                    break

    return walk
