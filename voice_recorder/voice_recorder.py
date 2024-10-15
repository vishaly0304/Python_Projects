# Import necessary libraries
import sounddevice as sd
from scipy.io.wavfile import write

# Define a function to record audio
def record_audio():
    # Prompt user to enter the duration for recording
    seconds = int(input("How many seconds do you need to record: "))
    
    # Notify user that recording has started
    print("Recording Started...")
    
    # Record the audio for the specified duration
    # 48000 is the sampling rate, channels=2 means stereo recording
    recording = sd.rec(int(seconds * 48000), samplerate=48000, channels=2)
    
    # Wait for the recording to finish
    sd.wait()
    
    # Prompt user to enter a file name to save the recording
    file_name = input("Give file name to save the file: ")
    
    # Write the recorded audio data to a file
    # 48000 is the sampling rate used for recording
    write(file_name, 48000, recording)
    
    # Notify user that recording is done
    print("Recording Done...")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the record_audio function
    record_audio()