from pathlib import Path
import parser
import ast
import _ast
from pprint import pprint
import os
import astor


def convert(file_path: str, types_to_keep=None):
    if types_to_keep == None:
        types_to_keep = (_ast.Import, _ast.ImportFrom, _ast.ClassDef, _ast.FunctionDef)

    # read file
    path = Path(file_path)
    if not path.is_file():
        return

    file_name = os.path.basename(path)
    if file_name[-3:] != ".py":
        return

    with path.open() as source:
        module_tree = ast.parse(source.read())

    parts = []

    for node in ast.iter_child_nodes(module_tree):
        if type(node) in types_to_keep:
            part = astor.to_source(node)
            parts.append(part)
        else:
            pass

    code = "".join(parts)

    pprint(code)

    export_fp = path.parent / (file_name[:-3] + "_new.py")

    with export_fp.open(mode="w") as f:
        f.write(code)


if __name__ == "__main__":
    convert("Samples/sample_file_1.py")
