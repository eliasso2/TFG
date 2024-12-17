import Simplex as sim

v1 = sim.Simplex(0)
v2 = sim.Simplex(0)
v3 = sim.Simplex(0)
v4 = sim.Simplex(0)

s1 = sim.Simplex(1, [v1, v2])
s2 = sim.Simplex(1, [v2, v3])
s3 = sim.Simplex(1, [v3, v4])
s4 = sim.Simplex(1, [v4, v1])
s5 = sim.Simplex(1, [v1, v3])
s6 = sim.Simplex(1, [v2, v4])

c1 = sim.Simplex(2, [s1, s4, s6])
c2 = sim.Simplex(2, [s2, s3, s6])
c3 = sim.Simplex(2, [s1, s2, s5])
c4 = sim.Simplex(2, [s3, s4, s5])

T1 = sim.Simplex(3, [c1, c2, c3, c4])

print(T1.dim)
print(T1.cares)

for c in T1.cares:
    print(c)
    print('Dimensió')
    print(c.dim)

    for s in c.cares:
        print(s)
        print('Dimensió')
        print(s.dim)

        for v in s.cares:
            print(v)
            print('Dimensió')
            print(v.dim)
            print('')