import argparse
import bisect
from collections import Counter

def main(input_file: str, part: int) -> int:
    left_list = []
    right_list = []
    with open(input_file, "r") as f:
        for line in f:
            left, right = line.split()
            bisect.insort(left_list, int(left))
            bisect.insort(right_list, int(right))

    if part == 1:
        answer = 0
        for left, right in zip(left_list, right_list):
            answer += abs(left - right)
        return answer
    elif part == 2:
        right_item_counts = Counter(right_list)
        answer = 0
        for item in left_list:
            answer += item * right_item_counts[item]
        return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--part", type=int, required=True, choices=(1, 2))
    args = parser.parse_args()
    answer = main(**vars(args))
    print(answer)
