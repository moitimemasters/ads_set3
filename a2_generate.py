import typing as tp
import random


def generate_random(size: int, numbers_range: tp.Tuple[int, int]) -> list[int]:
    return [random.randint(*numbers_range) for _ in range(size)]


def generate_reverse_sorted(size: int, numbers_range: tp.Tuple[int, int]) -> list[int]:
    generated = generate_random(size, numbers_range)
    generated.sort()
    generated.reverse()
    return generated


def generate_almost_sorted(size: int, numbers_range: tp.Tuple[int, int]) -> list[int]:
    generated = generate_reverse_sorted(size, numbers_range)
    generated.reverse()

    swap_times = random.randint(0, min(size // 5, 10))

    for _ in range(swap_times):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        generated[a], generated[b] = generated[b], generated[a]

    return generated


if __name__ == "__main__":
    numbers_range = (0, 3000)
    for i in range(500, 4000 + 100, 100):
        all_random = generate_random(i, numbers_range)
        reverse_sorted = generate_reverse_sorted(i, numbers_range)
        almost_sorted = generate_almost_sorted(i, numbers_range)

        for prefix, data in (
            ("all_random", all_random),
            ("reverse_sorted", reverse_sorted),
            ("almost_sorted", almost_sorted)
        ):
            with open(f"generated_data/{prefix}_{i}.txt", "w") as f:
                f.write(" ".join(map(str, data)))
