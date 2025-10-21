# A set is a collection which is unordered, unchangeable*, and unindexed.


courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'}

print(courses)


cs_courses = {'History', 'Math', 'Physics', 'ComSci'}
art_courses = {'History', 'Math', 'Art', 'Bnagla'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
