class TreeNode():
    def __init__(self,value,children):
        self.value = value
        self.children = children
class BKTree():
    def __init__(self,maxEditNum):
        self.root = None   
        self.maxEditNum = maxEditNum
    def insert(self,word):
        if not self.root:
            self.root = TreeNode(word,{})
            return
        current = self.root
        while True:
            parentWord = current.value
            editDis = self._editDistance(parentWord,word)
            childrenNodes = current.children
            if editDis not in childrenNodes:
                childrenNodes[editDis] = TreeNode(word,{})
                break
            else:
                current = childrenNodes[editDis]

    def suggest(self,word):
        suggestions = []
        if not self.root:
            return suggestions
        stack = [self.root]
        while stack:
            current = stack.pop()
            parentValue = current.value
            childrenWords = current.children
            editDis = self._editDistance(word,parentValue)
            if editDis <= self.maxEditNum:
                suggestions.append(parentValue)
            if childrenWords:
                minVal = editDis-self.maxEditNum
                maxVal = editDis + self.maxEditNum
                for x in range(minVal,maxVal+1):
                    if x in childrenWords:
                        stack.append(childrenWords[x])
        return suggestions
    def _editDistance(self,word,other):
        print(word)
        print(other)
        matrix = [[0 for _ in range(0,len(other)+1)] for _ in range(0,len(word)+1)]
        for x in range(0,len(word)+1):
            for y in range(0,len(other)+1):
                if min(x,y) == 0:
                    matrix[x][y] = max(x,y)
                else:
                    option1 = matrix[x-1][y] + 1
                    option2 = matrix[x][y-1] + 1
                    added = 0 if (word[x-1] == other[y-1]) else 1
                    option3 = matrix[x-1][y-1]+added
                    matrix[x][y] = min(option1,option2,option3)
        print(matrix[-1][-1])
        return matrix[-1][-1]
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("  " * level + str(node.value))
        for child in node.children.values():
            self.print_tree(child, level + 1)

if __name__ == "__main__":
    spellingTree = BKTree(1)
    spellingTree.insert("banana")
    spellingTree.insert("grapes")
    spellingTree.insert("apple")
    spellingTree.insert("bannana")
    spellingTree.insert("graps")
    spellingTree.insert("aple")
    spellingTree.insert("cake")
    spellingTree.insert("book")
    spellingTree.insert("books")
    spellingTree.print_tree()
