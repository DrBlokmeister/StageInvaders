# StageInvaders

Demcon stage planner challenge.

## Usage

Generate the sample schedule with default, punny stage names:

```bash
python schedule_generator.py
```

Provide your own stage names from a JSON or Python file:

```bash
python schedule_generator.py --stage-names names.json
python schedule_generator.py --stage-names names.py
```

`names.json` should contain an array of strings:

```json
["Main Stage", "Side Stage"]
```

`names.py` should define a list named `STAGE_NAMES`:

```python
STAGE_NAMES = ["Main Stage", "Side Stage"]
```

When a stage number exceeds the available names, the script prints `Stage <n>` for that entry.

## Schedule generator

`schedule_generator.py` assigns shows to stages so that no overlapping shows
share a stage and the number of stages is minimised.

```bash
python schedule_generator.py --input input_shows.py --output schedule.json
```

The `--input` argument accepts a Python or JSON file containing a `shows` list.
If `--output` is supplied the resulting schedule is written as JSON.

## Random show generator

`random_shows.py` provides a `generate_random_shows` helper to create random
show lists from a fixed set of band names:

```python
from random_shows import generate_random_shows

shows = generate_random_shows(10)
```

## Testing

Run the unit tests with:

```bash
pytest
```
