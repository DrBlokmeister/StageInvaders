# StageInvaders

Demcon stage planner challenge

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
