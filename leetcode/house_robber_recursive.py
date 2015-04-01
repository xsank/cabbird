class Solution:

    def memo(func):
        dic={}
        def decorate(self,*args):
            key=len(*args)
            if key not in dic:
                dic[key]=func(self,*args)
            return dic[key]
        return decorate

    @memo
    def rob(self,num):
        length=len(num)
        if length==0:
            return 0
        if length<=2:
            return max(num)
        return max(self.rob(num[:-1]),num[-1]+self.rob(num[:-2]))


if __name__=="__main__":
    print Solution().rob([1])
