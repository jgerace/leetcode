"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Constraints:

    1 <= secret.length, guess.length <= 1000
    secret.length == guess.length
    secret and guess consist of digits only.
"""
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        print("*****", secret, guess)
        letter_counts_secret = Counter(secret)
        letter_counts_guess = Counter(guess)

        bulls = 0
        cows = 0
        print("counts:", letter_counts_secret, letter_counts_guess)
        print("looking for bulls")
        for idx in range(len(guess)):
            letter = guess[idx]
            if secret[idx] == guess[idx]:
                print("  found bull", letter)
                bulls += 1
                letter_counts_secret[letter] -= 1
                letter_counts_guess[letter] -= 1
        print("counts:", letter_counts_secret, letter_counts_guess)
        print("looking for cows")
        for letter, count in letter_counts_guess.items():
            print("  guess: ", letter, count)
            if letter_counts_secret[letter] > 0 and letter_counts_guess[letter] > 0:
                print("  found cow", letter, letter_counts_secret[letter])
                num_matching_letters = min(letter_counts_secret[letter], letter_counts_guess[letter])
                cows += num_matching_letters
                letter_counts_secret[letter] -= num_matching_letters
                letter_counts_guess[letter] -= num_matching_letters

        print(f"{bulls}A{cows}B")
        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    output = Solution().getHint(secret="1807", guess="7810")
    assert output == "1A3B"

    output = Solution().getHint(secret="1123", guess="0111")
    assert output == "1A1B"

    output = Solution().getHint(secret="1122", guess="1222")
    assert output == "3A0B"

    output = Solution().getHint(secret="1122", guess="2211")
    assert output == "0A4B"
