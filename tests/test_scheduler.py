"""Unit tests for the festival stage schedule generator."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from schedule_generator import generate_schedule


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


def test_print_schedule_uses_stage_names(tmp_path, capsys):
    import schedule_generator as sg

    stage_file = tmp_path / "names.py"
    stage_file.write_text("STAGE_NAMES = ['Alpha Arena', 'Beta Base']")

    sg.main(["--input", "input_shows.py", "--stage-names", str(stage_file)])

    out = capsys.readouterr().out.splitlines()
    assert out[0] == "Alpha Arena:"
    assert out[3] == "Beta Base:"
