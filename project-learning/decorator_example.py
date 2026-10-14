import time

def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}: {time.time()-start:.2f}s")
        return result
    return wrapper

@timer
def load_data():
    print("Loading data...")
    time.sleep(1)

# • @timer = load_data = timer(load_data) ka shortcut.
# • *args, **kwargs se wrapper kisi bhi function par chalta hai.
# • Original ka naam bachane ke liye functools.wraps lagao.
# • Real use: logging, retry, auth check, caching (@lru_cache), FastAPI ke @app.get.