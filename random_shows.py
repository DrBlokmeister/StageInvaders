"""Utility for generating random festival shows."""

from __future__ import annotations

import random
from typing import List, Sequence, Tuple

Show = Tuple[str, float, float]

band_names: Sequence[str] = [
    "The Demi-Conductors",
    "Molten Salt 'n Pepper",
    "Electrolyzer Boys II H₂",
    "CryoJazz Quartet: Kelvin & the Degrees",
    "Qubit & The Entanglers",
    "Biopsy Bot Bi-Metal",
    "Servo Skynet Funk",
    "SMR Metalcore Reactor",
    "Thorizon Thunderlords",
    "Hydrogenated Groove Machine",
    "OptoMech Overload",
    "MechaTronic BoomBap",
    "Cleanroom Crooners",
    "DICE Rollers",
    "Plasma Etch Ninjas",
    "Stack Pressure Funk Collective",
    "Vapor Deposition Devotees",
    "Superfluid Funkadelic",
    "Rotor & The Cryostats",
    "Kelvinators of Love",
    "Overlapocalypse Now",
    "Flux Capacitor Leakage",
    "Servo Servo Go!",
    "Chip Placement Misfits",
    "Magnetic Resonance Rockers",
    "Needle Drive & The Scanner Bots",
    "Hydride & Seek",
    "Robolap Partners",
    "QCryo & The Coolants",
    "MiniModular Menace",
    "Bionic Stagecraft",
    "The DemCon-Artists",
    "DeMCONic Force Five",
    "DemConfidential Rappers",
    "GrindCore XY Stage",
    "Pulse Tube Troubadours",
    "Leak Test Lounge Lizards",
    "Servo Sirens",
    "True Grit & Grippers",
    "Ampere Time Machine",
    "Proton Pump Funk Unit",
    "SaltCore Grinder",
    "ThoriZoners",
    "Quantum Flippin’ Bits",
    "Femtosecond Headbang",
    "AlgorithmiX & the Min-Heaps",
    "Hydrogen Rage Machine",
    "Cryogenics & Roses",
    "Cobot Cabal Choir",
    "Valve Body Voodoo",
    "OptoElectro Swingers",
    "SMRizing Demolition",
    "Servo Serpe nts",
    "Luer & Order",
    "Coolant Flow Ragga",
]


def generate_random_shows(
    count: int,
    *,
    start_hour: float = 0.0,
    end_hour: float = 24.0,
    min_duration: float = 0.5,
    max_duration: float = 3.0,
    rng: random.Random | None = None,
) -> List[Show]:
    """Generate a list of random shows using the :data:`band_names` list.

    Args:
        count: Number of shows to generate.
        start_hour: Earliest possible start time.
        end_hour: Latest possible end time.
        min_duration: Minimum length of a show in hours.
        max_duration: Maximum length of a show in hours.
        rng: Optional ``random.Random`` instance for reproducibility.

    Returns:
        A list of ``(name, start, end)`` tuples.
    """
    if rng is None:
        rng = random

    if count <= len(band_names):
        names = list(rng.sample(band_names, count))
    else:
        names = list(rng.sample(band_names, len(band_names)))
        names += list(rng.choices(band_names, k=count - len(band_names)))

    shows: List[Show] = []
    for name in names:
        start = rng.uniform(start_hour, end_hour - min_duration)
        duration = rng.uniform(min_duration, min(max_duration, end_hour - start))
        end = start + duration
        shows.append((name, round(start, 2), round(end, 2)))
    return shows
