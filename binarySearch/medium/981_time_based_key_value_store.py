"""
LeetCode 981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Difficulty: Medium

Problem:
Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value 
at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with 
  the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was 
  called previously, with timestamp_prev <= timestamp. If there are multiple 
  such values, it returns the value associated with the largest timestamp_prev. 
  If there are no values, it returns "".

Example:
    Input:
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output:
    [null, null, "bar", "bar", null, "bar2", "bar2"]

    Explanation:
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", no value with timestamp 3, but 1 <= 3
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"
"""


class TimeMap:
    def __init__(self):
        # TODO: Implement your solution here
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # TODO: Implement your solution here
        pass

    def get(self, key: str, timestamp: int) -> str:
        # TODO: Implement your solution here
        pass


def main():
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(f"Test 1: {timeMap.get('foo', 1)}")  # Expected: "bar"
    print(f"Test 2: {timeMap.get('foo', 3)}")  # Expected: "bar"
    timeMap.set("foo", "bar2", 4)
    print(f"Test 3: {timeMap.get('foo', 4)}")  # Expected: "bar2"
    print(f"Test 4: {timeMap.get('foo', 5)}")  # Expected: "bar2"


if __name__ == "__main__":
    main()
