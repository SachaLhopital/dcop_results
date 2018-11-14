import matplotlib.pyplot as plt

###### Droite

nb_agents = [1,2,3,4,5,6,7,8,9,10]

#plt.subplot(222)
yellow_lg_time, = plt.plot(
    nb_agents,
    [37.026, 36.652, 51.212, 37.476, 37.214, 37.094, 33.712, 36.762, 36.696, 37.22],
    '-y',
    label='3 Rpi + 7 W'
)

green_lg_time, = plt.plot(
    nb_agents,
    [494.36, 498.426, 328.65, 329.212, 366.686, 488.216, 533.078, 528.898, 329.216, 366.066],
    '-.g',
    label='3 Rpi + 7 QEMU'
)
plt.xlabel('Agent number')
plt.ylabel('Exec. time (s)')
#plt.title('B : Execution time comparison \n between the deployed system and QEMU simulations \n for 10 agents')
plt.legend(
    handles=[yellow_lg_time, green_lg_time]
)
plt.savefig('output/qemu_vs_python_B.png')
plt.show()

#plt.subplot(224)
plt.plot(
    nb_agents,
    [260.88, 256.68, 3874.73, 532.27, 23.8, 8.56, 42.88, 34.24, 15.34, 44.55],
    '-y',
    label='3 Rpi + 7 W'
)

plt.plot(
    nb_agents,
    [494.36, 498.426, 328.65, 329.212, 366.686, 488.216, 533.078, 528.898, 329.216, 366.066],
    '-.g',
    label='3 Rpi + 7 QEMU'
)

plt.xlabel('Agent number')
plt.ylabel('Msg Size (bytes)')
#plt.title('D : Average Message size \n received for 10 agents', loc='center')
plt.legend(
    handles=[yellow_lg_time, green_lg_time]
)

plt.savefig('output/qemu_vs_python_D.png')
plt.show()


###### Gauche

nb_agents = [1,2,3,4,5,6]

#plt.subplot(221)
red_lg_time, = plt.plot(
    nb_agents,
    [4.546, 4.688, 4.576, 3.76, 4.856, 5.15],
    '-r',
    label='3 Rpi + 3 W'
)

brown_lg_time, = plt.plot(
    nb_agents,
    [39.75, 36.182, 42.17, 40.76, 36.598, 39.126],
    '-.',
    color="brown",
    label='3 Rpi + 3 QEMU'
)

plt.xlabel('Agent number')
plt.ylabel('Exec. time (s)')
#plt.title('A : Execution time comparison \n between the deployed system and QEMU simulations \n for 6 agents')
plt.legend(
    handles=[red_lg_time, brown_lg_time]
)
plt.savefig('output/qemu_vs_python_A.png')
plt.show()

#plt.subplot(223)
plt.plot(
    nb_agents,
    [250.39, 360.35, 250.39, 20.68, 48.11, 20.68],
    '-r'
)

plt.plot(
    nb_agents,
    [48.58, 31.39, 25.1, 20.45, 306.45, 255.02],
    '-.',
    color='brown'
)
plt.xlabel('Agent number')
plt.ylabel('Msg Size (bytes)')
#plt.title('C : Average Message size \n received for 6 agents', loc='center')
plt.legend(
    handles=[red_lg_time, brown_lg_time]
)

plt.savefig('output/qemu_vs_python_C.png')
plt.show()