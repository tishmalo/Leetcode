class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #check the situation-only two exceptions
        #1. When 9 is last number
        #[1, 2, 9]=> [1, 3, 9]

        #2 when subsequent numbers are 9
        #[1, 9, 9]=>[2,0,0]

        #3 best way to go about this is to transform the array into a       whole     number
        whole_number=int("".join(map(str, digits)))
        #Now add the +1
        whole_number+=1
        #now transform it to array again

        return [int(d) for d in str(whole_number)]
