"""Tests for the random show generator."""

import os
import sys
import random

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from random_shows import band_names, generate_random_shows


def test_generate_random_shows_basic():
    rng = random.Random(0)
    shows = generate_random_shows(5, rng=rng, start_hour=0, end_hour=24)
    assert len(shows) == 5
    for name, start, end in shows:
        assert name in band_names
        assert 0 <= start < end <= 24


def test_no_duplicate_names_when_enough():
    rng = random.Random(1)
    shows = generate_random_shows(len(band_names), rng=rng)
    names = [name for name, _, _ in shows]
    assert len(names) == len(set(names))
