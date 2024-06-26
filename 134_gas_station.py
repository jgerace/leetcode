"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:

    n == gas.length == cost.length
    1 <= n <= 105
    0 <= gas[i], cost[i] <= 104
"""
from typing import List


class Solution:
    def bruteForce(self, gas: List[int], cost: List[int]) -> int:
        # O(n^2)
        numStations = len(gas)
        for startIdx in range(numStations):
            totalGas = 0
            stationIdx = startIdx
            for ii in range(numStations):
                idx = (stationIdx + ii) % numStations
                totalGas += gas[idx] - cost[idx]
                if totalGas < 0:
                    break
            if totalGas >= 0:
                return stationIdx
        return -1

    def savesies(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # By this point we KNOW there is a unique answer because the problem guarantees it
        totalGas = 0
        startingStation = 0
        for idx in range(len(gas)):
            totalGas += gas[idx] - cost[idx]
            if totalGas < 0:
                totalGas = 0
                startingStation += 1

        # If we get to the end of the for loop and totalGas is non-negative, then we know that totalGas
        # is at least as large as the amount used from the given startingStation and larger than the amount
        # of gas used in all previous stations. Since we know there is only one answer, this must be it.
        return startingStation

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        starting_station = 0
        total_gas = 0
        for idx in range(len(gas)):
            total_gas += gas[idx]
            if total_gas - cost[idx] < 0:
                starting_station = idx + 1
                total_gas = 0
            else:
                total_gas -= cost[idx]

        return starting_station


if __name__ == '__main__':
    output = Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
    assert output == 3

    output = Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3])
    assert output == -1

    output = Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1])
    assert output == 4

    output = Solution().canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2])
    assert output == 0
