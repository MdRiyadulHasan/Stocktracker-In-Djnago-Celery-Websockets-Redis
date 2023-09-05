# import threading
# import time

# # Define a function that will be run by each thread
# def worker_function(thread_id):
#     print(f"Thread {thread_id} is starting... \n ")
#     sum = 0
#     for i in range(200):
#         sum = sum+i
#     print(f"Thread {thread_id} is Finished sum is : {sum} \n ", )
#     time.sleep(2)
#     print(f"Thread {thread_id} is done. \n ")

# # Create multiple threads
# threads = []

# for i in range(8):
#     thread = threading.Thread(target=worker_function, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()

# print("All threads have finished.")
# import threading

# # Define a simple function that will run in a thread
# def print_numbers():
#     for i in range(1, 18):
#         print(f"Number { i }")

# # Define another function to print letters
# def print_letters():
#     for letter in 'ABCDEFGHJKKIIY':
#         print(f"Letter {letter }")

# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Both threads have finished.")

import multiprocessing

# Define a function to perform some computation
def worker_function(number):
    result = number * 2
    print(f"Worker {number}: Result is {result}")

if __name__ == "__main__":
    # Create a list of numbers to process
    numbers_to_process = [1, 2, 3, 4, 5]

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Map the worker function to the list of numbers
    pool.map(worker_function, numbers_to_process)

    # Close the pool and wait for all processes to complete
    pool.close()
    pool.join()

    print("All processes have finished.")
