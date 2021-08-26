#!/usr/bin/env pytest

from pytest import raises
import src.util.DateStringFormatter as dsf
from src.test.ReadDataFrames import get_train


# statically perform the conversion at the start
df_train = get_train()
df_train = dsf.format_timestrings_inside_pd(df_train)


def enter_line_nr_and_shift_because_arrays_start_at_zero(line):
    return line - 1

# find months inside the csv using a similar regex: `^\d\d\.02\.2013`


def test_existence():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(1)
    assert df_train.iloc[line]['date'] is not None


def test_first_line():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(1)
    assert df_train.iloc[line]['date'] == "2013-01"


def test_last_line_of_january_2013():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(115690)
    assert df_train.iloc[line]['date'] == "2013-01"


def test_first_line_of_february_2013():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(115691)
    assert df_train.iloc[line]['date'] == "2013-02"


def test_first_line_of_match_2013():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(224304)
    assert df_train.iloc[line]['date'] == "2013-03"


def test_something_random_in_between():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(1245282)
    assert df_train.iloc[line]['date'] == "2013-12"


def test_last_line_of_august_2015():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(2831747)
    assert df_train.iloc[line]['date'] == "2015-08"


def test_first_line_of_september_2019():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(2831748)
    assert df_train.iloc[line]['date'] == "2015-09"


def test_last_line():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(2935849)
    assert df_train.iloc[line]['date'] == "2015-10"


def test_going_over_bounds():
    line = enter_line_nr_and_shift_because_arrays_start_at_zero(2935850)

    with raises(IndexError) as exc_info:
        df_train.iloc[line]['date']
    assert exc_info.type is IndexError
