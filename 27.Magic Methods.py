"""
MAGIC (DUnder) METHODS — COMPLETE NOTES & EXAMPLES
==================================================

Magic (aka “dunder”, double-underscore) methods let your classes hook into
Python’s built-in behavior: printing, comparing, iterating, using with-statements,
operators (+, *, in, len, []), formatting, and more.

⚠️ Tips
- Don’t shadow your class names with instances (e.g., avoid: person = person()).
- Implement __repr__ for debugging, __str__ for user-facing text.
- Keep __eq__ and __hash__ consistent (only hash immutable state).

This file is organized into themed sections with:
1) Syntax (what to implement) and
2) A minimal, practical example you can run.
"""

print("\n=== 1) OBJECT LIFECYCLE & REPRESENTATION: __new__, __init__, __repr__, __str__, __del__ ===")

# SYNTAX:
# class C:
#     def __new__(cls, *args, **kwargs):  # allocation (rarely needed)
#         return super().__new__(cls)
#     def __init__(self, ...):            # initialization
#         ...
#     def __repr__(self):                 # official/debug representation
#         return f"C(...)"                # should be unambiguous
#     def __str__(self):                  # human-friendly string
#         return "nice text"
#     def __del__(self):                  # called when object is (maybe) GC'ed
#         ...

class Person:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)  # allocation
        return obj

    def __init__(self, name, age):
        self.name = name
        self.age = age  # initialization

    def __repr__(self):
        # Debug-oriented. Include class & fields.
        return f"Person(name={self.name!r}, age={self.age!r})"

    def __str__(self):
        # User-oriented, readable.
        return f"{self.name} ({self.age}y)"

    def __del__(self):
        # NOTE: Not guaranteed timing; avoid critical logic here.
        pass

p = Person("Krish", 24)
print("repr(p):", repr(p))
print("str(p): ", str(p))  # also prints if you just do: print(p)

print("\n=== 2) COMPARISONS & HASHING: __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __hash__ ===")

# SYNTAX:
# def __eq__(self, other): ...
# def __lt__(self, other): ...  # <   (then Python can derive sorted order if you supply enough)
# def __hash__(self): ...       # only define if immutable & comparable

class Card:
    __slots__ = ("rank", "suit")  # optional: memory/attr control
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card({self.rank!r}, {self.suit!r})"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        order = "23456789TJQKA"
        # sort by rank first, then suit
        return (order.index(self.rank), self.suit) < (order.index(other.rank), other.suit)

    def __hash__(self):
        # hash immutable tuple of attributes
        return hash((self.rank, self.suit))

hand = [Card("A", "♠"), Card("T", "♥"), Card("A", "♦")]
print("Unsorted hand:", hand)
print("Sorted hand:  ", sorted(hand))
print("Set dedupe:   ", set(hand))  # uses __hash__/__eq__

print("\n=== 3) NUMERIC / OPERATOR OVERLOADING: __add__, __radd__, __iadd__, __sub__, __mul__, __rmul__, __truediv__, __neg__, __pos__, __abs__, __round__, __float__, __int__, __index__ ===")

# SYNTAX (common):
# def __add__(self, other): ...
# def __radd__(self, other): ...
# def __iadd__(self, other): ...
# def __mul__(self, other): ...
# def __rmul__(self, other): ...
# def __truediv__(self, other): ...
# def __neg__(self): ...
# def __abs__(self): ...
# def __float__(self): ...
# def __int__(self): ...
# def __index__(self): ...  # integer index (e.g., used in slicing)

import math

class Vector2D:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # +, -, scalar *
    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)  # commutative here

    def __iadd__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # scalar multiplication only
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __abs__(self):
        # magnitude
        return math.hypot(self.x, self.y)

    def __float__(self):
        # convert to magnitude
        return float(abs(self))

    def __int__(self):
        return int(abs(self))

v1, v2 = Vector2D(3, 4), Vector2D(1, 2)
print("v1+v2 =", v1 + v2)
v1 += v2
print("v1 after iadd:", v1)
print("3 * v2 =", 3 * v2)
print("|v2| =", abs(v2), " float(v2) =", float(v2), " int(v2) =", int(v2))

print("\n=== 4) CONTAINER/SEQUENCE PROTOCOL: __len__, __getitem__, __setitem__, __delitem__, __contains__, __iter__, __reversed__, __bool__ ===")

# SYNTAX:
# def __len__(self): ...
# def __getitem__(self, idx): ...    # support int indexing AND slices
# def __setitem__(self, idx, value): ...
# def __delitem__(self, idx): ...
# def __contains__(self, item): ...
# def __iter__(self): return iterator
# def __reversed__(self): return reversed iterator
# def __bool__(self): return True/False

class Notebook:
    def __init__(self, pages=None):
        self._pages = list(pages or [])

    def __repr__(self):
        return f"Notebook({self._pages!r})"

    def __len__(self):
        return len(self._pages)

    def __getitem__(self, idx):
        return self._pages[idx]  # supports int index & slice automatically

    def __setitem__(self, idx, value):
        self._pages[idx] = value

    def __delitem__(self, idx):
        del self._pages[idx]

    def __contains__(self, item):
        return item in self._pages

    def __iter__(self):
        return iter(self._pages)

    def __reversed__(self):
        return reversed(self._pages)

    def __bool__(self):
        return bool(self._pages)

nb = Notebook(["Todo", "Ideas", "Logs"])
print("len(nb):", len(nb))
print("nb[1]:", nb[1])
nb[1] = "Sketches"
print("slice nb[:2]:", nb[:2])
print("'Logs' in nb:", "Logs" in nb)
for p in nb: pass
print("reversed:", list(reversed(nb)))
del nb[0]
print("after del:", nb)
print("truthiness:", bool(nb))

print("\n=== 5) ITERATOR PROTOCOL: __iter__, __next__ ===")

# SYNTAX:
# class Iter:
#     def __iter__(self): return self
#     def __next__(self): ... raise StopIteration

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("Countdown from 3:", list(Countdown(3)))

print("\n=== 6) ATTRIBUTE ACCESS HOOKS: __getattr__, __getattribute__, __setattr__, __delattr__, __dir__ ===")

# SYNTAX:
# def __getattr__(self, name): ...          # only called if normal lookup fails
# def __getattribute__(self, name): ...     # called for EVERY attribute access
# def __setattr__(self, name, value): ...
# def __delattr__(self, name): ...
# def __dir__(self): return list_of_names

class LazyRecord:
    def __init__(self):
        super().__setattr__("_data", {"cached": 42})

    def __getattr__(self, name):
        # only runs if attribute not found normally
        if name == "lazy":
            value = "computed-on-demand"
            self._data[name] = value
            return value
        raise AttributeError(name)

    def __getattribute__(self, name):
        # monitor access (delegate carefully!)
        if name not in ("_data", "__dict__", "__class__"):
            # print(f"[get] {name}")  # you can log if you want
            pass
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        # track writes
        # print(f"[set] {name}={value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        # print(f"[del] {name}")
        super().__delattr__(name)

    def __dir__(self):
        # extend dir() with dynamic items
        return sorted(set(super().__dir__() + list(self._data.keys())))

lr = LazyRecord()
print("dir(lr) contains 'cached'?", "cached" in dir(lr))
print("lr.lazy (triggers __getattr__):", lr.lazy)

print("\n=== 7) CALLABLE OBJECTS: __call__ ===")

# SYNTAX:
# def __call__(self, *args, **kwargs): ...

class Accumulator:
    def __init__(self, start=0):
        self.total = start
    def __call__(self, value):
        self.total += value
        return self.total

acc = Accumulator()
print("acc(5):", acc(5), "acc(10):", acc(10))

print("\n=== 8) CONTEXT MANAGERS: __enter__, __exit__ ===")

# SYNTAX:
# def __enter__(self): ... return resource
# def __exit__(self, exc_type, exc, tb): ... return True to suppress exception

import time

class Timer:
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.t0
        print(f"[Timer] Elapsed ~{self.elapsed:.6f}s")
        return False  # don't suppress exceptions

with Timer() as t:
    sum(range(100000))

print("\n=== 9) CONVERSION & FORMATTING: __format__, __bytes__, __bool__, __len__ (truthiness), __complex__, __float__, __int__, __round__ ===")

# SYNTAX:
# def __format__(self, format_spec): ...
# def __bytes__(self): ...
# def __bool__(self): ...
# def __int__(self): ...
# def __float__(self): ...
# def __complex__(self): ...
# def __round__(self, n): ...

class FileSize:
    def __init__(self, bytes_):
        self.bytes = int(bytes_)
    def __int__(self):
        return self.bytes
    def __float__(self):
        return float(self.bytes)
    def __bytes__(self):
        return self.bytes.to_bytes(8, "big", signed=False)
    def __bool__(self):
        return self.bytes != 0
    def __format__(self, spec):
        # Support custom "human" format: f"{fs:human}"
        if spec == "human":
            b = self.bytes
            for unit in ("B","KB","MB","GB","TB","PB"):
                if b < 1024 or unit == "PB":
                    return f"{b:.2f} {unit}"
                b /= 1024
        # Fallback: respect normal formatting of the raw integer
        return format(self.bytes, spec)

fs = FileSize(1_234_567)
print("int(fs):", int(fs), "float(fs):", float(fs))
print("bytes(fs):", bytes(fs))
print(f"human: {fs:human}   dec: {fs:d}")

print("\n=== 10) SLICING & INDICES: __index__ and slice-aware __getitem__ ===")

# __index__ supplies an integer index usable where Python expects an int (e.g., slicing step)
class Step:
    def __init__(self, n):
        self.n = int(n)
    def __index__(self):
        return self.n

data = list(range(10))
print("data[::Step(2)]:", data[::Step(2)])

print("\n=== 11) DESCRIPTORS: __get__, __set__, __delete__ (advanced attribute control) ===")

# SYNTAX:
# class Descriptor:
#     def __get__(self, instance, owner): ...
#     def __set__(self, instance, value): ...
#     def __delete__(self, instance): ...

class LoggedAttribute:
    def __init__(self, name):
        self.name = name
        self.private_name = f"_{name}"
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = getattr(instance, self.private_name, None)
        # print(f"[desc get] {self.name} -> {value}")
        return value
    def __set__(self, instance, value):
        # print(f"[desc set] {self.name} = {value}")
        setattr(instance, self.private_name, value)
    def __delete__(self, instance):
        # print(f"[desc del] {self.name}")
        delattr(instance, self.private_name)

class User:
    name = LoggedAttribute("name")
    age  = LoggedAttribute("age")
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"

u = User()
u.name = "Nived"
u.age = 18
print("Descriptor-backed user:", u)

print("\n=== 12) COPYING & PICKLING HOOKS: __copy__, __deepcopy__, __getstate__, __setstate__ ===")

# SYNTAX:
# def __copy__(self): ...
# def __deepcopy__(self, memo): ...
# def __getstate__(self): return state
# def __setstate__(self, state): ...

import copy, pickle

class Settings:
    def __init__(self, theme, hotkeys=None):
        self.theme = theme
        self.hotkeys = dict(hotkeys or {})

    def __repr__(self):
        return f"Settings(theme={self.theme!r}, hotkeys={self.hotkeys!r})"

    def __copy__(self):
        # shallow copy: copy dict reference
        return Settings(self.theme, self.hotkeys)

    def __deepcopy__(self, memo):
        # deep copy: copy dict content
        return Settings(copy.deepcopy(self.theme, memo),
                        copy.deepcopy(self.hotkeys, memo))

    def __getstate__(self):
        # choose what to pickle
        return {"theme": self.theme, "hotkeys": self.hotkeys}

    def __setstate__(self, state):
        self.theme = state["theme"]
        self.hotkeys = state["hotkeys"]

s1 = Settings("dark", {"save": "Ctrl+S"})
s2 = copy.copy(s1)
s3 = copy.deepcopy(s1)
s1.hotkeys["open"] = "Ctrl+O"
print("Original:", s1)
print("Shallow copy (shares dict):", s2)
print("Deep copy (separate dict): ", s3)

blob = pickle.dumps(s1)
s4 = pickle.loads(blob)
print("Unpickled:", s4)

print("\n=== 13) STRING INTEROP: __format__, f-strings, __repr__ fallbacks ===")
# f"{obj}" -> __format__ -> __str__ -> __repr__
# format(obj, "spec") -> __format__("spec")
class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = float(amount); self.currency = currency
    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"
    def __str__(self):
        return f"{self.currency} {self.amount:,.2f}"
    def __format__(self, spec):
        if spec == "short":
            return f"{self.currency} {self.amount:.0f}"
        return format(str(self), spec)

