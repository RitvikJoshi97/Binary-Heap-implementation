class Node:
    def __init__(self,key = None, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    

class BinaryHeap():
    def __init__(self, key = None):
        self.root = Node(key)
        self.structure = [self.root]
    
    # As the order is fixed, we can make a function to define how to make the order as well
    # But this is almost as good, as the time complexity in both cases will be constant
    order = {}
    order["0"] = None
    order["1"] = 0
    order["2"] = 0
    order["3"] = 1
    order["4"] = 1
    order["5"] = 2
    order["6"] = 2
    order["7"] = 3
    order["8"] = 3
    order["9"] = 4
    order["10"] = 4
    order["11"] = 5
    order["12"] = 5


    # O(1) - constant
    def min(self):
        return self.structure[0].key

    def max(self):
        max_key = self.structure[0].key
        for each in self.structure:
            if each.key > max_key:
                max_key = each.key
        return max_key


    def insert(self, key):

        def exchange(node1, node2):
            temp = node1.key
            node1.key = node2.key
            node2.key = temp


        self.structure.append(Node(key))
        node_pos = len(self.structure) - 1

        parent_pos = self.order[str(node_pos)]
        if parent_pos != None:
            self.structure[node_pos].parent = self.structure[parent_pos]
        
        runBubble = []
        def bubble(node_pos):
            changes_made = True
            while changes_made == True:
                parent_pos = self.order[str(node_pos)]
                if parent_pos != None:
                    if self.structure[parent_pos].key > self.structure[node_pos].key:
                        exchange(self.structure[node_pos],self.structure[parent_pos])

                        runBubble.append(node_pos)

                        node_pos = parent_pos
                        continue
                    else:
                        changes_made = False
                else:
                    changes_made = False
            return
        
        bubble(node_pos)

        while len(runBubble) != 0:
            bubble(runBubble[0])
            runBubble.pop(0)


        # Give the children to the node
        if self.order[str(node_pos)] == self.order[str(node_pos-1)]:
            #child is parent's left child
            self.structure[node_pos].parent.right = self.structure[node_pos]
        else:
            self.structure[node_pos].parent.left = self.structure[node_pos]


    # O(m) 
    # where m is the height of the tree
    def extract(self):
        def exchange(node1, node2):
            temp = node1.key
            node1.key = node2.key
            node2.key = temp

        
        
        def bubbleDown(node):
            changes_made = True
            while changes_made == True:
                if node.left != None and node.right!= None:
                    if node.left.key < node.right.key:
                        child = node.left
                    else:
                        child = node.right
                elif node.left != None and node.right== None:
                    child = node.left
                elif node.left == None and node.right != None:
                    child = node.right
                else:
                    child = None
                
                if child != None:
                    if child.key < node.key:
                        exchange(node,child)
                        node = child
                    else:
                        changes_made = False
                else:
                    changes_made = False
                    
        
        elem = self.structure[0].key
        self.structure[0].key = self.structure[-1].key
        self.structure.pop(len(self.structure)-1)

        bubbleDown(self.structure[0])
        return elem
    
    def search(self,key):
        for each in self.structure:
            if each.key == key:
                return (str(key)+" found with parent: "+ str(each.parent.key))
        return "not found"
        


binaryHeap = BinaryHeap(20)
binaryHeap.insert(9)
binaryHeap.insert(12)
binaryHeap.insert(6)
binaryHeap.insert(13)
binaryHeap.insert(1)
binaryHeap.insert(8)
binaryHeap.insert(7)
binaryHeap.insert(15)
binaryHeap.insert(11)


k = 0
for i in range(1,6):
    for j in range(1,i):
        if k < len(binaryHeap.structure):
            print(binaryHeap.structure[k].key, end=" ")
            k += 1
    print()

print("#####")

print("min: ", binaryHeap.min())

print("#####")
print("extract")
print(binaryHeap.extract())


print("#####")



k = 0
for i in range(1,6):
    for j in range(1,i):
        if k < len(binaryHeap.structure):
            print(binaryHeap.structure[k].key, end=" ")
            k += 1
    print()



print("#####")

print("max: ", binaryHeap.max())


print("#####")

print("search 12: ", binaryHeap.search(12))

