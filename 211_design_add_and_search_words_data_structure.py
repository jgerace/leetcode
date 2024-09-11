"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 10^4 calls will be made to addWord and search.
"""
from collections import deque
# TODO

class WordDictionary:
    class Node:
        def __init__(self, children: dict, word_end=False):
            self.children = children
            self.word_end = word_end

    def __init__(self):
        self.root = self.Node(children={})

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            child_node = cur_node.children.get(char)
            if not child_node:
                new_node = self.Node(children={})
                cur_node.children[char] = new_node
                cur_node = new_node
            else:
                cur_node = child_node
        cur_node.word_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index) -> bool:
            if index >= len(word):
                return False

            char = word[index]
            print("looking at char", char)
            if char == ".":
                if index == len(word)-1 and len(node.children) > 0:
                    return True
                for _, next in node.children.items():
                    if dfs(next, index+1):
                        return True
            else:
                next = node.children.get(char)
                if not next:
                    return False
                elif index == len(word) - 1:
                    return next.word_end
                return dfs(next, index+1)
            return False

        print("*****")
        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("a")
    assert wd.search(".") is True
    assert wd.search("a") is True
    assert wd.search("aa") is False
    assert wd.search("a") is True
    assert wd.search(".a") is False
    assert wd.search("a.") is False

    wd = WordDictionary()
    wd.addWord("at")
    wd.addWord("and")
    wd.addWord("an")
    wd.addWord("add")
    assert wd.search("a") is False
    assert wd.search(".at") is False
    wd.addWord("bat")
    assert wd.search(".at") is True
    assert wd.search("an.") is True
    assert wd.search("a.d.") is False
    assert wd.search("b.") is False
    assert wd.search("a.d") is True
    assert wd.search(".") is False
