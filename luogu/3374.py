import sys
import os
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


# ------------------------------FastIO---------------------------------

n, m = map(int, input().split())
f = [0] * (4 * 5 * (10 ** 5))
a = list(map(int, input().split()))


def build(k, l, r):
    if l == r:
        f[k] = a[l - 1]
        return
    mid = (l + r) >> 1
    build(2 * k, l, mid)
    build(2 * k + 1, mid + 1, r)
    f[k] = f[2 * k] + f[2 * k + 1]


build(1, 1, n)


def add(k, l, r, x, y):
    f[k] += y
    if l == r:
        return
    mid = (l + r) >> 1
    if x <= mid:
        add(2 * k, l, mid, x, y)
    else:
        add(2 * k + 1, mid + 1, r, x, y)


def _sum(k, l, r, x, y):
    if l == x and r == y:
        return f[k]
    mid = (l + r) >> 1
    if y <= mid:
        return _sum(2 * k, l, mid, x, y)
    else:
        if x > mid:
            return _sum(2 * k + 1, mid + 1, r, x, y)
        else:
            return _sum(2 * k, l, mid, x, mid) + _sum(2 * k + 1, mid + 1, r, mid + 1, y)


for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        add(1, 1, n, x, y)
    else:
        print(_sum(1, 1, n, x, y))
