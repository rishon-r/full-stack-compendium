# FACADE PATTERN

# The Facade pattern provides a simple, unified interface to a complex subsystem — hiding all the messy details behind a clean front-facing class.
# The caller needs to know about every class, every step, and the correct order. That's a lot of knowledge to expose

# E.g

# Without a facade — caller has to manage everything themselves
'''
audio = AudioDecoder()
audio.load("song.mp3")
audio.decompress()

buffer = AudioBuffer()
buffer.allocate(1024)
buffer.fill(audio.get_data())

output = AudioOutput()
output.connect()
output.set_volume(80)
output.stream(buffer)

'''
# With facade

# E.g

'''
player = MusicPlayer()
player.play("song.mp3")  # all that complexity hidden behind one call

'''

# FULL EXAMPLE

# Complex subsystem classes
class AudioDecoder:
    def load(self, file: str) -> str:
        print(f"Decoding {file}")
        return "raw_audio_data"

class AudioBuffer:
    def allocate(self, size: int) -> None:
        print(f"Allocating buffer of {size}")

    def fill(self, data: str) -> None:
        print(f"Filling buffer with {data}")

class AudioOutput:
    def connect(self) -> None:
        print("Connecting to audio output")

    def set_volume(self, level: int) -> None:
        print(f"Setting volume to {level}")

    def stream(self, buffer: AudioBuffer) -> None:
        print("Streaming audio")


# The Facade — hides all of the above
class MusicPlayer:
    def __init__(self):
        self.decoder = AudioDecoder()
        self.buffer = AudioBuffer()
        self.output = AudioOutput()

    def play(self, file: str) -> None:
        data = self.decoder.load(file)
        self.buffer.allocate(1024)
        self.buffer.fill(data)
        self.output.connect()
        self.output.set_volume(80)
        self.output.stream(self.buffer)


# Main — caller only ever touches the facade
player = MusicPlayer()
player.play("song.mp3")
