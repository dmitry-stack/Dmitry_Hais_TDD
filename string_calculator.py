import re

class StringCalculator:

    def Calculate(self, arg: str) -> int:
        if arg == "":
            return 0

        delimiters = [",", "\n"]

        if arg.startswith("//"):
            header, arg = arg.split("\n", 1)

            delimiter_part = header[2:]

            if delimiter_part.startswith("["):
                delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            else:
                delimiters = [delimiter_part]

        pattern = "|".join(map(re.escape, delimiters))
        numbers = [int(n) for n in re.split(pattern, arg) if n]

        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise Exception(f"Negatives not allowed: {negatives}")

        numbers = [n for n in numbers if n <= 1000]

        return sum(numbers)