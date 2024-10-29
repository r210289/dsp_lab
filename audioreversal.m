[y, fs] = audioread('/home/rguktrkvalley/AllClLabPrograms/Classical.wav');
reversed_y = y(end:-1:1);
sound(reversed_y, fs);
