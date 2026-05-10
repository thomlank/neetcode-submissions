from typing import List
def get_key(target):
    if type(target) != int:
        return len(target)
    else:
        return abs(target)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = get_key, reverse = True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = get_key)
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
