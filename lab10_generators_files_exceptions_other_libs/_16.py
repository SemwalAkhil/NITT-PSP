# numpy array
import numpy as np


def creation_and_attributes() -> None:
    print("\n--- 1. Array Creation & Attributes ---")
    a = np.array([[10, 20, 30], [40, 50, 60]])
    zeros = np.zeros((2, 3), dtype=int)
    ones = np.ones((2, 3), dtype=int)
    seq = np.arange(0, 10, 2)
    lin = np.linspace(0, 1, 5)

    print("2D Array:\n", a)
    print(f"ndim: {a.ndim} | shape: {a.shape} | size: {a.size} | dtype: {a.dtype}")
    print("zeros:\n", zeros)
    print("ones:\n", ones)
    print("arange(0, 10, 2):", seq)
    print("linspace(0, 1, 5):", lin)


def indexing_and_slicing() -> None:
    print("\n--- 2. Indexing, Slicing & Boolean Masking ---")
    arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ])
    print("Original 3x4 array:\n", arr)
    print("Element at row 1, col 2:", arr[1, 2])
    print("First two rows, cols 1 to 2:\n", arr[:2, 1:3])
    print("Last column:", arr[:, -1])
    print("Values greater than 6:", arr[arr > 6])


def math_and_broadcasting() -> None:
    print("\n--- 3. Vectorized Math & Broadcasting ---")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([10, 20, 30])  # Broadcast across each row of 'a'

    print("a:\n", a)
    print("b (1D):", b)
    print("a + b (broadcasting):\n", a + b)
    print("a * 2:\n", a * 2)
    print("a ** 2:\n", a ** 2)


def reshaping_and_stacking() -> None:
    print("\n--- 4. Reshaping & Stacking ---")
    flat = np.arange(1, 13)
    grid = flat.reshape(3, 4)
    transposed = grid.T

    print("1D array (1..12):", flat)
    print("Reshaped to 3x4:\n", grid)
    print("Transpose (4x3):\n", transposed)
    print("Vertical stack:\n", np.vstack((flat[:4], flat[4:8])))
    print("Horizontal stack:\n", np.hstack((flat[:2], flat[2:4])))


def aggregations_and_axis() -> None:
    print("\n--- 5. Aggregations & Axis Operations ---")
    scores = np.array([
        [80, 90, 70],
        [60, 75, 85],
        [95, 88, 92],
    ])
    print("Scores (3 students x 3 subjects):\n", scores)
    print("Overall mean:", np.mean(scores))
    print("Column means (per subject, axis=0):", np.mean(scores, axis=0))
    print("Row sums (per student, axis=1):", np.sum(scores, axis=1))
    print("Max value & flat index:", np.max(scores), np.argmax(scores))


def menu() -> None:
    actions = {
        "1": creation_and_attributes,
        "2": indexing_and_slicing,
        "3": math_and_broadcasting,
        "4": reshaping_and_stacking,
        "5": aggregations_and_axis,
    }

    while True:
        print("\n=== NumPy Array Menu ===")
        print("1. Array Creation & Attributes")
        print("2. Indexing, Slicing & Boolean Masking")
        print("3. Vectorized Math & Broadcasting")
        print("4. Reshaping & Stacking")
        print("5. Aggregations & Axis Operations")
        print("6. Run All Examples")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()
        if choice == "q":
            print("Exiting.")
            break
        if choice == "6":
            for fn in actions.values():
                fn()
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter 1-6 or 'q'.")


if __name__ == "__main__":
    menu()