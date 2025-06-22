# Create your own node object, which has a hashmap (for easy lookup) and an endOfWord boolean to check if its a word stored in the Trie

class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    
    # Initialise a root node called self.root which we can use to start the operations.

    def __init__(self):
        self.root = TreeNode()
    

    # We set curr to root node then check if the characters are in the children (going down tree), if not, we add them in place and finally set the last character
    # to the end of the word
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.endOfWord = True  

    # Similar process, set root node but if c isnt in children we return false and if it makes its way to the end of the string we return the 'end of word' bool
    # The reason we return this and not a simple True is because you could have a word like applet and searching apple would result in a True statement
    # However, apple is not in the tree, but applet is, so we return the endOfWord, if apple has been inserted into the tree itself then it will have returned True
    # else False
    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
    
    # This is similar to the others, we basically loop through the prefix and if c isn't in children we simply return False

    def startsWith(self, prefix):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)