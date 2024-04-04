class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class BSTNode:
    def __init__(self, key, data) -> None:
        self.data = data
        self.key = key
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self) -> None:
        self.root = None


    def update(self, key, data):
        """Sets the data value of the value pair with equal key to data"""
        
        self._update_recur(key, data, self.root)
    
    def _update_recur(self, key, data, root):
        if root is None:
            raise NotFoundException
            
        elif root.key == key:
            root.data = data
            return
            
        if key < root.key:
            return self._update_recur(key, data, root.left)
        elif key >= root.key:
            return self._update_recur(key, data, root.right)
        
        return root
    
    def __setitem__(self, key, data):
        """Override to allow this syntax: some_bst_map[key] = data"""
        try:
            self.update(key, data)
        except NotFoundException:
            if self.root.key != key:
                self.insert(key, data)
        return self.root.data 


    def find(self, key):
        """Returns the data value of the value pair with equal key"""
        return self._find_recur(key, self.root)
    
    def __getitem__(self, key):
        """Returns the data value of the value pair with equal key """
        return self._find_recur(key, self.root)
        

         
    def _find_recur(self, key, root:BSTNode):
        
        if root is None:
            raise NotFoundException
            
        elif root.key == key:
            return root.data
        if key < root.key:
            return self._find_recur(key, root.left)
        elif key >= root.key:
            return self._find_recur(key, root.right)
        

    def _insert_recur(self, key, data, root:BSTNode):
        if root is None:
            return BSTNode(key, data)
        if key < root.key:
            root.left = self._insert_recur(key, data, root.left)
        elif key > root.key:
            root.right = self._insert_recur(key, data, root.right)
        elif key == root.key:
            raise ItemExistsException
        return root


    def insert(self, key, data):
        """Adds this value pair to the collection"""
        self.root = self._insert_recur(key, data, self.root)
    
    def _contain_recur(self, key, root):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._contain_recur(key, root.left)
        elif key > root.key:
            return self._contain_recur(key, root.right)


    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise false"""
        return self._contain_recur(key, self.root)
    
    def _str_recur(self, root):
        ret_string = ""
        if root is None:
            return ret_string
        ret_string += self._str_recur(root.left)
        ret_string += "{" + f"{root.key}:{root.data}" + "}" + " " 
        ret_string += self._str_recur(root.right)
        return ret_string

    def __str__(self) -> str:
        """Returns a string with the items orderedd by key and separated by a single space"""
        ret_string = "output: "
        ret_string += self._str_recur(self.root)
        return ret_string
    

    def remove(self, key):
        """Removes the value pair with equal key from the collection"""
        self.root = self._remove_recur(key, self.root)

    def _remove_recur(self, key, root):
        if root is None:
            return None
        if key == root.key:
            root = self._remove_root(root)
        elif key < root.key:
            root.left = self._remove_recur(key, root.left)
        elif key > root.key:
            root.right = self._remove_recur(key, root.right)
        return root
    
    def _remove_root(self, root):
        if root.left is None and root.right is None:
            return None
        elif root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        else:
            root.right = self._go_left(root.right, root)
            return root
    

    def _go_left(self, root, org_root):
        
        if root.left is None:
            org_root.key = root.key
            org_root.data = root.data

            return self._remove_root(root)
        root.left = self._go_left(root.left, org_root)
        return root


    def __len__(self):
        """Returns the number of items in the entire data structure"""
        return self._len_recur(self.root)
    

    def _len_recur(self, root):
        if root is None:
            return 0
        return self._len_recur(root.left) + 1 + self._len_recur(root.right)
