# python-shepard-tone-generator
python shepard tone generator


This Python script generates a *Shepard tone* composed of smooth beeping ticks, mimicking an infinitely ascending tone made of analog-style "bomb timer" ticks.



## 📦 Installation

```bash
pip install numpy
```
## Customization

You can customize the behavior of the Shepard tone by modifying the parameters at the top of the script.

| Variable        | Description                                              | Default  |
|----------------|----------------------------------------------------------|----------|
| `fs`           | Sampling rate in Hz                                      | `44100`  |
| `duration`     | Total duration of the generated audio in seconds         | `300.0`  |
| `n_tones`      | Number of sine waves spaced by octaves                   | `10`     |
| `base_freq`    | Base frequency of the Shepard tones in Hz                | `110`    |
| `tick_interval`| Time in seconds between each tick/beep                   | `1.0`    |
| `tick_dur`     | Duration of each tick sound in seconds                   | `0.1`    |

### Example: Longer duration and smoother ticking

```python
duration = 600.0        # 10 minutes
tick_interval = 2.0     # one tick every 2 seconds
tick_dur = 0.2          # longer, smoother ticks
base_freq = 55          # deeper tone
