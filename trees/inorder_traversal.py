from tree_base import TreeNode
import random
def create_b(count):
    
    node = TreeNode(random.randint(1,10))
    count -= 1
    def recurse(count): #can't call - or + function python
        if count == 0:
            return None
        node = TreeNode(random.randint(0,10))
        if random.randint(0,1) == 0:
            node.left = recurse(count - 1)
            
        if random.randint(0,1 )== 0:
            node.right = recurse(count - 1)
            
         
    recurse(count)
    return node

root = create_b(5)

def print_tree(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        length = len(stack)
        level = []
        
        for i in range(length):
            cur = stack.pop(0)  # Use pop(0) to achieve FIFO order, simulating a queue
            if cur:
                level.append(cur.value)
                stack.append(cur.left)
                stack.append(cur.right)
        
        print(' '.join(map(str, level)))
print_tree(root)