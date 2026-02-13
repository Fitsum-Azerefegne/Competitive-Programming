class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1: "I",
            5: "V", 
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4 : "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }
        res = ""
        num_str = str(num)
        for i, digit in enumerate(num_str):
            place_value = 10 ** (len(num_str) - i - 1) 
            one_digit = int(digit) * place_value
            if one_digit in roman_map:
                res += roman_map[one_digit]
            else:
                while one_digit > 0:
                    largest_smaller = max(key for key in roman_map.keys() if key <= one_digit)
                    res += roman_map[largest_smaller]
                    one_digit -= largest_smaller
        return res






