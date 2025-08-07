import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from schedule_generator import print_schedule


def test_print_schedule_maps_names(capsys):
    schedule = [
        {"time": "10:00", "stage": 1, "band": "Band A"},
        {"time": "11:00", "stage": 2, "band": "Band B"},
        {"time": "12:00", "stage": 4, "band": "Band C"},
    ]
    names = ["Main Stage", "Second Stage"]
    print_schedule(schedule, stage_names=names)
    captured = capsys.readouterr().out
    assert "10:00 - Main Stage - Band A" in captured
    assert "11:00 - Second Stage - Band B" in captured
    assert "12:00 - Stage 4 - Band C" in captured
