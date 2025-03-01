message = "C'est mon premier script !!!"
print(message)


je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))


import unittest
from typing import List

def count_names_with_more_than_seven_letters(names: List[str]) -> int:
    """
    Count the number of names that have more than seven letters.

    Parameters:
    - names (List[str]): A list of names (strings).

    Returns:
    - int: The number of names that have more than seven letters.
    """
    threshold_length = 7
    count = 0
    for name in names:
        if len(name) > threshold_length:
            print(f"{name} est un prénom avec un nombre de lettres supérieur à {threshold_length}")
            count += 1
        else:
            print(f"{name} est un prénom avec un nombre de lettres inférieur ou égal à {threshold_length}")
    return count

class TestNamesMethod(unittest.TestCase):
    def test_count_names_with_more_than_seven_letters(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_with_more_than_seven_letters(names_list)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
