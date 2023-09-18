# https://leetcode.com/problems/hand-of-straights/

class Solution(object):
    
    def isNStraightHandUgly(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        n_groups = len(hand) / groupSize

        rearranged = sorted(hand)
        cards_group = [ groupSize ] * n_groups
        next_group = defaultdict(list)
        last_group = 0
        completed = 0

        for n in rearranged:
            if next_group[n]:
                group = next_group[n].pop()
            else:
                group = last_group
                last_group += 1
            
            if group == n_groups:
                return False

            cards_group[group] -= 1
            if cards_group[group]:
                next_group[n+1].append(group)
            else:
                completed += 1
        
        return completed == n_groups
            

            
        