This is a documentation file for MakeOhio25 team 72 (GabaGhoul).
Members: Ryan Yovichin; Jake Dill; Quill van Roodselaar
Linkedins: https://www.linkedin.com/in/ryan-yovichin-507061297/  ; https://www.linkedin.com/in/jacob-dill-5ab456192/  ;  https://www.linkedin.com/in/nicole-van-roodselaar-087209219 

This is a part of the intel challenge: 
Propose and design a prototype/solution that advances
open-source chip development using accessible hardware.
● Your solution should align with one or more of the themes
given below.
● Emphasis is placed on creative, functional and affordable
solutions achieved within the 30 hour timeframe.
● Challenge themes include:
○ Optimization
■ Emphasis on running CV on low cost
microcontrollers like Raspberry Pi Picos and Pi
Zero’s.
○ Photolithography
○ DIY Testing and Characterization
■ Probe stations
■ IV Curve analysis tools
○ Optical encoder / Position tracking
○ Photomask printing
○ Low-cost image sensor

We made a tehcnical demonstration of a "Photolithography" alignment system using stepper motors. this 
was accompanied by a microscope which takes pictures, and provides tracking data for feed back, calibration,
tracking, and testing (the microsope had a resolution of roughly 2 microns) and a 7 seg. disp. that displayed the 
percent completion on the project.

timeline of comp.:
1. start
- meeting the team,ideation, research, inventory, collecting necessary componants, and researching componants
2. started making
- Raspberry PI, got working and talking to arduino, intended to use as python based micro controller which could take
pictures with the microscope, incomplete
- arduino, used to inteact with most of our componants, recieves info on semiconductor, then runs over the 
chip shinning a laser on inteact, complete
- photo diode, and laser, these two were used and test alignment and placement on semiconductor
- microscope, connects to camera and can be interacted with as a computer camera
3. Optimization
- got down to single stepping and half stepping (incomplete)
- alginment down to +/- 1 step (pre running code)
- 100% precision (never missed a index or over/understepped)
-laser focusing, (much greater than desired precision, Proof Of Concept)
- motor controller, work at optimal speed to never miss a signal
4. design 
- CAD Models, cad models for all 3D printable parts (microchip holder, microscope mount, laser mount)
- drawings for branstorming with "demensions"
- accuracy calculations
5. implementation
- python code, take photo, detail picture as only red (where is laser), average the points (find x,y of laser)
- arduino code (align steppers to bottom right, loop over whole array
capped size so as not to lose accuracy from and over torquing problem, presents percent complete for 7 seg. disp.)
- card board cuttouts (used due to time, held chips, laser, and microscope)
- PCB board (7 seg. display, motor drivers/steppers)
- with more time and maybe better material we wish we could have had a better construction than panara bread co. boxs
taped, glued and jerryrigged together
6. finish 
- 1.25 um accuracy
- microscope pictures and tracking
- 7 segment disp
- presentaion to be finished
7. future


hack ohio website: https://hack.osu.edu/make/2025

List of Resources
Photolithography: https://en.wikipedia.org/wiki/Photolithography
Optical encoder: https://www.google.com/search?q=Optical+encoder+%2F+Position+tracking&rlz=1C1ONGR_enUS1092US1092&oq=Optical+encoder+%2F+Position+tracking&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzI4NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#vhid=5p96MhXpwC5IaM&vssid=l
Motor dirver: https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1743180263699&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D
https://www.ti.com/product/L293D 
https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1743213446730&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D
https://l293d.readthedocs.io/en/latest/user-guide/python-scripts/
Pi camera setup: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/1 
photo diode: https://www.build-electronic-circuits.com/photodiode/ ; https://en.wikipedia.org/wiki/Photodiode
steppers:https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/
https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1743213446730&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D
https://l293d.readthedocs.io/en/latest/user-guide/python-scripts/
https://pages.pbclinear.com/rs/909-BFY-775/images/Data-Sheet-Stepper-Motor-Support.pdf
camera: https://medium.com/@robotamateur123/use-a-usb-camera-with-raspberry-pi-for-beginners-5f0ed8e98400