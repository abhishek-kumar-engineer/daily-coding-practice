def read_rows(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for row in read_rows('big.csv'):
    process(row)


# • Lazy evaluation: value tab banti hai jab maangi jaye.
# • Memory O(1) vs list O(n).
# • Generator expression: (x*x for x in data) ([] ki jagah ()).
# • Real use: bade datasets ko batch me model ko dena (data loader), streaming LLM response.
# • Limit: sirf ek baar iterate hota hai.
