class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        not_equal = []
        sets = []
        
        for eq in equations:
            if '!=' in eq:
                not_equal.append(eq)
            else:
                a, b = eq.split('==')
                sets.append(set([a, b]))

        idx = 0

        while idx < len(sets):
            temp_set = sets[idx]
            to_remove = []

            for inner in range(idx + 1, len(sets)):
                if len(temp_set & sets[inner]) > 0:
                    temp_set.update(sets[inner])
                    to_remove.append(sets[inner])

            for r in to_remove:
                sets.remove(r)

            idx += 1

        for neq in not_equal:
            a, b = neq.split('!=')

            if a == b:
                return False

            for s in sets:
                if a in s and b in s:
                    return False

        return True


sol = Solution()
# e = ["a==b","b!=a"]
# e = ["b==a","a==b"]
# e = ["a==b","b==c","a==c"]
# e = ["a==b","b!=c","c==a"]
# e = ["c==c","b==d","x!=z"]
# e = ["a==b","b!=c","c==a"]
# e = ["e!=c","b!=a","e==d"]
# e = ["f==a","a==b","f!=e","b!=b","a==c","b==e","c==f"]
e = ["v!=l","i!=g","m==n","s==w","c!=f","h==l","e==q","r==s","q!=l","c!=m","m!=q","r!=x","x!=f","q!=x","w==u","b!=p","u==w","e!=v","y!=m","i!=f","r!=y","c!=l","b!=h","k==p","p!=c","t==v","j!=o","b!=x","p!=u","r!=w"]
print(sol.equationsPossible(e))
        