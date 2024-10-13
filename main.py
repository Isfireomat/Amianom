import settings
import multiprocessing
from Modulus_vocis_recognitio import Vox
from Modulus_transmutator import Transmutator

def prin(buffer):
    while True:
        if not buffer.empty():
            Transmutator(buffer.get())
            
            
if __name__=="__main__":
    
    buffer=multiprocessing.Queue()    

    p1= multiprocessing.Process(target=Vox, kwargs={"disc":settings.disc,
                                                    "model":settings.model["ru"],
                                                    "buffer":buffer})

    p2= multiprocessing.Process(target=prin, kwargs={"buffer":buffer})

    p1.start()
    p2.start()
    p1.join()