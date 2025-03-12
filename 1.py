from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for countWordsWithSuffix: pattern = {pattern} must be a string"
            )

        def _count_words_with_suffix(pattern, node, index, count):
            if node.value is not None:
                if index == len(pattern):
                    return count + 1
                else:
                    return count
            for char, next_node in node.children.items():
                if index == len(pattern):
                    index = 0
                if char == pattern[index]:
                    index += 1
                count = _count_words_with_suffix(pattern, next_node, index, count)
                index = 0

            return count

        return _count_words_with_suffix(pattern, self.root, 0, 0)

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(
                f"Illegal argument for hasPrefix: prefix = {prefix} must be a non-empty string"
            )

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
