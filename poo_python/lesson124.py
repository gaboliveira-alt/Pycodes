
class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording
    
    
    def record(self):
        if self.recording:
            print(f'{self.name} JÁ está filmando...')
            return
        
        print(f'{self.name} está filmando...')
        self.recording = True
    
    
    def stop_recording(self):
        if not self.recording:
            print(f'{self.name} NÃO está filmando...')
            return
        
        print(f'{self.name} parou de filmar...')
        self.recording = False
    
    
    def photographing(self):
        if self.recording:
            print(f'{self.name} está filmando, não pode fotografar...')
            return
        
        print(f'{self.name} começou a fotografar...')


cam1 = Camera('Canon')
cam1.record()
cam1.record()
cam1.photographing()
cam1.stop_recording()
cam1.photographing()

print()

cam2 = Camera('Panasonic')
cam2.stop_recording()
cam2.record()
cam2.record()
cam2.photographing()
cam2.stop_recording()
cam2.photographing()