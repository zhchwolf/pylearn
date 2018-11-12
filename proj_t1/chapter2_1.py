from recommendations import critics
from recommendations import sim_distance
from math import sqrt

print(critics['Lisa Rose']['Lady in the Water'])
print(critics['Toby'])
print(critics['Mick LaSalle'])
print(sqrt(pow(4.5-4, 2) + pow(1-2, 2)))
dis_large = 1/(1+sqrt(pow(4.5-4, 2) + pow(1-2, 2)))
print(dis_large)

sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
