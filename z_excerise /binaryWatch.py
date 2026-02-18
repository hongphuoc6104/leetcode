from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range (12):
            for j in range (60):
                if (bin(i).count("1") + bin(j).count("1")) == turnedOn:
                    res.append(str(i) + ":" + str(j).zfill(2))
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.readBinaryWatch(1))
        