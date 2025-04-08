"""Test file for dictionary"""

__author__: str = "730552953"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert1() -> None:
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "c": "d", "f": "e"}


def test_invert2() -> None:
    assert invert({"happy": "sad", "good": "evil", "peace": "war"}) == {
        "sad": "happy",
        "evil": "good",
        "war": "peace",
    }


def test_invert3() -> None:
    assert invert({"1": "2"}) == {"2": "1"}


def test_count1() -> None:
    assert count(["apple", "apple", "apple", "banana", "banana", "peach"]) == {
        "apple": 3,
        "banana": 2,
        "peach": 1,
    }


def test_count2() -> None:
    assert count(["apple", "peach"]) == {"apple": 1, "peach": 1}


def test_count3() -> None:
    assert count(["apple"]) == {"apple": 1}


def test_favorite_color1() -> None:
    assert favorite_color({"james": "green", "juan": "blue", "jan": "green"}) == "green"


def test_favorite_color2() -> None:
    assert (
        favorite_color(
            {"james": "yellow", "jan": "yellow,", "thomas": "green", "lily": "blue"}
        )
        == "yellow"
    )


def test_favorite_color3() -> None:
    assert favorite_color({"james": "green"}) == "green"


def test_bin_len1() -> None:
    assert bin_len(["de", "meisje", "is", "totaal", "gek"]) == {
        2: {"de", "is"},
        6: {"meisje", "is"},
        3: {"gek"},
    }


def test_bin_len2() -> None:
    assert bin_len(["jongen"]) == {6: {"jongen"}}


def test_bin_len3() -> None:
    assert bin_len(["j"]) == {1: {"j"}}
