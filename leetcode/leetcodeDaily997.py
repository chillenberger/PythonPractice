# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

import unittest

class Solution:
    @staticmethod
    def trustsEdges(trust):
        trustDict = {}
        for x,y in trust: 
            if trustDict.get(x):
                trustDict[x].append(y)
            else:
                 trustDict[x] = [y]
        return trustDict
    
    @staticmethod
    def trustedEdges(trust):
        trustDict = {}
        for x, y in trust: 
            if trustDict.get(y):
                trustDict[y].append(x)
            else:
                 trustDict[y] = [x]
        return trustDict

    @staticmethod
    def findJudge(n: int, trust: list[list[int]]) -> int:
        if len(trust) == 0 and n ==1:
            return 1
        trusts = Solution.trustsEdges(trust)
        trustedBy = Solution.trustedEdges(trust)
        for person, t in trustedBy.items():
            if len(t) == n-1 and person not in trusts.keys():
                return person 
        return -1
    

class myTest(unittest.TestCase):

    def test_find_judge_one_person_judge(self):
        self.assertEqual(Solution.findJudge(1, []), 1)


    def test_find_judge_two_people(self):
        self.assertEqual(Solution.findJudge(2, [[1, 2]]), 2)

    def test_find_judge_20_peope(self):
        self.assertEqual(Solution.findJudge(21, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21]]), -1)

    def test2(self):
        self.assertEqual(Solution.findJudge(2, [[1, 2]]), 2)

class myTest2(unittest.TestCase): 

    def test_find_judge_one_person_judge(self):
        self.assertEqual(Solution.findJudge(1, []), 1)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(myTest))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(myTest2))
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(suite())
    runner.run(suite2())