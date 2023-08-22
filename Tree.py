from collections import deque

class TreeNode:

    def __init__(self, songs = None, album = None, artist = None, genre = None) -> None:
        self.songs = songs
        self.album = album
        self.artist = artist
        self.genre = genre
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.name)
            nodes_to_visit += current_node.children
# Tree Visualization helper ! 
    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
      
            if level > 0:
                level_str += "| "*(level-1)+ "|-"
            level_str += str(node.name)
            level_str += "\n"
            level+=1
            for child in reversed(node.children):
                stack.append([child, level])

        return level_str
            