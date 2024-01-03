class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count=0
        row=0
        while row<len(bank)-1:
            if '1' in bank[row]:
                    j=row+1
                    while j<len(bank) and  '1' not in bank[j]:
                        j+=1
                    if j<len(bank):
                        count+=  list(bank[row]).count('1')*list(bank[j]).count('1')               
                    row=j
            else:
                row+=1
        return count