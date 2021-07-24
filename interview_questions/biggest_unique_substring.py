class Solution:
    def biggest_unique_substring(self, input: str) -> str:

        from typing import Set, Dict
        
        dict_res = Dict()
        res = Set()
        before,after = 0 
        max_substring = ""
        for before  in range(len(input)):

            if input[before] not in dict_res.keys():
                dict_res[input[before]] = before
                max_substring = "".join(dict_res.keys())
                print (max_substring)
            else:
                index = dict_res[input[before]]
                


            



        return None




if __name__ == '__main__':
    s = Solution()
    print (s.biggest_unique_substring('abcabcda'))