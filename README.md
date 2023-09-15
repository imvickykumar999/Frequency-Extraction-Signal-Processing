# Frequency-Extraction-Signal-Processing

    This Script is able to extract Frequency of the voice detected in an audio file (preferred in ".wav" filetype)

<br>

>![ss](https://github.com/imvickykumar999/Frequency-Extraction-Signal-Processing/blob/main/extras/Screenshot%202023-09-15%20162146.png?raw=true)

<br>

```python
import librosa, winsound
import matplotlib.pylab as plt

def save_plot(filename):
    y, sr = librosa.load(filename)        
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(y)
    plt.savefig('test.png')
    return y, sr

y, sr = save_plot('test.wav')
# https://youtu.be/S0nOYs0PRak

scale = 5000
with open('test.txt', 'w') as f:
    for i, j in enumerate(y[::sr]):
        try:
            duration = 1000 # 1 sec
            frequency = scale + int(scale*j)

            winsound.Beep(frequency, duration)
        except:
            pass

        print(i, scale*(1 + j))
        f.write(f'{j}, ')

print(len(y), sr, len(y)/sr, 'seconds')
# 80000 22050 3.6281179138321997 seconds
# ValueError: frequency must be in 37 thru 32767

# The variable sr contains the sampling rate of y , 
# that is, the number of samples per second of audio.
```
