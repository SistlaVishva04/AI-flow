def topological_sort(nodes, edges):
    graph = {n.id: [] for n in nodes}

    for e in edges:
        graph[e.source].append(e.target)

    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for nxt in graph[node]:
            dfs(nxt)
        stack.append(node)

    for n in graph:
        dfs(n)

    return stack[::-1]
