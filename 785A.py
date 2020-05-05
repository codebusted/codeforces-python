
def polyhedron(s):
    if s == "Tetrahedron":
        return 4
    elif s == "Cube":
        return 6
    elif s == "Octahedron":
        return 8
    elif s == "Dodecahedron":
        return 12
    else:
        return 20

n = int(input())
result = 0
for i in range(n):
    s = str(input())
    result = result + polyhedron(s)

print(result)