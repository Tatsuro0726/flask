from model import db, Employee, Project, Company


# for e in Employee.query.all():
#     print(e.projects[0].name)

# e = Employee.query.first()
# print(e)
# print(e.company.name)
# print(e.projects[1].name)
# for p in e.projects:
#     print(p.name)

# Projectからの紐付け

# p = Project.query.get(1)
# print(p.employees.name)

# # Companyからの紐付け
# c = Company.query.get(2)
# print(c.employees.name)

# 紐付けの違い
e = Employee.query.first()
print(type(e.projects))
print(e.projects.order_by(Project.id.desc()).limit(1).first().name)