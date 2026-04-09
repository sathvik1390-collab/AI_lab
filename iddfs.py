graph = {
    '1':['2','3'],
    '2':['4'],
    '3':['5','6'],
    '4':[],
    '5':['7'],
    '6':[],
    '7':[]
}

def dls(node,goal,depth,path):
    print(f"Visiting:{node},Depth left:{depth}")
    path.append(node)
    if node == goal:
        return True
    if depth == 0:
        path.pop()
        return False
    for neighbour in graph[node]:
        if dls(neighbour, goal, depth - 1, path):
            return True
    path.pop()
    return False

def iddfs(start,goal,limit):
    for depth in range(limit + 1):
        print(f"\nSearching with depth limit = {depth}")
        path = []
        if dls(start, goal, depth, path):
            print("\nElement Found")
            print("Path:", " -> ".join(path))
            return True
    print("\nElement Not Found")
    return False

start = '1'
goal = '7'
limit = 3
iddfs(start, goal, limit)
 