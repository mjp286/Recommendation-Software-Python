from collections import deque

def adding_songs(root_node, genre):
    path_queue = deque()

    initial_path = [root_node]

    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        if current_node.genre == genre or current_node.genre is None:
            return current_node
        
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    return None

def getting_songs(root_node, genre):
    path_queue = deque()
    
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]

        if current_node.genre == genre:
            return current_node.children
            
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    return None
