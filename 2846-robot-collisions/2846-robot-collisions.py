class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        right = []
        nn = []
        inds = [i for i in range(len(positions))]
        new_  = sorted(zip(positions ,directions, healths, inds ))
        for ind, dirs , hel, jj in new_:
            if dirs == 'R':
                right.append((ind, dirs, hel, jj))
            else:
                flag = True
                while right:
                    Tind, Tdir, Thel, nj = right.pop()
                    if Thel > hel:
                        right.append((Tind, Tdir, Thel - 1, nj))
                        flag = False
                        break
                    elif Thel == hel:
                        flag = False
                        break
                    else:
                        hel -= 1
                if flag:
                    nn.append((ind, dirs, hel, jj))
        
        return  [num[-2] for num in sorted(nn + right,key=lambda x:x[-1])]