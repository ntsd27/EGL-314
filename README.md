#
<h1 align="center">
  <img src="./Media Assests/NanyangPolyLogo.png" width = 350px height=170px>
</h1>

<h1 align="center">
  Project S.O.N.I.C - Reaction Training
</h1>


 
<p align="center">
  <a href="https://github.com/ntsd27/EGL314/commits/main"><img src="https://img.shields.io/github/last-commit/ntsd27/EGL-314.svg?style=for-the-badge"/></a>
</p>

## Table of Contents
> - [Overview](#overview)
> - [Station Game](#station-game)
> - [Dependencies](#dependencies)
> - [Pre-Requisites](#pre-requisities)
> - [Setting Up](#setting-up)
> - [References](#references)
> - [Contributors](#contributors)


## Overview
> Project S.O.N.I.C (Sensory Observation Ninja Immersive Challenge) is an experiential/exploratory initiative designed to blend the ancient "ninja training techniques" with modern technology. Students will design a range of interactive stations that simulate ninja training scenarios which are designed to test and enhance particpants listening abilities, reaction time and memory, The stations includes: 

1. Stealth Walking 
2. The Blindfold Challenge
3. Art of Hearing
4. Reaction Time
5. Memory Sequence

> Which at the end, when participants have participated in all 5 stations, they will be presented with a: 

6. Graduation Sequence

> In this repository, it will be focused solely on Station 3 - Art of Hearing.

## Station Game

> In the Art of Hearing, it  is the ultimae test in auditory acuity. In this station, participants are required to isolate specific sounds from a layered landscape and decipher the messages, which they then enter the deciphered messages to achieve victory at the station 

><details open>
> <summary>Key Features include:</summary>
* Rich, Multi-layered environments created by L-ISA 
* Focusing and listening to specific sounds to decipher messages 
* Using those messages to put in a number combination lock at the station to achieve victory.

## Dependencies
> All the codes in this repository have been made using **Python 3.9 or higher**

## Pre-Requisities
> These are the softwares required that was utilised in the project:
1. loopMIDI - Click [Here](https://www.tobias-erichsen.de/software/loopmidi.html)
2. L-ISA Studio - Click [Here](https://www.l-acoustics.com/products/l-isa-studio/#)
3. Reaper DAW - Click [Here](https://www.reaper.fm/download.php)

## Setting Up
> 1. Update your Raspberry Pi
   
   ```
   sudo apt update
   sudo apt upgrade
   ```
   
  > If update and/or upgrade is unsuccesful, manually set the date and time by
   
   ```
   sudo date -s 'YYYY-MM-DD HH:MM:SS"
   ```
> 2. Setting up Virtual Environment
   
  > To install Virtual Environment

   ```
   sudo apt install virtualenv python3-virtualenv -y
   ```

  > To create a new virtual environment

   ```
   virtualenv -p /usr/bin/python3 <environment_name>
   ```

 >   The <environment_name> is a variable, able to name it to other names

  **THE VIRUTAL ENVIRONMENT IS A FOLDER**
   
  > To activate the virtual environment

   ```
   source <environment_folder>/bin/activate
   ```

  > To install a package

   ```
   pip3 install python-osc
   ```

  > To deactivate environment
   
   ```
   deactivate
   ```


## Tutorials
> * **[Backlog 1 Sprint 1](./Backlog%201%20Sprint%201/B1S1.md)** - OSC Control to GrandMA3 and QL1 
> * **[Backlog 1 Sprint 2](./Backlog%201%20Sprint%202/B1S2.md)**  - Laser Sequence Slow and Fast
> * **[Backlog 2 Sprint 1](./Backlog%202%20Sprint%201/B2S1.md)** - L-ISA snapshots, OSC Communication to DAW 
>* **[Backlog 2 Sprint 2](./Backlog%202%20Sprint%202/B2S2.md)** - Configuration of number lockpad GUI for POC demostration
>* **[POC](./POC//POC.md)** - All the resources utilised for the demostration

## References
> - **[Huats Club - rpistarterkit](https://github.com/huats-club/rpistarterkit)** - Getting started on configuring your Raspberry Pi
> - **[Huats Club - oscstarterkit](https://github.com/huats-club/oscstarterkit)** - Getting started on using Python Open Sound Control
 >- **[Huats Club - mts_sensor_cookbook](https://github.com/huats-club/mts_sensor_cookbook)** - Foundation codes on common sensors


## Contributors
> <a href="https://github.com/KarmaLuvsU"><img src="https://avatars.githubusercontent.com/u/167286591?v=4" title="Victor Nguyen" width="50" height="50"></a>
<a href="https://github.com/Jerolaw"><img src="https://avatars.githubusercontent.com/u/132433711?v=4" title="Jerome" width="50" height="50"></a>
<a href="https://github.com/THINESH2024"><img src="https://avatars.githubusercontent.com/u/171120826?v=4" title="Thinesh" width="50" height="50"></a>

