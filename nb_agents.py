import matplotlib.pyplot as plt

nb_agents = [2, 6, 10, 16, 20, 26, 30, 36, 40, 46, 50]

plt.plot(nb_agents, [40, 80, 128.2, 1834.6, 2012, 1328, 2108, 8221.3, 2418.875, 8692.2, 16947.2], '-y')
plt.plot(nb_agents, [76, 101, 112, 1553, 1863, 1402, 1601, 12086, 2363, 6396, 11906], '-b')
plt.plot(nb_agents, [76, 95, 169, 2242, 1749, 1388, 1202, 13017, 3058, 6493, 12154], '-c')

plt.title('Execution time depending on number of agents with Frodo', loc='center')
plt.xlabel('Number of agents')
plt.ylabel('Execution time (s)')

plt.savefig('output/nb_agents.png')
plt.show()