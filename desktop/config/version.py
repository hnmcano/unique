import json
from pathlib import Path

def get_version():
    path = Path(__file__).parent / "version.json"
    data = json.loads(path.read_text())
    return data["version"]


#USO

# from config.version import get_version
# print(get_version())