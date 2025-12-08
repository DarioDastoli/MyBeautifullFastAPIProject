import os
from pathlib import Path

def load_env(path:str = ".env") -> None:
    env_path = Path(path)

    with env_path.open() as f:
        for line in f:
            line = line.strip()

            #skip any comment
            if not line or line.startswith("#"):
                continue
            
            #skip lines where i do not  asign anything
            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            os.environ.setdefault(key, value)