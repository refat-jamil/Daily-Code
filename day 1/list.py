# Python dose not have bult-in support for Arrays. but Python List can be used instead.

# What is list?
# List are used to store multiple items in a single variable

courses = ['History', 'Math', 'Physics', 'ComSci']

# print(courses)

# print(len(courses))

# print(courses[0])

# print(courses[3])

# print(courses[-1])

# print(courses[0:3])

# print(courses[2:])

# courses.append('Art')

# print(courses)

# courses.insert(3, 'Chem')

# print(courses)

courses_2 = ['ICT', 'Bio']

# print(courses_2)

# print(courses, courses_2)

# courses.append(courses_2)

# print(courses)

# courses.insert(len(courses), courses_2)

# print(courses)

courses.extend(courses_2)

print(courses)

courses.remove('Math')

print(courses)

courses.pop()

print(courses)

p = courses.pop()

print(p)
print(courses)
