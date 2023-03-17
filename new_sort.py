import os
import sys

sort_name = sys.argv[1:]
raw_sort_name = " ".join(sort_name)
if len(sort_name) > 1:
    sort_name = "_".join(sort_name)

os.system(f"mkdir {sort_name} && touch {sort_name}/{sort_name}.py")

file_path = os.path.join(sort_name,f"{sort_name}.py")
with open(file_path, "w") as f:
    f.write(f"""\"\"\"{raw_sort_name.capitalize()}\"\"\"
from typing import List
def {sort_name}(lst:list) -> List:
    \"\"\"{raw_sort_name.capitalize()} algorithm\"\"\"

    return lst
""")