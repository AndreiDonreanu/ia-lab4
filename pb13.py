import TreeNode

from TreeNode import  TreeNode



p1=TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
q1=TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))

print("Sunt p1 si q1 acelasi arbore?")
print(p1.same_tree(q1))

p2=TreeNode(1,TreeNode(2,None,None),None)
q2=TreeNode(1,None,TreeNode(2,None,None))

print("Sunt p2 si q2 acelasi arbore?")
print(p2.same_tree(q2))

p3 = TreeNode(1,
              TreeNode(2, TreeNode(5), TreeNode(4)),
              TreeNode(3, TreeNode(6), TreeNode(7)))

q3 = TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3, TreeNode(6), TreeNode(7)))

print("Are p3 and q3 the same tree?")
print(p3.same_tree(q3))