class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = {"a":".-",
                    "b":"-...",
                    "c":"-.-.",
                    "d":"-..",
                    "e":".",
                    "f":"..-.",
                    "g":"--.",
                    "h":"....",
                    "i":"..",
                    "j":".---",
                    "k":"-.-",
                    "l":".-..",
                    "m":"--",
                    "n":"-.",
                    "o":"---",
                    "p":".--.",
                    "q":"--.-",
                    "r":".-.",
                    "s":"...",
                    "t":"-",
                    "u":"..-",
                    "v":"...-",
                    "w":".--",
                    "x":"-..-",
                    "y":"-.--",
                    "z":"--.."}
        result = []
        for i in words:
            string = ''
            for j in i:
                string+=alphabet[j]
            result.append(string)
        result = set(result)
        return len(result)