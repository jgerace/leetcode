class Trie:
    class Node:
        def __init__(self, children: dict, word_end: bool = False):
            self.children = children
            self.word_end = word_end

    def __init__(self):
        self.root = self.Node(children={})
        return

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            letter_node = cur_node.children.get(char)
            if letter_node:
                cur_node = letter_node
            else:
                new_node = self.Node(children={}, word_end=False)
                cur_node.children[char] = new_node
                cur_node = new_node
        cur_node.word_end = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for letter in word:
            letter_node = cur_node.children.get(letter)
            if letter_node:
                cur_node = letter_node
            else:
                return False
        return cur_node.word_end

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for letter in prefix:
            letter_node = cur_node.children.get(letter)
            if letter_node:
                cur_node = letter_node
            else:
                return False
        return True
