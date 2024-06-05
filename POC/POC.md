## <p align=center>Proof Of Concept
</p>

<p align=center>All the resources required to demostrate a full proof of concept!!</p>

## Table Of Contents
>- [Overview](#overview) 

>- [System Diagram](#system-diagram)
>    - [Hardware and Software Setup](#hardware-and-software-setup)
>   - [Touchscreen Setup](#touchscreen-display-setup)
>- [Media Assests](#media-assests)
>- [Codes](#codes)

## Overview
> In this Proof Of Concept, there will be a master station which will be shared among all teams 




## Hardware and Software Setup

### System Diagram
```mermaid
graph LR
A[Raspberry Pi] --OSC--> B[Reaper DAW] --DANTE VSC--> C[L-ISA Processor] --Meta Data--> D[L-ISA Controller]--DANTE--> E[Yamaha QL1] --DANTE--> F[Speakers]
A --OSC--> G[GrandMA3] --SCAN--> H[Moving Lights]
```

### Touchscreen Display Setup

> 1. On the Raspberry Pi 3 7" Touchscreen Display, gently remove the black tabs of the ribbon cable connector simultaneously

<p align = center >
<img src = "./Media Assests/ribbonconnector.png">
</p>

> 2. Insert the ribbon cable into the connector with the blue side down. 
>Push the connector's black tabs back in to secure it.

<p align = center >
<img src="./Media Assests/ribbon-cable-connection.png">
</p>


>3.  Connect the wires as such:
> * Red jumper wire to 5V on the display board
> * Green jumper wire to SDA on the display board
> * Yellow jumper wire to SCL on the display board
> * Black jumper wire to GND on the display board

<p align = center >
<img src="./Media Assests/7inch-screen-jumper-wire-connections.png">
</p>

> 4. On the Raspberry Pi, Connect the following:
> * Red jumper wire to 5V (either pin 2 or pin 4) on the Raspberry Pi
> * Green jumper wire to GPIO 2 (Pin 3) on the Raspberry Pi
> * Yellow jumper wire to GPIO 3 (Pin 5) on the Raspberry Pi
> * Black jumper wire to Ground (any ground pin) on the Raspberry Pi 

<p align = center >
<img src="./Media Assests/pi4_gpio.png">
</p>

> 5. Boot up your Raspberry Pi and the display touchscreen should work!

## Media Assests

> All the media assests utilised in this POC include:
>
> [Legend Board](./Media%20Assests/Legend%20Board.png) - Poster with the coded messages to decipher

<img src = "./Media Assests/Legend Board.png">

> [Audio Files](./Audio%20Files/AudioFiles.zip) - zip file with all the audio files used in this POC demostration

> [Reaper]() - Master Reaper file used

>[GrandMA3]() - Master MA3 file used with the correct patching of lights

## Codes
> In **[this folder](./Codes)** , there are mainly 3 python files, all of which are needed to run and showcase the demostration smoothly.

> 1. [numblock_gui.py](./Codes/numblock_gui.py) - main file and GUI that trigger the functions to be called from the other files.
> 2. [dawcontrol.py](./Codes/dawcontrol.py) - python file to jump to various markers and allow of play/pause of track.
> 3. [ma3control.py](./Codes/ma3control.py) - python file to trigger sequences in GrandMA3 software and also clear them afterwards. 



