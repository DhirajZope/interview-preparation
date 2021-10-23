import time
# import multiprocessing as mp
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    # print(f"Done sleeping for {seconds} second(s)...")
    return f"Done sleeping for {seconds} second(s)..."

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]

    results = executor.map(do_something, secs)

    # p1 = executor.submit(do_something, 1)
    # p2 = executor.submit(do_something, 1)

    # print(p1.result())
    # print(p2.result())

# for f in concurrent.futures.as_completed(results):
#     print(f.result())

for result in results:
    print(result)

# processes = []

# for _ in range(10):
#     p = mp.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)


# p1.start()
# p2.start()

# p1.join()
# p2.join()

# do_something()
# do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)}")