import numpy as np
import wave

# ─── PARAMETERS ─────────────────────────────────────────────────────────
fs = 44100           # sample rate
duration = 300.0      # total length in seconds
n_tones = 10         # octave‐spaced voices
base_freq = 110      # reference pitch (Hz)
tick_interval = 1.0  # seconds between ticks
tick_dur = 0.1       # tick length (s) – longer for a smoother click

# ─── TIME AXIS ──────────────────────────────────────────────────────────
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

# ─── CONTINUOUS SHEPARD TONE ────────────────────────────────────────────
y_cont = np.zeros_like(t)
for i in range(n_tones):
    off = i - (n_tones-1)/2
    freq = base_freq * 2**(off + t/duration)          # glide up one octave
    amp  = np.exp(-0.5 * (off/(n_tones/2))**2)        # Gaussian envelope
    y_cont += amp * np.sin(2*np.pi*freq*t)
y_cont /= np.max(np.abs(y_cont))

# ─── SMOOTH TICK ENVELOPE ───────────────────────────────────────────────
tick_len = int(tick_dur * fs)
hann_env = np.hanning(tick_len)                       # smooth ramp up/down
env = np.zeros_like(t)
for tk in np.arange(0, duration, tick_interval):
    pos = int(tk * fs)
    end = pos + tick_len
    if end < len(env):
        # overlay window (max in case of any overlap)
        env[pos:end] = np.maximum(env[pos:end], hann_env)
env /= np.max(env)                                    # normalize 0→1

# ─── GATED (TICKING) SHEPARD ────────────────────────────────────────────
y = y_cont * env
y /= np.max(np.abs(y))

# ─── WRITE WAV ──────────────────────────────────────────────────────────
data = (y * 32767).astype(np.int16)
with wave.open('shepard_tone.wav', 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(data.tobytes())

print("WAV written: shepard_tone.wav")
