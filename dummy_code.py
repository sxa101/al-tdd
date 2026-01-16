# dummy_code.py

class MyClass:
    """A dummy class."""

    def __init__(self, value: int = 0):
        self.value = value

    def method_one(self, name: str) -> str:
        return f"Hello, {name}"
    
    async def async_method(self, items: list, *, a=1, b=None):
        pass

def top_level_function(a, b, c=True, /):
    """A top level function."""
    pass
