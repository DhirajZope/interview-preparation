def sq_gen(lst):
    for n in lst:
        yield n*n


arr = [1,2,3,4,5]

sq = sq_gen(arr)
# print(sq)
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())

for s in sq:
    print(s)


