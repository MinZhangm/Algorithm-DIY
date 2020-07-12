# 新的数据类型,快速检索字符串
# 空间换时间
# leetcode-208

# 创建一个多叉输的类
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root

        for s in word:

            root = root.children[s]
        root.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for s in word:
            if s not in root.children:
                return False
            root = root.children[s]
        return root.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for s in prefix:
            if s not in root.children:
                return False
            root = root.children[s]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
