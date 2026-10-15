import openjij as oj

N = 5
h = {i: -1 for i in range(N)}
J = {(i, j): -1 for i in range(N) for j in range(i+1, N)}

print('H_i:', h)
print('J_ij:', J)

sampler = oj.SASampler()
response = sampler.sample_ising(h, J, num_reads=1)

print(response.states)

print([s for s in response.samples()])

