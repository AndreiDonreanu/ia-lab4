
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


    def inorder(self,list):

        if self.left:
            self.left.inorder(list)

        list.append(self.val)

        if self.right:
            self.right.inorder(list)


    def postorder(self,list):
        if self.left:
            self.left.postorder(list)
        if self.right:
            self.right.postorder(list)
        list.append(self.val)

    def preorder(self,list):
        list.append(self.val)
        if self.left:
            self.left.preorder(list)
        if self.right:
            self.right.preorder(list)


    def same_tree(self,other):
        list1=[]
        list2=[]
        self.inorder(list1)
        self.preorder(list1)
        self.postorder(list1)
        other.inorder(list2)
        other.preorder(list2)
        other.postorder(list2)

        if list1 == list2:
            return True

        else:
            return False