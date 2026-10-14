class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strings = ""
        for strings in strs:
            encoded_strings += f"{len(strings)}:{strings}"
        return encoded_strings

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = s.find(":",i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decoded_strings.append(s[start:end])
            i=end
        return decoded_strings