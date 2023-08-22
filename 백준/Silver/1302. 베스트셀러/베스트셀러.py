n = int(input())
books = {}

for _ in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

sorted_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(sorted_books[0][0])