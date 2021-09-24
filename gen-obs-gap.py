from pathlib import Path
import yaml
import os

for path in Path("./").rglob("time-travel*.yaml"):
    data = yaml.load(open(str(path)))
    data["mode"] = "obs-gap"
    yaml.dump(
        data,
        open(
            os.path.join(path.parent, path.name.replace("time-travel", "obs-gap")), "w"
        ),
    )
