N = int(input())

members = [tuple([int(age), name]) for age, name in (input().split() for _ in range(N))]
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])