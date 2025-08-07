"""Stage schedule generator for music festivals.

This script assigns shows to stages so that no overlapping shows share a stage
while minimising the total number of stages required. It can be run as a
stand-alone script or imported as a module.
"""

from __future__ import annotations

import argparse
import json
import importlib.util
from heapq import heappush, heappop
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

Show = Tuple[str, float, float]
Schedule = Dict[int, List[Show]]


def generate_schedule(shows: Sequence[Show]) -> Schedule:
    """Generate a stage schedule for the given shows.

    Args:
        shows: A sequence of shows represented as (name, start, end) tuples.

    Returns:
        Mapping of stage numbers to the list of shows assigned to that stage in
        chronological order.
    """
    events: List[Tuple[float, int, int]] = []
    for index, (_, start, end) in enumerate(shows):
        events.append((start, 1, index))  # 1 denotes start
        events.append((end, 0, index))    # 0 denotes end; ensures end before start when times equal

    events.sort()

    available: List[int] = []
    next_stage = 1
    schedule: Schedule = {}
    show_stage: Dict[int, int] = {}

    for _, event_type, index in events:
        if event_type == 1:  # start
            if available:
                stage = heappop(available)
            else:
                stage = next_stage
                next_stage += 1
            show_stage[index] = stage
            schedule.setdefault(stage, []).append(shows[index])
        else:  # end
            stage = show_stage[index]
            heappush(available, stage)

    return schedule


def load_shows(path: str) -> List[Show]:
    """Load shows from a Python module or JSON file."""
    file_path = Path(path)
    if file_path.suffix == ".py":
        spec = importlib.util.spec_from_file_location("shows_module", file_path)
        if not spec or not spec.loader:
            raise ImportError(f"Cannot load module from {path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        shows = getattr(module, "shows", None)
        if shows is None:
            raise AttributeError(f"Module {path} does not define 'shows'")
        return list(shows)
    else:
        with file_path.open() as f:
            return [tuple(show) for show in json.load(f)]


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default="input_shows.py",
        help="Path to a Python or JSON file providing a 'shows' list.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the resulting schedule as JSON.",
    )
    return parser.parse_args(argv)


def print_schedule(schedule: Schedule) -> None:
    """Pretty-print the schedule to the terminal."""
    for stage in sorted(schedule):
        print(f"Stage {stage}:")
        for name, start, end in schedule[stage]:
            print(f"  {name}: {start} - {end}")


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    shows = load_shows(args.input)
    schedule = generate_schedule(shows)
    print_schedule(schedule)
    if args.output:
        serialisable = {
            stage: [list(show) for show in shows]
            for stage, shows in schedule.items()
        }
        with open(args.output, "w") as f:
            json.dump(serialisable, f, indent=2)


if __name__ == "__main__":
    main()
