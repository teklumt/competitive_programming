class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res=0
        for i in range(len(energy)):  
            if initialEnergy>energy[i] and initialExperience<=experience[i]:
                res+=-initialExperience+experience[i]+1
                initialExperience+=-initialExperience+experience[i]+1
            elif initialEnergy<=energy[i] and initialExperience>experience[i]:
                res+=-initialEnergy+energy[i]+1
                initialEnergy+=-initialEnergy+energy[i]+1
            elif initialEnergy<=energy[i] and initialExperience<=experience[i]:
                res+=-initialExperience+experience[i]+1
                res+=-initialEnergy+energy[i]+1
                initialExperience+=-initialExperience+experience[i]+1
                initialEnergy+=-initialEnergy+energy[i]+1
            initialEnergy-=energy[i]
            initialExperience+=experience[i]
        return res