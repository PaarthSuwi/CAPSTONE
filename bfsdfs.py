# BFS Implementation
def bfs(graph, start):
    queue = [start]  # Use a list as a queue
    visited = set([start])
    order = []

    while queue:
        node = queue.pop(0)  # Remove from the front (FIFO)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# DFS Implementation
def dfs(graph, start):
    stack = [start]  # Use a list as a stack
    visited = set([start])
    order = []

    while stack:
        node = stack.pop()  # Remove from the top (LIFO)
        order.append(node)

        for neighbor in reversed(graph[node]):  # Reverse to maintain left-to-right order
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order

# Function to convert numbers to letters
def number_to_letter(order):
    return [chr(96 + num) for num in order]

# Example Usage
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2, 6],
    5: [2],
    6: [4]
}

start_node = 1

# BFS Traversal
bfs_order = bfs(graph, start_node)
bfs_letters = number_to_letter(bfs_order)
print("BFS Order (Letters):", bfs_letters)

# DFS Traversal
dfs_order = dfs(graph, start_node)
dfs_letters = number_to_letter(dfs_order)
print("DFS Order (Letters):", dfs_letters)