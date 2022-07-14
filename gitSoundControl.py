inf="""This sets and get the System Master Volume"""

from tkinter import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

#--- THIS IS FOR THE INITIALIZATION OF THE SOUND MODULE ---
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#----------------------------------------------------------

def getCurrentMasterVolume():
    return int(round(volume.GetMasterVolumeLevelScalar() * 100))

def displayCurrentVolume():
    selection = str(getCurrentMasterVolume()) + "%"
    label.config(text = selection)

def setMasterVolume(self):
    scalarVolume = int(var.get()) / 100
    volume.SetMasterVolumeLevelScalar(scalarVolume, None)
    displayCurrentVolume()

def mute(boolMute):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        print("volume.GetMute(): %s" % volume.GetMute())
        volume.SetMute(boolMute, None)

def toggle():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if toggleBtn.config('text')[-1] == 'Mute Off':
        toggleBtn.config(text='Mute On')
        mute(1)
    else:
        toggleBtn.config(text='Mute Off')
        mute(0)


root = Tk(className="\Windows Master Volume Manager")
root.geometry("500x200")

#SCALE COMPONENT
var = IntVar()
var.set(getCurrentMasterVolume())
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, variable=var, showvalue=0, command=setMasterVolume)
scale.pack(anchor=CENTER)

#LABEL component
label = Label(root)
label.pack()

#TOGGLE BUTTON COMPONENT
toggleBtn = Button(text="Mute Off", width=12, command=toggle)
toggleBtn.pack(pady=5)

displayCurrentVolume()
root.mainloop()
