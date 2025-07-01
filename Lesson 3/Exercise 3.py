import time

start_time = time.time()
timeout = 5  # seconds

while time.time() - start_time < timeout:
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    time.sleep(1)

total_time = time.time() - start_time
print(f"Exiting the loop. Total time elapsed: {total_time:.2f} seconds")