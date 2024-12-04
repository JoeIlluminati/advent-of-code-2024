from itertools import chain
import argparse
import re

def main(input_file: str, part: int) -> int:
    memory = ""
    with open(input_file, "r") as f:
        memory = f.read()

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    if part == 1:
        answer = sum([int(a)*int(b) for a,b in re.findall(mul_pattern, memory)])
        return answer

    elif part == 2:
        do_pattern = r"do\(\)"
        dont_pattern = r"don't\(\)"
        do_splits = re.split(do_pattern, memory)
        donts_removed = [re.split(dont_pattern, split, maxsplit=1)[0] for split in do_splits]
        mul_calls = chain(*[re.findall(mul_pattern, split) for split in donts_removed])
        answer = sum([int(a)*int(b) for a,b in mul_calls])
        return answer

    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--part", type=int, required=True, choices=(1,2))
    args = parser.parse_args()
    answer = main(**vars(args))
    print(answer)
