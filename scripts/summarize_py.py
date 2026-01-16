# scripts/summarize_py.py
import ast
import sys

def format_arg(arg: ast.arg) -> str:
    """Formats a single ast.arg object into a string."""
    res = arg.arg
    if arg.annotation:
        # Use ast.unparse to handle complex type hints gracefully
        res += f": {ast.unparse(arg.annotation)}"
    return res

def format_args(args: ast.arguments) -> str:
    """Formats ast.arguments into a signature string like '(a, b: int)'."""
    parts = []
    
    all_args = args.posonlyargs + args.args
    pos_only_split = len(args.posonlyargs)
    
    # Defaults are stored for both pos-only and regular args together
    defaults_offset = len(all_args) - len(args.defaults)
    
    # Positional or keyword arguments
    for i, arg in enumerate(all_args):
        parts.append(format_arg(arg))
        if i >= defaults_offset:
            default_val = ast.unparse(args.defaults[i - defaults_offset])
            parts[-1] += f" = {default_val}"
    
    if pos_only_split > 0:
        parts.insert(pos_only_split, '/')
        
    # Keyword-only arguments
    if args.kwonlyargs:
        if not args.vararg:
            parts.append('*')
        for i, arg in enumerate(args.kwonlyargs):
            parts.append(format_arg(arg))
            if args.kw_defaults[i] is not None:
                default_val = ast.unparse(args.kw_defaults[i])
                parts[-1] += f" = {default_val}"

    # Varargs
    if args.vararg:
        parts.append(f"*{args.vararg.arg}")
    if args.kwarg:
        parts.append(f"**{args.kwarg.arg}")

    return f"({', '.join(parts)})"

def summarize_python_file(file_path: str) -> str:
    """
    Parses a Python file and returns a structured summary of its contents.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        tree = ast.parse(content, filename=file_path)
        
        summary_lines = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
                summary_lines.append(f"- {prefix}def `{node.name}{format_args(node.args)}`")
            elif isinstance(node, ast.ClassDef):
                summary_lines.append(f"- class `{node.name}`:")
                # Indent to show methods belonging to the class
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        prefix = "async " if isinstance(item, ast.AsyncFunctionDef) else ""
                        summary_lines.append(f"  - {prefix}def `{item.name}{format_args(item.args)}`")
        
        return "\n".join(summary_lines)
    except Exception as e:
        return f"Error summarizing {file_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize_py.py <file_path>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    summary = summarize_python_file(file_path)
    print(summary)
