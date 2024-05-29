"""
Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

    If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV

Constraints:

    1 <= num <= 3999
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        output = ""
        remaining = num
        keys = list(values.keys())
        while remaining > 0:
            digit = int(str(remaining)[0])

            # get symbol with max value that can be subtracted from the input
            # can abstract into a helper func
            maxVal = 0
            maxValIdx = 0
            for ii in range(len(keys) - 1, -1, -1):
                if remaining >= keys[ii]:
                    maxVal = keys[ii]
                    maxValIdx = ii
                    break

            if digit == 4:
                # maxVal will begin w/ 1 (1, 10, 100)
                # represent digit with this corresponding letter (I, X, C) + the one greater
                output += values[maxVal] + values[keys[maxValIdx+1]]
                remaining -= digit * maxVal
            elif digit == 9:
                # maxVal will begin w/ 5 (5, 50, 500)
                # represent digit with a letter corresponding to a number beginning w/ 1 (I, X, C)
                # which is in the values list in the index 1 lower than the index of maxVal
                # and the number greater than this digit (X, C, M) in the index 1 higher than maxVal
                output += values[keys[maxValIdx-1]] + values[keys[maxValIdx+1]]
                remaining -= digit * keys[maxValIdx-1]
            else:
                output += values[maxVal]
                remaining -= maxVal

        return output


if __name__ == '__main__':
    output = Solution().intToRoman(3749)
    assert output == "MMMDCCXLIX"

    output = Solution().intToRoman(58)
    assert output == "LVIII"

    output = Solution().intToRoman(1994)
    assert output == "MCMXCIV"

    output = Solution().intToRoman(4)
    assert output == "IV"

    output = Solution().intToRoman(9)
    assert output == "IX"

    output = Solution().intToRoman(99)
    assert output == "XCIX"
