# 📖 Chapter 1: Introduction to Arrays & Strings (Giới thiệu Mảng & Chuỗi)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Understand how arrays are stored in memory (Hiểu mảng lưu trong bộ nhớ thế nào)
- Know the difference between Array and String in Python (Biết sự khác biệt giữa Mảng và Chuỗi trong Python)
- Master basic operations and their time complexity (Thành thạo các thao tác cơ bản và Big-O)

---

## 1. What is an Array? (Mảng là gì?)

An **Array** is a collection of elements stored in **contiguous memory** locations (Mảng là tập hợp phần tử lưu trong **vùng nhớ liên tiếp**).

### 🧠 Memory Layout (Bố cục bộ nhớ)

```
Index:    0     1     2     3     4
        +-----+-----+-----+-----+-----+
Array:  |  10 |  20 |  30 |  40 |  50 |
        +-----+-----+-----+-----+-----+
Address: 100   104   108   112   116
         ↑
         Each element takes same space (Mỗi phần tử chiếm cùng không gian)
```

### Why Contiguous Memory Matters (Tại sao bộ nhớ liên tiếp quan trọng)

Because elements are stored **side by side**, the computer can calculate the address of any element **instantly** (Vì phần tử lưu **cạnh nhau**, máy tính tính được địa chỉ bất kỳ phần tử **tức thì**):

```
Address of arr[i] = base_address + i × element_size
                  = 100 + i × 4     (int = 4 bytes)

arr[3] → 100 + 3 × 4 = 112 → O(1) access! ✅
```

This is why **random access is O(1)** — the defining superpower of arrays (Đây là lý do **truy cập ngẫu nhiên O(1)** — siêu năng lực của mảng).

---

## 2. What is a String? (Chuỗi là gì?)

A **String** is essentially an **array of characters** with special properties (Chuỗi thực chất là **mảng ký tự** với thuộc tính đặc biệt).

```
String:  "HELLO"
Index:    0   1   2   3   4
        +---+---+---+---+---+
        | H | E | L | L | O |
        +---+---+---+---+---+
```

### ⚠️ Critical: Strings are IMMUTABLE in Python (Chuỗi KHÔNG THỂ THAY ĐỔI trong Python)

```python
s = "hello"
s[0] = "H"    # ❌ TypeError: 'str' object does not support item assignment

# To modify, convert to list first (Để sửa, chuyển sang list trước)
s_list = list(s)       # ['h', 'e', 'l', 'l', 'o']
s_list[0] = 'H'        # ✅ Works!
s = ''.join(s_list)    # "Hello"
```

### String vs List in Python

| Feature | `list` (Array) | `str` (String) |
|---------|---------------|----------------|
| Mutable? | ✅ Yes | ❌ No (immutable) |
| Element type | Any type | Characters only |
| Modify in-place | ✅ `arr[i] = x` | ❌ Must create new string |
| Concatenation cost | O(1) amortized `.append()` | O(n) `s + "x"` creates new string! |
| Common operation | `arr.append()`, `arr.pop()` | `s.split()`, `s.join()` |

> **Key insight (Nhận xét quan trọng)**: Because strings are immutable, **string concatenation in a loop is O(n²)**, not O(n)! Use `''.join()` instead (Vì chuỗi bất biến, **nối chuỗi trong vòng lặp là O(n²)**! Dùng `''.join()` thay thế).
>
> ```python
> # ❌ BAD — O(n²): each += creates a new string
> result = ""
> for char in characters:
>     result += char        # Copies entire string each time!
>
> # ✅ GOOD — O(n): build list, join once
> parts = []
> for char in characters:
>     parts.append(char)    # O(1)
> result = ''.join(parts)   # O(n) total
> ```

---

## 3. Python Array Operations (Thao tác mảng trong Python)

### Creating Arrays (Tạo mảng)

```python
# Empty array (Mảng rỗng)
arr = []

# With values (Có giá trị)
arr = [1, 2, 3, 4, 5]

# Repeat values (Lặp giá trị)
arr = [0] * 10                    # [0, 0, 0, ..., 0]

# List comprehension (Tạo bằng comprehension)
arr = [i**2 for i in range(5)]    # [0, 1, 4, 9, 16]

# ⚠️ TRAP: 2D array wrong way (Cách SAI tạo mảng 2D)
grid = [[0] * 3] * 3              # ❌ All rows point to SAME list!
grid[0][0] = 1                    # Changes ALL rows!

# ✅ CORRECT 2D array
grid = [[0] * 3 for _ in range(3)]  # Each row is independent
```

### Common Operations with Big-O (Các thao tác thường dùng)

```python
arr = [10, 20, 30, 40, 50]

# --- Access — O(1) ---
val = arr[2]              # 30 — direct access by index
val = arr[-1]             # 50 — last element

# --- Modify — O(1) ---
arr[2] = 99               # [10, 20, 99, 40, 50]

# --- Append (end) — O(1) amortized ---
arr.append(60)             # [10, 20, 99, 40, 50, 60]

# --- Pop (end) — O(1) ---
arr.pop()                  # Removes & returns 60

# --- Pop (specific index) — O(n) ---
arr.pop(0)                 # Removes first → shifts all elements!

# --- Insert (beginning/middle) — O(n) ---
arr.insert(0, 5)           # Shifts all elements right!

# --- Search — O(n) ---
idx = arr.index(30)        # Linear search
exists = 30 in arr         # Linear search

# --- Length — O(1) ---
n = len(arr)

# --- Sort — O(n log n) ---
arr.sort()                 # In-place
sorted_arr = sorted(arr)   # Returns new sorted list

# --- Reverse — O(n) ---
arr.reverse()              # In-place
rev = arr[::-1]            # Returns new reversed list

# --- Slice — O(k) where k = slice length ---
sub = arr[1:4]             # Creates new list [arr[1], arr[2], arr[3]]
```

---

## 4. Python String Operations (Thao tác chuỗi trong Python)

```python
s = "Hello, World!"

# --- Access — O(1) ---
ch = s[0]                  # 'H'
ch = s[-1]                 # '!'

# --- Length — O(1) ---
n = len(s)                 # 13

# --- Check content — O(n) ---
has = 'World' in s         # True — linear search
idx = s.find('World')      # 7 — returns index, -1 if not found
idx = s.index('World')     # 7 — raises ValueError if not found

# --- Case — O(n), creates new string ---
s.lower()                  # "hello, world!"
s.upper()                  # "HELLO, WORLD!"

# --- Split & Join — O(n) ---
words = s.split(', ')      # ['Hello', 'World!']
joined = '-'.join(words)   # 'Hello-World!'

# --- Check type — O(n) ---
"abc".isalpha()            # True — all letters?
"123".isdigit()            # True — all digits?
"abc123".isalnum()         # True — letters or digits?

# --- Strip whitespace — O(n) ---
"  hello  ".strip()        # "hello"

# --- Replace — O(n) ---
s.replace("World", "Python")  # "Hello, Python!"

# --- Convert to list for mutation — O(n) ---
chars = list(s)            # ['H', 'e', 'l', 'l', 'o', ...]
```

---

## 5. Array vs Other Data Structures (Mảng vs Cấu trúc dữ liệu khác)

| Operation | Array | Linked List | Hash Set | Sorted Array |
|-----------|-------|-------------|----------|-------------|
| Access by index | **O(1)** ✅ | O(n) | ❌ N/A | **O(1)** |
| Search | O(n) | O(n) | **O(1)** ✅ | O(log n) |
| Insert at end | **O(1)** | **O(1)** | **O(1)** | O(n) |
| Insert at start | O(n) | **O(1)** ✅ | **O(1)** | O(n) |
| Delete | O(n) | **O(1)** ✅ | **O(1)** | O(n) |
| Memory | Contiguous | Scattered | Extra space | Contiguous |

**When to use arrays** (Khi nào dùng mảng):
- Need fast access by index (Cần truy cập nhanh theo index)
- Data size is known or grows at end (Kích thước biết trước hoặc tăng ở cuối)
- Need to iterate in order (Cần duyệt theo thứ tự)

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **Why is accessing `arr[1000]` the same speed as `arr[0]`?** Explain using memory addresses (Giải thích bằng địa chỉ bộ nhớ).

2. **What is the time complexity of this code?** (Big-O của đoạn code này?)
   ```python
   result = ""
   for i in range(n):
       result += str(i)
   ```
   *Hint: Think about string immutability.*

3. **Why is `arr.insert(0, x)` O(n) but `arr.append(x)` is O(1)?** (Tại sao insert đầu O(n) nhưng append cuối O(1)?)

4. **How do you create a correct 2D array in Python?** Why does `[[0]*3]*3` fail? (Tạo mảng 2D đúng cách? Tại sao `[[0]*3]*3` sai?)

5. **Name 2 situations where a Hash Set is better than an Array for searching** (Kể 2 tình huống Hash Set tốt hơn Mảng để tìm kiếm).

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
