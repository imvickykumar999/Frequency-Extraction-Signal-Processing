
# https://colab.research.google.com/drive/1-Ilo-MFRbiCxiQEgAIcaU8TjvpHmMx-J#scrollTo=c0Mekc6Jw3ir

import librosa, winsound
import matplotlib.pylab as plt

song = input('Enetr song name: ')
scale = 5000

def save_plot(filename):
    y, sr = librosa.load(filename)        
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(y)
    plt.savefig(f'output/{song}.png')
    return y, sr

y, sr = save_plot(f'input/{song}.mp3')

with open(f'output/{song}.txt', 'w') as f:
    for i, j in enumerate(y[::sr]):
        try:
            duration = 1000 # 1 sec
            frequency = scale + int(scale*j)

            winsound.Beep(frequency, duration)
        except:
            pass

        print(i, 'sec. ', scale*(1 + j), 'Hz.')
        f.write(f'{j}, ')

print('\n', len(y), '/', sr, '=', len(y)/sr, 'seconds')
