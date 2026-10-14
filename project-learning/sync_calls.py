import time

def call_api(i):
    time.sleep(1)  # fake API call
    return i

start = time.time()
results = [call_api(i) for i in range(10)]
print(f"Time: {time.time() - start:.2f}s")