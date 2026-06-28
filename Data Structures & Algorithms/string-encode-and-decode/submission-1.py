class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        length = len(s)
        i = 0
        decodedStr = []

        while i < length:
            j = i
            while s[j] != "#":
                j += 1
            
            lenStr = int(s[i:j])

            startInd = j + 1
            endInd = startInd + lenStr

            decodedStr.append(s[startInd: endInd])
            i = endInd

        return decodedStr