#Group no: 45
#Name: Jadida Kalim
#Student no: 21436054
#Name: Thabiso Nkosi
#Student no: 22507745

bfs_dfs = 0

""" This class creates a node and initializes all the properties that a node has such is its data, parent and children"""
class Node:
    def __init__(self, data):
        self.data = data  # variable that contains the data that needs to be stored in Node object
        self.children = [None, None, None]  # A list of size 3 used to store the children(R,P,S) of a node if it has any.
        self.parent = None  # variable used to store parent node of the current Node object.

    """This method is used to add 3 children (R,P,S) to a node"""
    def add_children(self):
        R = Node('R')
        P = Node('P')
        S = Node('S')

        R.parent = self
        P.parent = self
        S.parent = self

        self.children[0] = R
        self.children[1] = P
        self.children[2] = S

"""This class contains methods that build and search a tree by either using BFS or DFS"""
class Tree:
    def __init__(self,d):
        self.depth = d #initializes the depth of the tree
        self.root = Node("") #creates the "root" node of the tree.

    def buildBfs(self):

        """This function builds and searches a tree dynamically using BFS. A list is returned containing the sequences represented by each
        node in the order in which they are visited. The tree building and searching starts at the root node up until the
        depth of the tree is reached. The way this function works is that there is a list, (queue) that contains a tuple.
        The tuple stores the current node and a string containing the current node's parent's data. """

        visited = [] #list used to store the sequences represented by each node
        queue = [(self.root, "")]
        bfsDepth = self.depth #stores the depth of the tree

        while queue:
            """While queue is not empty, the first tuple stored in queue is removed and the values stored in the tuple are assigned 
            to this_node and this_node_parents. They are then appended to visited. The reason why the first value stored is removed
            is because BFS first goes through all the nodes in a tree level before moving onto the next level and therefore uses a 
            FIFO approach. """

            this_node, this_node_parents = queue.pop(0)
            visited.append(this_node_parents + str(this_node.data))

            """This if statement then checks if the length of the string, this_node_parents, is less than depth-1. This to 
            make sure that the tree is only built to the specified depth. Depth-1 is used because if, for example the depth 
            variable has a value of 3 then no children should be added to the current node if the length of this_node_parents 
            is 2 as the nodes on the final depth will only have 2 parent nodes before them. If this if statement is true then
            child nodes are added to the current node, and each of the child nodes and their parents are stored in a tuple
            which is appended to queue"""

            if len(this_node_parents) < bfsDepth-1:
                this_node.add_children()
                for child in this_node.children:
                    if child is not None:
                        queue.append((child, visited[-1])) # visited[-1] conatins the data of the child node's parents
            elif bfsDepth == 1:
                """The elif statement is used if the depth is 1 since the if statement does not work for such a case. It has the same 
                functionlity as the if statement except the child nodes are directly appended to the visited list"""
                this_node.add_children()
                i = 0
                while i<3: # i<3 because each node has 3 children
                    visited.append(this_node.children[i].data)
                    i += 1

        visited.pop(0) #the first value is removed because it contains the data of the root node, which is an empty string
        return visited

    def buildDfs(self):

        """This function builds and searches a tree dynamically using DFS. A list is returned containing the sequences represented by each
        node in the order in which they are visited. The tree building and searching starts at the root node up until the
        depth of the tree is reached. The way this function works is that there is a list, (stack) that contains a tuple.
        The tuple stores the current node and a string containing the current node's parent's data. """

        visited = [] #list used to store the sequences represented by each node
        stack = [(self.root, "")]
        dfsDepth = self.depth #stores the depth of the tree

        while stack:
            """While stack is not empty, the last tuple stored in stack is removed and the values stored in the tuple are assigned 
            to this_node and this_node_parents. They are then appended to visited. The reason why the last value stored is removed
            is because when DFS reaches a node it traverses one child of that specific node first until it reaches the final 
            depth where that current node has no more children. Then only does it travel up the tree and explore all the other
            children and node. Therefore DFS uses a LIFO approach."""

            this_node, this_node_parents = stack.pop()
            visited.append(this_node_parents + str(this_node.data))

            """This if statement then checks if the length of the string, this_node_parents, is less than depth-1. This to 
            make sure that the tree is only built to the specified depth. Depth-1 is used because if, for example the depth 
            variable has a value of 3 then no children should be added to the current node if the length of this_node_parents 
            is 2 as the nodes on the final depth will only have 2 parent nodes before them. If this if statement is true then
            child nodes are added to the current node, and each of the child nodes and their parents are stored in a tuple
            which is appended to stack"""

            if len(this_node_parents) < dfsDepth-1:
                this_node.add_children()
                for child in this_node.children[::-1]: #the last child is added first due to the way in which DFS traverses a tree
                    if child is not None:
                        stack.append((child, visited[-1])) # visited[-1] conatins the data of the child node's parents
            elif dfsDepth == 1:
                """The elif statement is used if the depth is 1 since the if statement does not work for such a case. It has the same 
                functionlity as the if statement except the child nodes are directly appended to the visited list"""
                this_node.add_children()
                i = 0;
                while i<3: # i<3 because each node has 3 children
                    visited.append(this_node.children[i].data)
                    i += 1

        visited.pop(0) #the first value is removed because it contains the data of the root node, which is an empty string
        return visited

tree = Tree(5) # a Tree object with a depth of 5 is created because the maximum length of the break sequence is 5

if input == "":
    traversed = [] # stores all the node sequences visited
    list = [] # this list is later used to store the lists returned from buildBFS and buildDFS
    history = [] # stores the previous moves played by breakable.py
    index = -1 # used for the indexing of the variable "list"
    repeats = 0
    sequence = "" # stores the current sequence that is being played
    repeat = False # this variable is set to true if breakable.py is repeating its moves
    was_repeat = False # this variable is set to true if breakable.py was previously repeating its moves
    if bfs_dfs == 0:
        list = tree.buildBfs()
    elif bfs_dfs == 1:
        list = tree.buildDfs()
else:
    history.append(input)
    if len(history) >= 2:
        if history[-1] == history[-2]: # this if statement helps to check if breakable.py is repeating its moves
            repeat = True

"""This if statement checks if repeat is True and it sets "sequence" to the previous sequence from "list" as that could possibly
be the break sequence. While breakable.py seems to keep repeating its moves, the move that would beat breakable.py's move is
played. Repeat is then set to false"""

if repeat == True:
    sequence = list[index - 1]

    if history[-1] == "R":
        object = "P"
    elif history[-1] == "P":
        object = "S"
    elif history[-1] == "S":
        object = "R"
    repeat = False
elif len(history) >= 3 and (history[-3] == history[-2]) and (history[-2] != history[-1]): # this elif statement checks if breakable.py was repeating its moves
    was_repeat = True
else:
    if sequence == "":
        if was_repeat == True:
            """if was_repeat is true, index remains the same value because incase the sequence that the program thought was
            the break sequence actually isn't, the sequence after the potential break sequence can be played"""
            index = index
            traversed.pop() # removes the last sequence stored before the break sequence was triggered as this sequence was not played as yet
            was_repeat = False
        else:
            index += 1

        sequence = list[index]
        traversed.append(list[index])

    if len(sequence) >= 1: # checks that the string "sequence" is not empty
        object = sequence[0]
        sequence = sequence[1:]

output = object

""" 
Results:

The agent does win 100% of the games most of the time. Although it was also found that no matter how high or low the 
number of matches were, as the number of rounds decreased the chances of winning also drastically decreased and even went as 
low as 0% depending on how low the number of rounds were. This is most likely due to the fact that the number of rounds per 
match were not enough rounds to enable the agent to actually find the break sequence in the list of all sequences that stores
all the possible sequences. For example if the break sequence for a certain match was RRSSP and the number of rounds were 30,
the agent would not at all reach this break sequence and would therefore lose the match entirely. 

Another thing that was noticed was that if the rounds were high and the number of matches played were the same as the number
of rounds played, the agent would mostly win 98/99% of the games. This could be due to the way in which the game is in a sense 
played randomly even though each agent has its own specific strategy. The strategies of each agent might also not be 100% 
perfect. It could also once again be due to the fact that the agent does not reach the break sequence in 1 or 2 of the matches
because there were not enough rounds played in order to reach it.

In terms of whether BFS or DFS is the better option the following results were obtained:

* For 10 matches and 1000 rounds run 10 times for each search strategy, Both strategies won an average of 100% of the matches.
BFS won on average 57.6% of the rounds and DFS won 55.58% of the rounds.

* For 20 matches and 30 rounds run 10 times for each search strategy, BFS won an average of 66% of the matches and DFS won an
average of 48% of the matches. BFS won on average 42.25% of the rounds and DFS won 35.27% of the rounds.

* For 1000 matches and 1000 rounds run 10 times for each search strategy, BFS won an average of 99.66% of the matches and DFS
won an average of 99.14% of the matches. BFS won on average 58.62% of the rounds and DFS won 55.37% of the rounds.

From these results overall it can be seen that BFS almost always wins a higher percentage of the matches than DFS. This is 
most likely because of the fact that in BFS each node on each level is searched first before proceeding to the next level. In
DFS one node and one of its children are initially searched and it only starts searching all the other nodes and  levels 
once the depth of the tree is reached and there are no more child nodes to search. Therefore in most cases BFS finds the break 
sequence faster than DFS, due to it having a shorter search path than DFS most of the time. 

The code was also run by manually changing the depth in breakable.py. It was noticed that when the depth of the tree was low such 
as 2 or 3, BFS found the break sequence faster most of the time and when the depth was higher, such as 4 or 5, DFS found the 
break sequence faster most of the time. This shows BFS is usually better in terms of searching for solutions that are closer
to the root node and DFS is better when it comes to searching for solutions that are deeper in the tree. 

It should also be noted that these results were also affected by the faultiness of breakable.py, as in when the break sequence is
triggered even though the actual break sequence is not reached. This faultiness increases as the length of the break sequence 
increases and this also affects the win rate of the agents. 

rpsrunner.py output:

Pool 1: 1 bots loaded
Pool 2: 1 bots loaded
Playing 5000 matches per pairing.
Running matches in 4 threads
5000 matches run
total run time: 5814.59 seconds

breakable.py: won 0.0% of matches (0 of 5000)
    won 19.0% of rounds (9513637 of 50000000)
    avg score -4289.7, net score -21448527.0

main.py: won 100.0% of matches (5000 of 5000)
    won 61.9% of rounds (30962164 of 50000000)
    avg score 4289.7, net score 21448527.0

"""
