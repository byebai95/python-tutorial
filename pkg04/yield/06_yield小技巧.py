def generate_numbers():
    for i in range(10):
        yield i


# for num in generate_numbers():
#     print(num)

# print(list(generate_numbers()))
gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

