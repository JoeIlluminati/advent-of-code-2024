import argparse
from itertools import pairwise

def check_is_safe(report: list[int]) -> bool:
    differences = [b-a for a,b in pairwise(report)]

    in_bounds = all(-3 <= diff <= 3 for diff in differences)
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all( diff < 0 for diff in differences)

    return in_bounds and (all_increasing or all_decreasing)


def check_if_safe_with_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        if check_is_safe(dampened_report):
            return True
    return False


def main(input_file: str, part: int) -> int:
    with open(input_file, "r") as f:
            safe_reports = 0
            for line in f:
                report = [int(level) for level in line.split()]
                is_safe = check_is_safe([int(level) for level in line.split()])
                if is_safe:
                    safe_reports += 1
                elif part == 2:
                    is_actually_safe = check_if_safe_with_dampener(report)
                    if is_actually_safe:
                        safe_reports += 1
            return safe_reports
    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--part", type=int, required=True, choices=(1,2))
    args = parser.parse_args()
    answer = main(**vars(args))
    print(answer)
