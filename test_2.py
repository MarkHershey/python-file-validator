from pathlib import Path
import parser
import ast
from pprint import pprint
import _ast
import astor

sample_fp = Path("Samples/sample_file_1.py")


class FuncLister(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(node.name)
        self.generic_visit(node)


class RewriteName(ast.NodeTransformer):
    def visit_Name(self, node):
        return ast.copy_location(
            ast.Subscript(
                value=ast.Name(id="data", ctx=ast.Load()),
                slice=ast.Index(value=ast.Str(s=node.id)),
                ctx=node.ctx,
            ),
            node,
        )


class removeIf(ast.NodeTransformer):
    def visit_If(self, node):
        return None


with sample_fp.open() as source:
    tree = ast.parse(source.read())
    print("####### BEFORE #######\n")
    print(astor.to_source(tree))

    # call transformer
    tree = removeIf().visit(tree)

    # return source code
    extracted = astor.to_source(tree)
    print("####### AFTER #######\n")
    print(extracted)

# print(astor.dump_tree(tree))
