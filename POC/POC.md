## <p align=center>Proof Of Concept
</p>

<p align=center>All the resources required to demostrate a full proof of concept!!</p>

## Table Of Contents
>- [Overview](#overview) 

>- [System Diagram](#system-diagram)
>    - [Hardware and Software Setup](#hardware-and-software-setup)
>   - [Touchscreen Setup](#touchscreen-display-setup)


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