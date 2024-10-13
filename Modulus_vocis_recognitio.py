from vosk import Model, KaldiRecognizer
import pyaudio
import json

def Vox(disc:int,model:str,buffer): 
    rec = KaldiRecognizer(Model(model), disc)  
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=disc,  
        input=True,
        frames_per_buffer=8000)
    
    stream.start_stream()
    
    while True:
        try:
            data = stream.read(8000)    
                    
            if len(data) == 0: break
            
            if rec.AcceptWaveform(data):
                item=json.loads(rec.Result())
                print(item["text"])
                buffer.put(item["text"])
            else: 
                pass
                # buffer.put(rec.PartialResult())
            
        except: print("Error 1")
        
    stream.stop_stream()
    stream.close()
    p.terminate()
    

if __name__=="__main__":
    import settings
    buffer=set()
    Vox(disc=settings.disc,model=settings.model["en"],buffer=buffer)    