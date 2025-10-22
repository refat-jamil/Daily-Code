# Python dose not have bult-in support for Arrays. but Python List can be used instead.

# What is list?
# List are used to store multiple items in a single variable

courses = ['History', 'Math', 'Physics', 'ComSci']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:3])
print(courses[2:])
courses.append('Art')
print(courses)
courses.insert(3, 'Chem')
print(courses)

courses_2 = ['ICT', 'Bio']

print(courses_2)
print(courses, courses_2)
courses.append(courses_2)
print(courses)
courses.insert(len(courses), courses_2)
print(courses)
courses.extend(courses_2)
print(courses)
courses.remove('Math')
print(courses)
courses.pop()
print(courses)
p = courses.pop()
print(p)
print(courses)


courses = ['History', 'Math', 'Physics', 'ComSci']
courses.reverse()


nums = [1, 2, 3, 4, 5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)



nums = [100, 250, 370, 4, 50]
sorted_list = sorted(nums)
print(sorted_list)
max_nums = max(nums)
print(max_nums)
sum_nums = sum(nums)
print(sum_nums)




courses = ['History', 'Math', 'Physics', 'ComSci']
print(courses.index("Physics"))
print('Physics' in courses)
print('Chemistry' in courses)


courses = ['History', 'Math', 'Physics', 'ComSci']
for subject in courses:
    print(subject)


courses = ['History', 'Math', 'Physics', 'ComSci']
for index, subject in enumerate(courses):
    print(index, '-', subject)


courses = ['History', 'Math', 'Physics', 'ComSci']
course_str = ', '.join(courses)
print(course_str)
print(type(course_str))

new_list = course_str.split(', ')
print(course_str)
print(new_list)

 
print(max(12, 100, 222))