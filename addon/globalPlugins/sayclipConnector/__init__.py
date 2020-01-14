# copyright tiflojuegos.com
# based on clipcopy, translate and other stuff
# plugin dessigned to connect NVDA with sayclip

import globalPluginHandler
import ui
import tones
import speech
import api


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.data = ''
        self.oldSpeak = speech.speak
        self.active = False

    def mySpeak(self, text, *args, **kwargs):
        tones.beep(500, 80)
      
        self.data = text
      
        self.oldSpeak(text, *args, **kwargs)

    def script_toggleCommunication(self, gesture):
        self.active = not self.active
        if(self.active):
            self.oldSpeak('conectandose a sayclip')
            speech.speak = self.mySpeak
            tones.beep(800, 100)
            tones.beep(1500, 100)
        else:
            self.oldSpeak('desconectandose de sayclip')
            speech.speak = self.oldSpeak
            tones.beep(800, 120)
            tones.beep(800, 120)

    def terminate(self):
        if(self.active):
            speech.speak = self.oldSpeak

    __gestures = {
        "kb:nvda+control+,":"toggleCommunication",
    }
