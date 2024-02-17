# Frequency-Extraction-Signal-Processing

    This Script is able to extract Frequency of the voice detected in an audio file (preferred in ".mp3" filetype)

<br>

![system sound](https://github.com/imvickykumar999/Frequency-Extraction-Signal-Processing/assets/50515418/73649166-23ae-44c6-9578-6e2584bbfd0f)
![Saiyyan](https://github.com/imvickykumar999/Frequency-Extraction-Signal-Processing/assets/50515418/e0756cb4-1814-4c67-b425-9713111c4760)

<br>

```python
import librosa, winsound, json
import matplotlib.pylab as plt

song = input('\nEnter song name: ')
scale = 5000

def save_plot(filename):
    y, sr = librosa.load(filename)
    plt.figure(figsize=(20, 10))
    plt.title(song)
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(y)
    plt.savefig(f'output/{song}.png')
    return y, sr

y, sr = save_plot(f'input/{song}.mp3')
dictionary = {}

for i, j in enumerate(y[::sr]):
    try:
        duration = 1000 # 1 sec
        frequency = scale + int(scale*j)

        winsound.Beep(frequency, duration)
        print(i, 'sec. ', int(scale*(1 + j)), 'Hz.')

    except:
        pass

    dictionary.update({i: scale*(1 + j)})
json_object = json.dumps(dictionary, indent=4)
 
with open(f'output/{song}.json', "w") as outfile:
    outfile.write(json_object)

print('\n', len(y), '/', sr, '=', len(y)/sr, 'seconds')
```
