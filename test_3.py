from pathlib import Path
import parser
import ast
from pprint import pprint
import _ast
import astor

sample_fp = Path("Samples/sample_file_1.py")


class removeIf(ast.NodeTransformer):
    def visit_If(self, node):
        return None


class removeExpr(ast.NodeTransformer):
    def visit_Expr(self, node):
        return None


# read file
with sample_fp.open() as source:
    tree = ast.parse(source.read())


# object types to keep
types_to_keep = (_ast.Import, _ast.ImportFrom, _ast.ClassDef, _ast.FunctionDef)

# traverse direct child nodes
for node in ast.iter_child_nodes(tree):
    if type(node) in types_to_keep:
        print(astor.to_source(node))

    else:
        pass

    #
    # print("####### BEFORE #################################################\n")
    # print(astor.to_source(tree))
    #
    # # call transformer
    # tree = removeIf().visit(tree)
    #
    # # return source code
    # extracted = astor.to_source(tree)
    # print("####### AFTER #################################################\n")
    # print(extracted)

# print(astor.dump_tree(tree))
