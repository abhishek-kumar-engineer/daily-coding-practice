import asyncio, time

async def call_api(i):
    await asyncio.sleep(1)  # fake API call
    return i

async def main():
    start = time.time()
    results = await asyncio.gather(*(call_api(i) for i in range(10)))
    print(f"Time: {time.time() - start:.2f}s")

asyncio.run(main())

# • async def coroutine banata hai, seedha call karne par chalta nahi.
# • await sirf async function ke andar.
# • asyncio.gather kai coroutines ek saath chalata hai.
# • Event loop ek thread me baari-baari se tasks switch karta hai.
# • Galti: time.sleep async me mat use karo, asyncio.sleep use karo; warna poora loop block.
# • Async CPU-heavy kaam tez nahi karta (uske liye multiprocessing).
# • Real use: LLM API calls, FastAPI endpoints, web scraping, DB queries.