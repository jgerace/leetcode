"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Trie:
    class Node:
        def __init__(self, children: dict, word_end: bool = False):
            self.children = children
            self.word_end = word_end

    def __init__(self):
        self.root = self.Node(children={})
        return

    def insert(self, word: str) -> None:
        print("inserting:", word)
        cur_node = self.root
        for char in word:
            letter_node = cur_node.children.get(char)
            if letter_node:
                print("  found letter:", char)
                cur_node = letter_node
            else:
                print(" adding:", char)
                new_node = self.Node(children={}, word_end=False)
                cur_node.children[char] = new_node
                cur_node = new_node
        print(" setting word_end")
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


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("apple") is True
