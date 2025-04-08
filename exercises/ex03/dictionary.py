"""An introduction to dictionaries"""

__author__: str = "730552953"


def invert(dict_initial: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    for key in dict_initial:
        value = dict_initial[key]
        if value in invert_dict:
            raise KeyError
        invert_dict[value] = key
    return invert_dict


def count(inputlist: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(inputlist):
        if inputlist[idx] in count_dict:
            count_dict[inputlist[idx]] += 1
            idx += 1
        else:
            count_dict[inputlist[idx]] = 0
    return count_dict


def favorite_color(namefavorite: dict[str, str]) -> str:
    color_list: list[str] = list(namefavorite.values())
    colornumber: dict[str, int] = count(color_list)
    max_number: int = max(colornumber.values())
    for key in colornumber:
        if colornumber[key] == max_number:
            return key


def bin_len(binlist: list[str]) -> dict[int, set[str]]:
    idx: int = 0
    bins: dict[int, set[str]] = {}
    while idx < len(binlist):
        if len(binlist[idx]) not in bins:
            bins[len(binlist[idx])] = {binlist[idx]}
        else:
            bins[len(binlist[idx])].add(binlist[idx])
        idx += 1
    return bins
