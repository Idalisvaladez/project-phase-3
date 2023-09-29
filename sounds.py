import simpleaudio as sa

wav_object = sa.WaveObject.from_wave_file("Sounds/Prison_Cell_Door.wav")
play_object = wav_object.play()
play_object.wait_done()