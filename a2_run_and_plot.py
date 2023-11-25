import sys
import subprocess
import matplotlib.pyplot as plt


def compile():
    with subprocess.Popen(
        "rustc a2.rs".split(),
        stdout=sys.stdout,
        stderr=sys.stderr,
    ) as process:
        process.wait()
        if process.returncode != 0:
            raise RuntimeError("Compilation of sorting programm failed")


def run_test(sort_type: str, input_file: str, threshold: int | None = None) -> int:
    with subprocess.Popen(
        ["./a2", sort_type, input_file] + ([str(threshold)] if threshold else []),
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        universal_newlines=True,
    ) as process:
        process.wait()
        if process.returncode != 0:
            raise RuntimeError(f"Sorting programm didn't finish successfuly on test {input_file}")
        output = int(process.stdout.read().strip())       

    return output


if __name__ == "__main__":
    compile()
    prefixes = "all_random", "reverse_sorted", "almost_sorted"
    data_range = range(500, 4000 + 100, 100)
    for test_case in prefixes:
        y = []
        for size in data_range:
            elapsed_micros = run_test("standart", f"generated_data/{test_case}_{size}.txt")
            y.append(elapsed_micros)

        plt.title(f"Standart merge sort: {test_case}")
        plt.xlabel("Array size")
        plt.ylabel("Working time (microseconds)")
        plt.scatter(data_range, y)
        plt.show()
        
    for test_case in prefixes:
        for threshold in (5, 10, 20, 50):
            y = []
            for size in data_range:
                elapsed_micros = run_test("standart", f"generated_data/{test_case}_{size}.txt", threshold)
                y.append(elapsed_micros)

            plt.title(f"Hybrid merge sort: {test_case}, with threshold for insertion sort -- {threshold}")
            plt.xlabel("Array size")
            plt.ylabel("Working time (microseconds)")
            plt.scatter(data_range, y)
            plt.show()

