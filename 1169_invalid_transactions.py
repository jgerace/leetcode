"""
A transaction is possibly invalid if:

    the amount exceeds $1000, or;
    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:

    transactions.length <= 1000
    Each transactions[i] takes the form "{name},{time},{amount},{city}"
    Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
    Each {time} consist of digits, and represent an integer between 0 and 1000.
    Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from collections import defaultdict
from typing import List

from testing import listItemsEqual


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        print("*****")
        fraud_idxs = set()
        name_to_transaction = defaultdict(list)  # name -> (time_int, city, idx)
        for idx, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                fraud_idxs.add(idx)

            prior_transactions = name_to_transaction[name]
            for prior_time, prior_city, prior_idx in prior_transactions:
                if (time - 60 <= prior_time <= time + 60) and prior_city != city:
                    fraud_idxs.add(idx)
                    fraud_idxs.add(prior_idx)
            name_to_transaction[name].append((time, city, idx))

        result = []
        for idx in fraud_idxs:
            result.append(transactions[idx])
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"])
    assert listItemsEqual(output, ["alice,20,800,mtv", "alice,50,100,beijing"])

    output = Solution().invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"])
    assert listItemsEqual(output, ["alice,50,1200,mtv"])

    output = Solution().invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"])
    assert listItemsEqual(output, ["bob,50,1200,mtv"])

    output = Solution().invalidTransactions(["alice,20,1220,mtv", "alice,20,1220,mtv"])
    assert listItemsEqual(output, ["alice,20,1220,mtv", "alice,20,1220,mtv"])

    output = Solution().invalidTransactions(["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"])
    assert listItemsEqual(output, ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"])

    output = Solution().invalidTransactions(
        ["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona", "bob,820,596,bangkok",
         "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"])
    assert listItemsEqual(output, ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"])

    output = Solution().invalidTransactions(
        ["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona", "alex,587,402,bangkok",
         "chalicefy,973,830,barcelona", "alex,932,86,bangkok", "bob,188,989,amsterdam"])
    assert listItemsEqual(output, ["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona"])
