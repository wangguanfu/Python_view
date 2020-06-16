"""
split  upper  reverse

翻转子字符串


回文数



"""

# 翻转
class Solution:
    def reverseStr(self, s):
        ben = 0
        end = len(s)
        while ben < end:
            s[ben], s[end] = s[end], s[ben]
            ben += 1
            end -= 1



# 回文数
class Solution1:
    def isPalindrome(self, x):
        if x < 0: return False

        s = str(x)
        ben = 0
        end = len(s) - 1

        while ben < end:
            if s[ben] == s[end]:
                ben += 1
                end -= 1
            else:
                return False
        return True


def test():
    s = Solution1()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-1) is True
    assert s.isPalindrome(1) is True




















