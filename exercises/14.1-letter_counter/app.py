par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
def counter_letter(str):
    for letter in str.lower():
        if letter != " ":
            if letter in counts:
                counts[letter] += 1
            else: counts[letter] = 1
            

print(counter_letter(par))

print(counts)
