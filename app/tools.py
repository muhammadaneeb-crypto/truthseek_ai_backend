import ast, operator, re
from tavily import TavilyClient
from .config import settings

_ALLOWED = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
 ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod,
 ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}
def _calc_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool): return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        a, b = _calc_node(node.left), _calc_node(node.right)
        if isinstance(node.op, ast.Pow) and (abs(b) > 10 or abs(a) > 1e6): raise ValueError("Exponent too large")
        return _ALLOWED[type(node.op)](a, b)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED: return _ALLOWED[type(node.op)](_calc_node(node.operand))
    raise ValueError("Only basic arithmetic is supported")
def calculate(expression: str):
    expression = expression.strip().replace("^", "**")
    if len(expression) > 200 or not re.fullmatch(r"[0-9+*/().%\-\s]+", expression): raise ValueError("Unsupported arithmetic expression")
    return _calc_node(ast.parse(expression, mode="eval").body)
def search_web(query: str, max_results: int = 5) -> list[dict]:
    if not settings.tavily_api_key: return []
    client = TavilyClient(api_key=settings.tavily_api_key)
    response = client.search(query=query, max_results=max_results, search_depth="advanced")
    output=[]
    for item in response.get("results", []):
        url=item.get("url", "")
        if url.startswith(("https://", "http://")):
            output.append({"title":item.get("title") or url,"url":url,"content":(item.get("content") or "")[:2500]})
    return output
