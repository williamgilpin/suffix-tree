""" Test the maximal repeats function. """

# pylint: disable=missing-docstring

import pytest

from suffix_tree import Tree
from suffix_tree.tree import BUILDERS


@pytest.mark.parametrize("builder", BUILDERS)
class TestMaximalRepeats:
    def maximal_repeats(self, tree, arr, min_cv=2, min_len=2):
        a = []
        for cv, path in sorted(tree.maximal_repeats()):
            if cv >= min_cv and len(path) >= min_len:
                a.append("%d %s" % (cv, str(path)))
        assert a == arr

    def test_maximal_repeats_1(self, builder):
        # See [Gusfield1997]_ §7.12.1, 144ff.
        tree = Tree({"A": "xabxac", "B": "awyawxawxz"}, builder=builder)
        self.maximal_repeats(
            tree,
            [
                "2 x a",
            ],
        )

    def test_maximal_repeats_2(self, builder):
        tree = Tree(
            {
                "A": "1abc2abc3",
                "B": "4abc5abc6",
                "C": "7abc",
                "D": "7abc",
                "E": "abc",
            },
            builder=builder,
        )

        self.maximal_repeats(
            tree,
            [
                "2 7 a b c",
                "5 a b c",
            ],
        )

    def test_maximal_repeats_3(self, builder):
        # pylint: disable=line-too-long
        tree = Tree(
            {
                "berlin-sb-lat-qu-931": ["157", "165", "167", "165"],
                "cava-dei-tirreni-bdb-4": [
                    "232",
                    "020b",
                    "092",
                    "093",
                    "039",
                    "061",
                    "102",
                    "135",
                    "098",
                    "099",
                    "039",
                    "040",
                    "039",
                    "040",
                    "044",
                    "141",
                    "140",
                    "098",
                    "121",
                    "098",
                    "090",
                    "095",
                    "134",
                    "135",
                    "088",
                    "104",
                    "139",
                    "140",
                    "067",
                    "091",
                    "094",
                    "158",
                    "159",
                    "161",
                    "162",
                    "163",
                    "164",
                    "165",
                    "158",
                    "165",
                    "161",
                ],
                "gotha-flb-memb-i-84": [
                    "A000",
                    "176",
                    "039",
                    "040",
                    "020a",
                    "022",
                    "023",
                    "097",
                    "095",
                    "094",
                    "098",
                    "043",
                    "044",
                    "112",
                    "039",
                    "020b",
                    "039",
                    "098",
                    "140",
                    "141",
                    "138",
                    "139",
                    "A000",
                    "196",
                    "112",
                    "105",
                    "134",
                    "157",
                    "166",
                    "163",
                    "175",
                    "165",
                    "191",
                    "192",
                    "193",
                    "209",
                    "210",
                    "228",
                    "213",
                    "212",
                    "216",
                    "217",
                ],
                "heiligenkreuz-sb-217": [
                    "249",
                    "068",
                    "134",
                    "157",
                    "165",
                    "167",
                    "201",
                    "165",
                    "188",
                    "191",
                    "193",
                    "188",
                    "192",
                    "016",
                    "015",
                    "013",
                    "055",
                    "056",
                    "042",
                    "052",
                    "066",
                    "020a",
                    "078",
                    "191",
                    "131",
                    "192",
                    "195",
                    "266",
                    "242",
                    "293",
                    "273b",
                    "287",
                    "094",
                    "040",
                    "020a",
                    "023",
                    "095",
                    "094",
                    "098",
                    "020b",
                    "157",
                    "163",
                    "165",
                    "196",
                ],
                "ivrea-bc-xxxiii": [
                    "068",
                    "020a",
                    "022",
                    "023",
                    "095",
                    "094",
                    "021",
                    "097",
                    "098",
                    "039",
                    "040",
                    "039",
                    "040",
                    "041",
                    "129",
                    "043",
                    "044",
                    "112",
                    "088",
                    "104",
                    "134",
                    "135",
                    "139",
                ],
                "ivrea-bc-xxxiv": [
                    "022",
                    "020a",
                    "022",
                    "023",
                    "095",
                    "094",
                    "021",
                    "097",
                    "098",
                    "039",
                    "040",
                    "039",
                    "040",
                    "041",
                    "129",
                    "043",
                    "098",
                    "099",
                    "101",
                    "100",
                    "020a",
                    "044",
                    "112",
                    "088",
                    "134",
                    "135",
                    "060",
                    "140",
                    "141",
                    "138",
                    "139",
                    "157",
                    "165",
                    "164",
                    "163",
                    "093",
                    "201",
                    "159",
                ],
                "modena-bc-o-i-2": [
                    "163",
                    "039",
                    "040",
                    "020a",
                    "022",
                    "023",
                    "097",
                    "095",
                    "094",
                    "098",
                    "043",
                    "044",
                    "112",
                    "039",
                    "020b",
                    "039",
                    "098",
                    "157",
                    "163",
                    "165",
                    "191",
                    "192",
                    "193",
                    "196",
                    "216",
                    "217",
                ],
                "muenchen-bsb-lat-19416": [
                    "020a",
                    "093",
                    "020a",
                    "022",
                    "023",
                    "095",
                    "046",
                    "067",
                    "047",
                    "039",
                    "040",
                    "039",
                    "040",
                    "041",
                    "129",
                    "043",
                    "044",
                    "112",
                    "099",
                    "097",
                    "098",
                    "103",
                    "093",
                    "105",
                    "191",
                    "192",
                    "193",
                    "201",
                ],
                "muenchen-bsb-lat-29555-1": [
                    "M024",
                    "163",
                    "175",
                    "165",
                    "M015",
                    "196",
                    "193",
                    "209",
                    "210",
                    "228",
                    "273",
                    "224",
                ],
                "muenchen-bsb-lat-3853": [
                    "249",
                    "068",
                    "134",
                    "157",
                    "165",
                    "167",
                    "201",
                    "165",
                    "188",
                    "191",
                    "193",
                    "188",
                    "192",
                    "016",
                    "015",
                    "013",
                    "055",
                    "056",
                    "042",
                    "052",
                    "066",
                    "020a",
                    "078",
                    "191",
                    "131",
                    "192",
                    "195",
                    "252a",
                    "266",
                    "242",
                    "293",
                    "273b",
                    "287",
                    "094",
                    "040",
                    "020a",
                    "023",
                    "095",
                    "094",
                    "098",
                    "020b",
                    "157",
                    "163",
                    "165",
                    "196",
                ],
                "muenchen-bsb-lat-6360": ["157", "165", "167", "201", "165"],
                "paris-bn-lat-3878": [
                    "249",
                    "157",
                    "165",
                    "167",
                    "188",
                    "191",
                    "293",
                    "165",
                    "196",
                    "252a",
                ],
                "paris-bn-lat-4613": [
                    "020a",
                    "094",
                    "095",
                    "096",
                    "025",
                    "098",
                    "039",
                    "040",
                    "022",
                    "023",
                    "105",
                    "033",
                    "121",
                    "141",
                    "191",
                    "192",
                    "158",
                    "165",
                    "201",
                    "215",
                    "214",
                    "219",
                ],
                "salzburg-bea-st-peter-a-ix-32": [
                    "252",
                    "191",
                    "201",
                    "M023",
                    "215",
                    "210",
                    "093",
                    "112",
                    "293",
                    "252a",
                    "010",
                    "011",
                    "293",
                ],
                "st-gallen-sb-733": ["020a", "089", "022", "023", "097", "094"],
                "st-paul-abs-4-1": [
                    "092",
                    "093",
                    "020a",
                    "094",
                    "095",
                    "088",
                    "044",
                    "046",
                    "067",
                    "098",
                    "099",
                    "041",
                    "043",
                    "044",
                    "039",
                    "098",
                    "134",
                    "090",
                    "113",
                    "139",
                    "140",
                    "141",
                    "140",
                    "139",
                    "158",
                    "140",
                    "165",
                    "181",
                ],
                "vatikan-bav-chigi-f-iv-75": [
                    "232",
                    "020b",
                    "092",
                    "093",
                    "039",
                    "061",
                    "102",
                    "135",
                    "098",
                    "099",
                    "039",
                    "040",
                    "039",
                    "040",
                    "044",
                    "141",
                    "140",
                    "098",
                    "090",
                    "134",
                    "135",
                    "088",
                    "104",
                    "139",
                    "140",
                    "067",
                    "091",
                    "094",
                    "095",
                    "158",
                    "159",
                    "098",
                    "159",
                    "162",
                    "163",
                    "164",
                    "165",
                    "161",
                    "093",
                    "201",
                    "020a",
                    "095",
                    "088",
                    "044",
                    "046",
                    "099",
                    "041",
                    "043",
                    "044",
                    "141",
                    "158",
                    "208",
                ],
                "vatikan-bav-reg-lat-1000b": ["157", "165"],
                "vatikan-bav-reg-lat-263": [
                    "202",
                    "087",
                    "044",
                    "224",
                    "A000",
                    "163",
                    "093",
                    "224",
                    "225",
                    "232",
                    "020b",
                ],
                "vatikan-bav-vat-lat-5359": ["201", "165"],
                "vercelli-bce-clxxiv": ["167", "092", "093", "165", "163", "166"],
                "vercelli-bce-clxxv": ["163"],
                "wien-oenb-ser-n-3761": ["157"],
                "wolfenbuettel-hab-blankenb-130": [
                    "022",
                    "043",
                    "044",
                    "060",
                    "103",
                    "097",
                    "095",
                    "067",
                    "040",
                    "020a",
                    "112",
                    "038",
                    "023",
                    "094",
                    "041",
                    "020a",
                    "105",
                    "098",
                    "057",
                    "014",
                    "114",
                    "039",
                    "040",
                    "039",
                    "040",
                    "139",
                    "140",
                    "156",
                    "178",
                    "143",
                    "150",
                    "138",
                    "179",
                    "174",
                    "157",
                    "160",
                    "165",
                    "228",
                    "164",
                    "163",
                    "093",
                    "166",
                    "159",
                    "102",
                    "201",
                    "158",
                    "161",
                    "093",
                    "191",
                    "192",
                    "193",
                    "201",
                    "158",
                    "180",
                    "210",
                    "211",
                    "214",
                    "219",
                    "202",
                    "022",
                    "023",
                    "095",
                    "098",
                    "041",
                    "129",
                    "043",
                    "044",
                    "094",
                    "215",
                    "131",
                ],
            },
            builder=builder,
        )

        self.maximal_repeats(
            tree,
            [
                "4 022 023 095",
                "4 023 095 094",
                "4 041 129 043",
                "4 043 044 112",
                "4 092 093",
                "4 095 094 098",
                "4 098 099",
                "4 134 135",
                "4 139 140",
                "4 191 192 193",
                "4 201 165",
                "5 020a 022 023",
                "5 040 020a",
                "5 044 112",
                "5 157 165 167",
                "5 191 192",
                "6 023 095",
                "6 039 040 039 040",
                "6 095 094",
                "7 043 044",
                "7 157 165",
                "8 022 023",
                "9 039 040",
            ],
            min_cv=4,
        )
