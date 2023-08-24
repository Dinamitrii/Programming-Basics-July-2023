import time

def time_execution(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Example function to be timed
def example_function():
    nums = {num: num for num in range(1, 150_000_000)}
    searched_number = 1_999_999

    if searched_number in nums.keys():
        return


def function_with_get():
    nums = {num: num for num in range(1, 150_000_000)}
    searched_number = 1_999_999

    return nums.get(searched_number)


execution_time = time_execution(example_function)
print(f"Execution time: {execution_time:.6f} seconds")

print()
print()

execution_time = time_execution(function_with_get)
print(f"Execution time: {execution_time:.6f} seconds")
