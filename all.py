import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def subcategorybar(X, vals, legend_array, width=0.8):
    mean_values = vals.mean(axis=1)
    n = len(mean_values)
    _X = np.arange(len(X))

    print(mean_values[0])

    for i in range(n):
        plt.bar(X[i], mean_values[i], width=width/float(n), align='center')

    plt.xticks(_X, legend_array, rotation=90)


# Chambre
room_legend, = plt.plot([1,2,3,4,5,6], [4.546, 4.688, 4.576, 3.76, 4.856, 5.15], '-y', label='Room (6 agents)')

# Zone
zone_legend_6, = plt.plot([1,2,3,4,5,6], [2.29, 2.28, 2.45, 2.19, 2.46, 2.42], '-sb', label='Area (6 agents)')
zone_legend_4, = plt.plot([1,2,3,4], [1.43, 1.41, 1.49, 1.29], '-s', color='#FFA500', label='Area (4 agents)')

# Multi
multi_legend_6, = plt.plot([1,2,3,4,5,6], [50.26, 46.72, 47.69, 50.33, 44.04, 47.76], '-.c', label='Multivariable (6 agents)')
multi_legend_2, = plt.plot([1,2], [6.75, 8.81], '-.b', label='Multivariable (2 agents)')

plt.legend(handles=[room_legend, zone_legend_4, zone_legend_6, multi_legend_2, multi_legend_6])
#plt.title('Execution time comparison for 6 Rooms', loc='center')
plt.xlabel('Agent number')
plt.ylabel('Execution time (s)')

plt.savefig('output/all.png')
plt.show()

# Histogram
x = np.array([1, 2, 3, 4, 5, 6])
legend_array = (
        'a1 = Area Approach (6 Areas)',
        'a2 = Area Approach (4 Areas)',
        'a3 = Multivariable Approach (2 Areas)',
        'a4 = Room Approach',
        'a5 = Multivariable Approach (6 Areas)'
    )

subcategorybar(
    x,
    np.array([
        [1.43, 1.41, 1.49, 1.29, 1, 1],
        [2.29, 2.28, 2.45, 2.19, 2.46, 2.42],
        [6.75, 8.81, 1, 1, 1, 1],
        [4.546, 4.688, 4.576, 3.76, 4.856, 5.15],
        [50.26, 46.72, 47.69, 50.33, 44.04, 47.76]
    ]),
    [
        '',
        'a1',
        'a2',
        'a3',
        'a4',
        'a5'
    ]
)

## Legend
plt.plot([], [], '', label="a1 = Area Approache (6 Areas)")
plt.plot([], [], '', label="a2 = Area Approache (4 Areas)")
plt.plot([], [], '', label='a3 = Multivariable Approache (2 Areas)')
plt.plot([], [], '', label='a4 = Room Approache')
plt.plot([], [], '', label="a5 = Multivariable Approache (6 Areas)")
plt.legend()

#plt.title('Average execution time comparison for 6 Rooms', loc='center')
plt.ylabel('Average execution time (s)')
plt.savefig('output/all_histogram.png')
plt.show()