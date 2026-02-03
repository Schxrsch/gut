import time
import sympy as sp

def build_input():
    n = 20
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    for i in range(n):
        A[i][i] = 2.0
        if i > 0:
            A[i][i - 1] = -1.0
        if i < n - 1:
            A[i][i + 1] = -1.0
        b[i] = 1.0
    return A, b

def run_once(A, b):
    A = sp.Matrix(A)
    b = sp.Matrix(b)
    x = A.LUsolve(b)
    return list(x)

def main():
    A, b = build_input()

    repeats = 3  # number of functional units

    checksum = 0.0
    start = time.time()
    for _ in range(repeats):
        x = run_once(A, b)
        checksum += float(x[0])  # prevent optimization
    elapsed = time.time() - start

    print(f"elapsed={elapsed:.3f}s checksum={checksum}")

    # SCI functional units
    print(f"R={repeats}")

if __name__ == "__main__":
    main()
