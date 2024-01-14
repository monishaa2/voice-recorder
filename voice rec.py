import sounddevice as sd
import wavio
import os

class VoiceRecorder:
    def __init__(self):
        self.sampling_frequency = 44100
        self.channels = 1
        self.duration = 5  # seconds
        self.output_folder = "recordings"
        self.current_recording = None

    def start_recording(self):
        print("Recording...")
        self.current_recording = sd.rec(int(self.sampling_frequency * self.duration),
                                        samplerate=self.sampling_frequency, channels=self.channels, dtype='int16')
        sd.wait()
        print("Recording stopped.")

    def save_recording(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        file_name = input("Enter a file name (without extension): ")
        file_path = os.path.join(self.output_folder, f"{file_name}.wav")

        wavio.write(file_path, self.current_recording, self.sampling_frequency, sampwidth=3)
        print(f"Recording saved as {file_path}")

    def run(self):
        self.start_recording()
        self.save_recording()

if __name__ == "__main__":
    VoiceRecorder().run()
