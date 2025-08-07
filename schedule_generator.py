import argparse
import json
import random
import runpy
from typing import Iterable, List

stage_prefixes = [
    "Heisenberg",
    "Optical",
    "Qubit",
    "Cryo",
    "Flux",
    "Kelvin",
    "Servo",
    "Photon",
    "Plasma",
    "Gripper",
    "Ampere",
    "Hydrogen",
    "Quantum",
    "DICE",
    "Nano",
    "Circuit",
    "Magnetron",
    "Molten",
    "PhaseShift",
    "Thorizon",
]

stage_suffixes = [
    "Dome",
    "Colosseum",
    "Planetarium",
    "Lab",
    "Core",
    "Reactor",
    "Arena",
    "Theatre",
    "Chamber",
    "Nest",
    "Generator",
    "Loop",
    "Vortex",
    "Box",
    "Sanctum",
    "Station",
    "Pit",
    "Quadrant",
    "Yard",
    "Cage",
]

# Epic Main Stage suggestions
main_stages = [
    "The Quantum Nexus",
    "The Mechatronic Arena",
    "The Reactor of Legends",
    "The Core Stage",
    "The Dome of Infinity",
]


def _generate_default_stage_names(count: int = 5) -> List[str]:
    """Generate a list of default stage names."""
    names = [random.choice(main_stages)]
    for _ in range(count - 1):
        names.append(f"{random.choice(stage_prefixes)} {random.choice(stage_suffixes)}")
    return names


STAGE_NAMES = _generate_default_stage_names()


def load_stage_names(path: str) -> List[str]:
    """Load stage names from a JSON or Python file."""
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list) or not all(isinstance(s, str) for s in data):
            raise ValueError("JSON stage names must be a list of strings")
        return data
    if path.endswith(".py"):
        data = runpy.run_path(path)
        names = data.get("STAGE_NAMES") or data.get("stage_names")
        if names is None:
            raise ValueError("Python file must define STAGE_NAMES or stage_names")
        if not isinstance(names, list) or not all(isinstance(s, str) for s in names):
            raise ValueError("STAGE_NAMES must be a list of strings")
        return names
    raise ValueError("Unsupported file type for stage names; use .json or .py")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Generate and print a schedule.")
    parser.add_argument(
        "--stage-names",
        help="Path to JSON or Python file providing custom STAGE_NAMES",
    )
    return parser.parse_args(argv)


def print_schedule(schedule: Iterable[dict], stage_names: List[str] | None = None):
    if stage_names is None:
        stage_names = STAGE_NAMES
    for slot in schedule:
        stage_num = slot["stage"]
        if 0 < stage_num <= len(stage_names):
            name = stage_names[stage_num - 1]
        else:
            name = f"Stage {stage_num}"
        print(f"{slot['time']} - {name} - {slot['band']}")


def main(argv=None):
    args = parse_args(argv)
    stage_names = STAGE_NAMES
    if args.stage_names:
        stage_names = load_stage_names(args.stage_names)
    example_schedule = [
        {"time": "10:00", "stage": 1, "band": "Opening Act"},
        {"time": "11:00", "stage": 2, "band": "Midday Jam"},
        {"time": "12:00", "stage": 6, "band": "Closing Band"},
    ]
    print_schedule(example_schedule, stage_names)


if __name__ == "__main__":
    main()
