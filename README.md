# StageInvaders

Demcon stage planner challenge.

## Schedule generator

`schedule_generator.py` assigns shows to stages so that no overlapping shows
share a stage and the number of stages is minimised.

```bash
python schedule_generator.py --input input_shows.py --output schedule.json
```

The `--input` argument accepts a Python or JSON file containing a `shows` list.
If `--output` is supplied the resulting schedule is written as JSON.

Stages are named with a set of randomly generated puns.  Provide a Python or
JSON file with custom names to override them:

```bash
python schedule_generator.py --input input_shows.py --stage-names my_names.py
```

Where `my_names.py` defines a `STAGE_NAMES` list, e.g.:

```python
STAGE_NAMES = ["Main Stage", "Chill Zone"]
```

Alternatively, a JSON file may contain a simple list:

```json
["Main Stage", "Chill Zone"]
```

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
