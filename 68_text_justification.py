"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        # break words into lines
        numLettersOnLine = 0
        numSpacesRequired = 0
        line = []
        for word in words:
            if numLettersOnLine + len(word) + numSpacesRequired <= maxWidth:
                line.append(word)
                numLettersOnLine += len(word)
                numSpacesRequired += 1
            else:
                lines.append(line)
                line = []
                line.append(word)
                numLettersOnLine = len(word)
                numSpacesRequired = 1
        lines.append(line)

        output = []
        # put spaces between words
        print(lines)
        for line in lines[:-1]:
            print(line)
            lineLen = sum(len(word) for word in line)
            numWords = len(line)
            numSpaceGaps = numWords - 1 if numWords > 1 else 1
            numSpacesToFill = maxWidth - lineLen
            spaces = ['' for _ in range(numSpaceGaps)]

            for idx in range(numSpacesToFill):
                spaces[idx % numSpaceGaps] += ' '

            outputString = ''
            for idx in range(numWords):
                outputString += line[idx]
                if idx < len(spaces):
                    outputString += spaces[idx]
            output.append(outputString)

        lastLine = ' '.join(lines[-1])
        lineLen = sum(len(word) for word in lastLine)
        numSpacesToFill = maxWidth - lineLen
        output.append(lastLine + ' ' * numSpacesToFill)

        return output


if __name__ == '__main__':
    output = Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    print(output)
    assert output == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]

    output = Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    assert output == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]

    output = Solution().fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"], 20)
    assert output == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
