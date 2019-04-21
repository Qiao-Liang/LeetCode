from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def recurse(idx, bound, times):
            dic = defaultdict(int)
            sub_formulas = []

            while idx < bound:
                if formula[idx].isalpha() and formula[idx].isupper():
                    alpha_idx = idx + 1

                    while alpha_idx < bound and formula[alpha_idx].isalpha() and formula[alpha_idx].islower():
                        alpha_idx += 1

                    atom = formula[idx: alpha_idx]
                    digit_idx = alpha_idx
                    
                    while digit_idx < bound and formula[digit_idx].isdigit():
                        digit_idx += 1

                    dic[atom] += (1 if alpha_idx == digit_idx else int(formula[alpha_idx: digit_idx])) * times
                    idx = digit_idx
                elif formula[idx] == "(":
                    stack = ["("]
                    left_idx = right_idx = idx + 1

                    while stack:
                        if formula[right_idx] == "(":
                            stack.append("(")
                        elif formula[right_idx] == ")":
                            stack.pop()
                        
                        right_idx += 1

                    digit_idx = right_idx

                    while digit_idx < bound and formula[digit_idx].isdigit():
                        digit_idx += 1

                    sub_formulas.append(((left_idx, right_idx - 1, 1 if digit_idx == right_idx else int(formula[right_idx: digit_idx]))))
                    idx = digit_idx

            for left, right, sub_times in sub_formulas:
                temp = recurse(left, right, sub_times)

                for key, val in temp.items():
                    dic[key] += val * times
                
            return dic

        dic = recurse(0, len(formula), 1)
        atoms = sorted(dic.keys())
        return ''.join([atom + str(dic[atom]) if dic[atom] > 1 else atom for atom in atoms])


sol = Solution()
# formula = "Mg(OH)2"
# formula = "H2O"
formula = "K4(ON(SO3)2)2"
print(sol.countOfAtoms(formula))
