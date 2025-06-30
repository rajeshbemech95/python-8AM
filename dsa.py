
# # # stack = []

# # # stack.append("a")
# # # stack.append("b")
# # # stack.append("c")
# # # stack.append("d")
# # # print(stack)

# # # print(stack.pop())
# # # print(stack)
# # # # print(stack[-1])

# # # from collections import deque

# # # q = deque()

# # # q.append("A")
# # # q.append("B")
# # # q.append("c")
# # # q.append("d")
# # # # A,B,C,D
# # # print(q)
# # # print(q.popleft())
# # # print(q)


# # # q = [1,2,3]
# # # for i in q:
# # #     i = i
# # # -1

# # # a =None

# # # class Node:
# # #     def __init__(self,data):
# # #         self.data = data
# # #         self.next = None
        
# # # class LinkedList:
# # #     def __init__(self):
# # #         self.head = None
        
# # #     def append(self, data):
# # #         new_node = Node(data)
# # #         self.head = new_node
        
        
# # #         last = last.next
# # #         last.next = new_node
        
        

# # class Node:
# #     def __init__(self,url):
        
# #         self.url = url
# #         self.next = None
        
# # class BrowserHistory:
# #     def __init__(self):
# #         self.head = None
        
# #     def visit(self,url):
# #         new_node = Node(url)
# #         if not self.head:
# #             self.head = new_node
# #         else:
# #             curr = self.head
# #             while curr.next:
# #                 curr = curr.next
# #             curr.next = new_node
            
# #     def show_history(self):
# #         curr = self.head
# #         while curr:
# #             print("url visited", curr.url)
# #             curr = curr.next
            
            
# # # history = BrowserHistory()
# # # history.visit("googl.com")
# # # history.visit("google.com")
# # # history.visit("googel.com")
# # # history.visit("gooegl.com")

# # # history.show_history()
        
# # person= {
# #     "name" : "name1",
# #     "age" : 30
# #  }

# # print(person["name"])

# # person["email"] = "exmple@python.com"



# # def count_data(words):
# #     data = {}
# #     for word in words:
# #         if word in data:
# #             data[word] += 1
            
# #         else:
# #            data[word] = 1
# #     return data      
            
# # words = ["apple", "orange","banana","apple","grapes","orange","orange"]         
# # res = count_data(words)
# # # print(res)
    
    
# # # 4 = 4 * 3*2*1     
# # # n * n-1      
# #         # 20 60 120
# # def factorials(n):
    
# #     if n == 0:
# #         return 1
    
# #     else :
# #         return n * factorials(n-1)
    
    
# # print(factorials(5))
    
    
# class TreeNode:
#     def __init__(self,name, is_file=False):
#         self.name = name
#         self.is_file = is_file
#         self.children = []
        
#     def add_child(self, child):
#         self.children.append(child)
        
#     def print_tree(self, level=0):
#         intent = " " * level
        
#         print(f"{intent}{"[FILE]" if self.is_file else "[DIR]"} {self.name}")
        
#         for child in self.children:
#             child.print_tree(level + 1)
        
# root = TreeNode("root")

# docs = TreeNode("Documents")
# music = TreeNode("Music")
# pics = TreeNode("Pictures")

# file1 = TreeNode("example.pdf",is_file=True)
# file2 = TreeNode("sample.txt",is_file=True)
# file3 = TreeNode("song.mp3",is_file=True)

# root.add_child(docs)
# root.add_child(music)
# root.add_child(pics)

# docs.add_child(file1)
# music.add_child(file3)
# pics.add_child(file2)

# root.print_tree()

text = "red,blue,green,orange,yellow"
text= u"hello123"
# text = input("enter value")
# print(text.find("l"))
# print(text.replace("e", "o"))
# print(text.strip())
# print(text.split(","))
# print(text.isdigit())
# print(r"input string is{text} given by user{text}")
print(text)
print(type(text))





