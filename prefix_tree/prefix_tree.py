# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
# in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
# and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix
# prefix, and false otherwise.

# Вспомогательный класс для хранения узла node
class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = self.get_node()

    @staticmethod
    def get_node():
        return TrieNode()

    @staticmethod
    def char_to_index(char):
        # проверяем, есть ли символ
        return ord(char) - ord('a')

    # метод для длобавления нового слова
    def insert(self, word: str) -> None:
        node = self.root
        for level in range(len(word)):
            index = self.char_to_index(word[level])
            # если текущий символ не существует
            if not node.children[index]:
                node.children[index] = self.get_node()
            node = node.children[index]
        # помечаем последний узел как лист, то есть конец слова
        node.is_end = True

    # метод для поиска слова
    def search(self, word: str) -> bool:
        node = self.go(word)
        if node is False:
            return False
        else:
            return node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.go(prefix) is not False

    # метод для продвижения по слову, если оно существует
    def go(self, word):
        node = self.root
        for level in range(len(word)):
            index = self.char_to_index(word[level])
            if node.children[index]:
                node = node.children[index]
            else:
                return False
        return node


if __name__ == '__main__':
    # Input
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    # Output
    # [null, null, true, false, true, null, true]

    obj = Trie()
    obj.insert("apple")
    param_1 = obj.search('apple')
    print(param_1)                   # return True
    param_2 = obj.search("app")
    print(param_2)                   # return False
    param_3 = obj.startsWith("app")
    print(param_3)                   # return True
    obj.insert("app")
    param_4 = obj.search('app')      # return True
    print(param_4)

