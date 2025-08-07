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

## Testing

Run the unit tests with:

```bash
pytest
```
