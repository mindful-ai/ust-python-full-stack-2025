# 🧩 Assessment Problem: Unit Testing the `StrOps` Class

## 🎯 Objective
You are required to write **unit test cases** for the class `StrOps`, which performs various string operations such as reversing words, counting words, removing punctuation, and more.

Your task is **not to re-implement the class**, but to write a **comprehensive unit test suite** using Python’s `unittest` framework that ensures all methods in the class are tested — including **boundary cases, invalid inputs, and tricky situations**.

---

## 🧱 Given Class (`StrOps`)

You are provided the following implementation for testing:

```python
import string
import random
from itertools import permutations

class StrOps:
    def getSpan(self, s, ss):
        result = []
        start = 0
        while True:
            idx = s.find(ss, start)
            if idx == -1:
                break
            result.append((idx, idx + len(ss)))
            start = idx + 1
        return result

    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

    def removePunctuation(self, s):
        return "".join(ch for ch in s if ch not in string.punctuation)

    def countWords(self, s):
        return len(s.split())

    def characterMap(self, s):
        cmap = {}
        for ch in s:
            cmap[ch] = cmap.get(ch, 0) + 1
        return cmap

    def makeTitle(self, s):
        return s.title()

    def normalizeSpaces(self, s):
        return " ".join(s.split())

    def transform(self, s, tt):
        return "".join(tt.get(ch, ch) for ch in s)

    def getPermutations(self, s):
        return ["".join(p) for p in permutations(s)]

    def jumble(self, s):
        s_list = list(s)
        random.shuffle(s_list)
        return "".join(s_list)
```

---

## 🧪 Your Task

Create a file named `test_strops.py` and write **unit test cases** using Python’s `unittest` module.

Your tests must include:
1. ✅ **Basic test cases** (standard inputs)
2. ⚠️ **Boundary and tricky cases**
3. 💥 **Error or edge case handling**

---

## 🧠 Test Scenarios to Cover

| Method | Description | Test Scenarios |
|--------|--------------|----------------|
| **getSpan(s, ss)** | Returns list of (start, end) for substring occurrences | 1️⃣ Normal case: `"mississippi", "ss"` → `[(2,4),(5,7)]`<br>2️⃣ Overlapping case: `"aaaa", "aa"` → `[(0,2),(1,3),(2,4)]`<br>3️⃣ No match: `"python", "zz"` → `[]`<br>4️⃣ Empty substring → should return `[]` (avoid infinite loop) |
| **reverseWords(s)** | Reverses word order | 1️⃣ `"this is test"` → `"test is this"`<br>2️⃣ Single word: `"hello"` → `"hello"`<br>3️⃣ Multiple spaces between words → should ignore extra spaces<br>4️⃣ Empty string → should return empty |
| **removePunctuation(s)** | Removes punctuation from string | 1️⃣ `"Hi! How are you?"` → `"Hi How are you"`<br>2️⃣ String with only punctuation → should return empty<br>3️⃣ Mixed punctuation and letters → `"A,B.C!"` → `"ABC"` |
| **countWords(s)** | Returns count of words separated by spaces | 1️⃣ `"this is test"` → 3<br>2️⃣ `"  spaced   text  "` → 2<br>3️⃣ Empty string → 0<br>4️⃣ String with only punctuation → 0 |
| **characterMap(s)** | Returns dict of character counts | 1️⃣ `"hello"` → {'h':1,'e':1,'l':2,'o':1}<br>2️⃣ Empty string → {}<br>3️⃣ Repeated single character `"aaa"` → {'a':3} |
| **makeTitle(s)** | Converts string to title case | 1️⃣ `"this is text"` → `"This Is Text"`<br>2️⃣ Mixed case: `"tHiS Is TeXt"` → `"This Is Text"`<br>3️⃣ Empty string → `""` |
| **normalizeSpaces(s)** | Reduces multiple spaces | 1️⃣ `"this   is    text"` → `"this is text"`<br>2️⃣ Tabs and newlines → should normalize to single spaces<br>3️⃣ Leading/trailing spaces → should be trimmed |
| **transform(s, tt)** | Replaces chars based on mapping | 1️⃣ `"math", {'t':'T'}` → `"maTh"`<br>2️⃣ Multiple replacements `"hello", {'l':'L','o':'O'}` → `"heLLO"`<br>3️⃣ Empty dict → returns input unchanged<br>4️⃣ Keys not present in string → no effect |
| **getPermutations(s)** | Returns list of all permutations | 1️⃣ `"abc"` → 6 permutations<br>2️⃣ `"aa"` → only one unique permutation<br>3️⃣ Empty string → `['']` |
| **jumble(s)** | Returns randomly shuffled version | 1️⃣ `"python"` → same characters, different order<br>2️⃣ Empty string → `""`<br>3️⃣ Assert that `sorted(jumble(s)) == sorted(s)` |

---

## 📘 Expected Learning Outcomes

| Skill | Expectation |
|-------|--------------|
| **Unit Testing** | Use of `unittest.TestCase` and multiple assert types |
| **Setup/TearDown** | Initialize `StrOps` instance cleanly |
| **Edge Case Thinking** | Handle spaces, empty inputs, and overlapping patterns |
| **Randomness Handling** | Test `jumble()` logic without relying on exact output |
| **Code Coverage** | Ensure every method is tested through at least 2 cases |

---

## 💡 Bonus Challenge (Optional)
- Write a **parameterized test** (using a loop or `subTest()`) to validate multiple inputs for a single function.
- Generate a **test coverage report** using:
  ```bash
  coverage run -m unittest discover
  coverage report -m
  ```
- Add tests to ensure that all functions return the correct **data types** (e.g., list, dict, string).

---
