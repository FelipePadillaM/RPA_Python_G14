class Tree:
    
    def __init__(self, key) -> None:
        
        self.val = key
        self.left = None
        self.right = None

    def insert(self, key):

        if self.val is None:
            return Tree(key.size)

        if key.size < self.val.size:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Tree(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Tree(key)
                return

    def pre_order(self):
        print(self.val, end=' ')

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        
        if self.left:
            self.left.in_order()

        print(self.val, end=' ')
        print()

        if self.right:
            self.right.in_order()

    def post_order(self):
        
        if self.left:
            self.left.post_order()
        
        if self.right:
            self.right.post_order()
        
        print(self.val, end=' ')

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    


    
