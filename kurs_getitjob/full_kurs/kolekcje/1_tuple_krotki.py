# tuple - niezmienna, indeksowana od zera, dopuszcza powtórzenia

t1 = (1, 1.6, 'adam')
t2 = (2, )

print(type(t1))
print(t1[2])
print(t1[-2])


lap_times = ('Lewis Hamilton', 78.89, 79.99, 79.99, 80.89, 80.84)

print(lap_times[0])
print(lap_times[1:])
print((lap_times[3:5]))
print(lap_times.count(79.99))
print(lap_times.index('Lewis Hamilton'))

time_sum = 0
for x in lap_times[1:]:
    time_sum += x
print(time_sum)

time_sum = print(sum(lap_times[1:]))


nowa_tupla = lap_times + (81.20, 79.01)
print(nowa_tupla[1:])
