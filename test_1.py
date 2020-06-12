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


tree = RewriteName().visit(tree)


with sample_fp.open() as source:
    tree = ast.parse(source.read())

    # FuncLister().visit(tree)

    for node in ast.walk(tree):
        if isinstance(node, _ast.ClassDef):
            print(node.name)

#     extracted = astor.to_source(tree)
#
#     print(extracted)
#
#     # pprint(tree)
#     # print()
#     # pprint(tree.body)
#     # pprint(type(tree.body))
#     # print()
#
#     for object in tree.body:
#         new_body = []
#         if isinstance(object, _ast.ImportFrom):
#             new_body.append(object)
#             print(f"Found desired object: {object}")
#         elif isinstance(object, _ast.Import):
#             new_body.append(object)
#             print(f"Found desired object: {object}")
#         elif isinstance(object, _ast.ClassDef):
#             new_body.append(object)
#             print(f"Found desired object: {object}")
#         elif isinstance(object, _ast.FunctionDef):
#             new_body.append(object)
#             print(f"Found desired object: {object}")
#         else:
#             pass
#
#     print(new_body)
#
#
# print(astor.dump_tree(tree))
