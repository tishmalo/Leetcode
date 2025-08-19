#Num=[1, 2, 3, 4, 5]
#T=7
#ans=[1, 4]=> index of 1 and 5
#use dictionary to store the index of the elements 
#Nums=[1, 2, 5]
#T=7
#complement=c
#step 1
#dic=[1, 0]=>number and index 
#complement=7-1=6
#6 not present, go to number 2
#step 2
#dic[2, 1]
#complement=7-5=2
#get the index of 5 from the dictionary
#5 is not in dictionary
#step 3
#dic[5, 2]
#complement=7-5=2
#2 is present, return [1, 2] => index of 2 and 5

class solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in dic:
                return [dic[complement], i]
            dic[num]=i
        return []