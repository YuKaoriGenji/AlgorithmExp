import RBTree
def command(Tree):
    '''
     insert id name start end
     delete id
     del start end
     search all start end
     search one start end
     exit
     '''
 
    while True:
        print("\n")
        command = list(input().split())
        if command[0] == "insert":
            x = RBTree.RBnode(command[1], command[2], float(
                command[3]), float(command[4]))
            Tree.rb_insert(x)
            print("after insert :")
            Tree.inorder_traversal(Tree.root)
            print("\n")
        elif command[0] == "delete":
            delete = []
            Tree.search_id(Tree.root, command[1], delete)
            if len(delete) < 1:
                print("delete error\n")
            else:
                Tree.rb_delete(delete[0])
                print("after delete :")
                Tree.inorder_traversal(Tree.root)
                print("\n")
 
        elif command[0] == "del":
            delete = []
            Tree.search(Tree.root, float(
                command[1]), float(command[2]), delete)
            if len(delete) < 1:
                print("delete error\n")
            else:
                while len(delete) != 0:
                    Tree.rb_delete(delete[-1])
                    delete.pop(-1)
                print("after del:")
                Tree.inorder_traversal(Tree.root)

        elif command[0]=="display":
            Tree.wide_traversal(Tree.root)
        elif command[0] == "search":
            if command[1] == "all":
                all = []
                Tree.search(Tree.root, float(
                    command[2]), float(command[3]), all)
                if len(all) == 0:
                    print("There is no class at this time")
                else:
                    while len(all) != 0:
                        x = all.pop(-1)
                        print("id:{:<4} name:{:<14} start:{:<4} end:{:<4} color:{:<5}".format(
                            x.id, x.name, x.start, x.end, x.color))
 
            if command[1] == "one":
                x = Tree.interval_search(start=float(
                    command[2]), end=float(command[3]))
                if x is not Tree.nil:
                    print("id:{:<4} name:{:<14} start:{:<4} end:{:<4} color:{:<5}".format(
                        x.id, x.name, x.start, x.end, x.color))
                else:
                    print("There is no class at this time")
 
        elif command[0] == "exit":
            exit("Good bye!\n")
        else:
            print("Re-enter,please")
 
 
def main():
    course = {
        "1": ("one", 8, 4),   "2": ("two", 8, 9),
        "3": ("three", 24, 25), "4": ("four", 5, 8),
        "5": ("five", 16, 27),  "6": ("six", 17, 19),
        "7": ("seven", 26, 26), "8": ("eight", 0, 3),
        "9": ("nine", 6, 10),   "10": ("ten", 19, 20)}
 
    Tree = RBTree.RBtree()  # Tree.left.start < Tree.start <= Tree.right.start
    for i in course.keys():
        node = RBTree.RBnode(i, *course[i])
        Tree.rb_insert(node)
    print("\n\n初始树为：")
    Tree.inorder_traversal(Tree.root)
    print("\n\nyou can do :\n insert id name start end \n delete id \n display \n del start end\n search all start end\n search one start end\n exit")
    command(Tree)
 
  
if __name__ == '__main__':
    main()

