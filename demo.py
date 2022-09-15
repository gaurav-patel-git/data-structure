# Python3 program to find longest consecutive
# sequence in binary tree

# A utility class to create a node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def longestConsecutiveUtil(root, curLength,
                        expected, res):
    if (root == None):
        return

    if (root.data == expected+1 or root.data == expected-1):
        res[0] += 1 

    longestConsecutiveUtil(root.left, curLength,
                        root.data , res)
    longestConsecutiveUtil(root.right, curLength,
                        root.data , res)


def longestConsecutive(root):
    if (root == None):
        return 0

    res = [0]

    longestConsecutiveUtil(root, 0, root.data, res)

    return res[0]

# Driver Code
if __name__ == '__main__':

    root = newNode(16)
    root.left = newNode(7)
    root.left.left = newNode(8)
    root.right = newNode(7)
    root.right.right = newNode(8)


    print(longestConsecutive(root))

# This code is contributed by PranchalK
