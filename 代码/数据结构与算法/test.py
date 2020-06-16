# 1. O(n)
arr = [1, 3, 8, 4, 5]
arr.reverse()
print(arr)

# arr[::-1]
# # print(arr)


# 2.

l = [1, 3, 3, 2, 5, 8, 2, 1, 9]

print(list(set(l)))


# 3.
# 时间复杂度O(n) 空间复杂是O(n)
ids = [1, 3, 3, 2, 5, 8, 2, 1, 9]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)
