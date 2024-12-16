import argparse
from typing import Generator, Tuple

def search(wordsearch: list[str], tuple_size: int = 4) -> Generator[str, None, None]:
    length = len(wordsearch)
    width = len(wordsearch[0])

    # horizontal
    for i in range(length - tuple_size + 1):
        for j in range(width):
            word = "".join([wordsearch[j][i+k] for k in range(tuple_size)])
            yield word
            yield word[::-1]

    # vertical
    for i in range(length):
        for j in range(width - tuple_size + 1):
            word = "".join([wordsearch[j+k][i] for k in range(tuple_size)])
            yield word
            yield word[::-1]

    # diagonal
    for i in range(length - tuple_size + 1):
        for j in range(width - tuple_size + 1):
            word = "".join([wordsearch[i+k][j+k] for k in range(tuple_size)])
            yield word
            yield word[::-1]

    for i in range(length - tuple_size + 1):
        for j in range(tuple_size - 1, width):
            word = "".join([wordsearch[i+k][j-k] for k in range(tuple_size)])
            yield word
            yield word[::-1]


def search_part_2(wordsearch: list[str]) -> Generator[Tuple[str, str], None, None]:
    length = len(wordsearch)
    width = len(wordsearch[0])

    """
    Indices to capture for the diagonals along the X

    --+--+--
    00|  |02
    --+--+--
      |11|
    --+--+--
    20|  |22
    --+--+--
    """
    for i in range(length-2):
        for j in range(width-2):
            diag1 = "".join([wordsearch[i+k][j+k] for k in range(3)])
            diag2 = "".join([wordsearch[i+2-k][j+k] for k in range(3)])
            yield (diag1, diag2)


def main(input_file: str, part: int) -> int:
    wordsearch = []
    with open(input_file, "r") as f:
        wordsearch = [line.strip() for line in f]

    if part == 1:
        found = 0
        for word in search(wordsearch, 4):
            if word == "XMAS":
                found += 1
        return found

    elif part == 2:
        found = 0
        for diag1, diag2 in search_part_2(wordsearch):
            if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
                found += 1
        return found

    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--part", type=int, required=True, choices=(1,2))
    args = parser.parse_args()
    answer = main(**vars(args))
    print(answer)
