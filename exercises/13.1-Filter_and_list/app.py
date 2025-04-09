all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def filter_names(name):
    return name[0]== "R"


result_filter_r = list(filter(filter_names, all_names))


print(result_filter_r)

