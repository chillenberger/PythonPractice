# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
         return bin(int(a,2)+int(b,2))[2:]

    def addOct(a: str, b: str) -> str:
        return oct(int(a,8)+int(b,8))[2:]

    def addHex(a: str, b: str) -> str:
        return hex(int(a, 16)+int(b,16))[2:]

if __name__ == '__main__':
    print(Solution.addBinary('11', '1'))
    print(Solution.addOct('11', '7'))
    print(Solution.addHex('1c', '24'))
