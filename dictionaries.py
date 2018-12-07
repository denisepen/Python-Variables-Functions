# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# like ruby hashes and js objects

person = {
'first_name': 'Dee',
'last_name': 'Doe',
'age': 39
}

print(person['age'])
print(person.get('last_name'))

# add key value
person['height'] = 5.5
print(person)
