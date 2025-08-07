"""Unit tests for the festival stage schedule generator."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from schedule_generator import generate_schedule, print_schedule


def _min_stages(shows):
    events = []
    for _, start, end in shows:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()
    current = max_overlap = 0
    for _, delta in events:
        current += delta
        max_overlap = max(max_overlap, current)
    return max_overlap


def _stage_is_valid(stage_shows):
    return all(prev[2] <= curr[1] for prev, curr in zip(stage_shows, stage_shows[1:]))


def test_print_schedule_maps_names(capsys):
    schedule = {
        1: [("Band A", 10, 11)],
        2: [("Band B", 11, 12)],
        4: [("Band C", 12, 13)],
    }
    names = ["Main Stage", "Second Stage"]
    print_schedule(schedule, stage_names=names)
    captured = capsys.readouterr().out
    assert "Main Stage:" in captured
    assert "  Band A: 10 - 11" in captured
    assert "Second Stage:" in captured
    assert "  Band B: 11 - 12" in captured
    assert "Stage 4:" in captured
    assert "  Band C: 12 - 13" in captured


def test_schedule_minimises_stage_count():
    shows = [
        ("show_1", 0, 10),
        ("show_2", 5, 15),
        ("show_3", 15, 20),
    ]
    schedule = generate_schedule(shows)
    assert len(schedule) == _min_stages(shows)
    assert all(_stage_is_valid(s) for s in schedule.values())


def test_handles_edge_touching_shows():
    shows = [
        ("a", 0, 10),
        ("b", 10, 20),
        ("c", 10, 30),
    ]
    schedule = generate_schedule(shows)
    assert len(schedule) == _min_stages(shows)
    assert all(_stage_is_valid(s) for s in schedule.values())

