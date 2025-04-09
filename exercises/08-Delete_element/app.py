people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    new_lis_people = []
    for i in people:
        if i != person_name:
            new_lis_people.append(i)
    return new_lis_people
    

    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
