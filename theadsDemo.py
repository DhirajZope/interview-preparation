import time
import threading as th
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"Sleeping for {secs} second(s)...")
    time.sleep(secs)
    # print(f"Done Sleeping {secs} second(s)...")
    return f"Done Sleeping {secs} second(s)....."

# do_something()
# do_something()

# t1 = th.Thread(target=do_something)
# t2 = th.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # print(f1.result())
    # print(f2.result())


# threads = []
# wait = [5, 4, 3, 2, 1]

# for _ in range(5):
#     t = th.Thread(target=do_something, args=[wait[_]])
#     t.start()
#     threads.append(t)


# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)...')