import librosa, winsound
import matplotlib.pyplot as plt

song = input('\nEnter song name: ')
y, sr = librosa.load(f'input/{song}.mp3')

scale = 5000
y = y[::sr]

for i, j in enumerate(y):
    frequency = scale + int(scale*j)
    print(i, frequency)
    plt.scatter(i, frequency)
    winsound.Beep(frequency, 1000)
    plt.pause(0.1)

plt.show()
