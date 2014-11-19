Overview
--------

The mission of the Open Power Quality project is to design and implement open source hardware, software, and data for low cost, crowd-sourced power quality monitoring, storage, and analysis. For more details, please see our [home page](http://openpowerquality.org).

This repository provides the proposed schematics for the second generation Open Power Quality metering device (OPQBox2). 

Currently, OPQBox2 is in the design stage.  We are circulating this design to solicit feedback and make improvements prior to production. We greatly appreciate your willingness to provide us with feedback.

Operational requirements
------------------------

The design of OPQBox2 is influenced by our experience with the first generation OPQBox.  Design information about our first generation hardware is available at the [OPQBox1 repository](https://github.com/openpowerquality/opqbox1). 

We performed a [pilot study of our first generation hardware and software](http://openpowerquality.org/technology/g1-pilot-study.html), and one of the results of this study are the following major requirements for OPQBox2:

  * **Operational parameters.**  OPQBox2 can be plugged into a standard U.S. two prong outlet with expected power at a frequency of 60 Hz and with a voltage of 110 V. It can operate under a frequency range of XX Hz to XX Hz and under a voltage range of XX V to XX V. Fuses will disable OPQBox2 when voltages or frequency exceed operational parameters.

  * **Support event recording upon power cutout.** OPQBox2 adds an 8k of ferromagnetic RAM(FRAM) IC.  Fram will be used as a circular buffer, containing 0.5s of high resolution voltage measurements. Fram will maintain its state through a power cycle, which will be sent to the cloud once the power-grid comes back online.
 
  * **Satisfy IEEE PQ standards.**  This includes 256 samples per waveform and locking to 60Hz input.
  
  * **Improve data quality through removal of the voltage sensing transformer.** Using a transformer for voltage measurements makes the device hard to calibrate. Furthermore we found that wall-wart transformers distort the line voltage.
  
Summary of component changes
----------------------------

Here is a summary of component changes proposed for OPQBox2:

 
                | OPQBox1 | OPQBox2
--------------- | ------- | -------
**Power**       |         | 
                | 12V transformer for isolated voltage sensing | Resistor Divider for direct voltage sensing 
                | 40-10V DC for power | Isolated 5V DC-DC,  Unisolated capacitive PSU
**Measurement** |         |
                | 4KSPS 16Bit ADC | 50 KSPS 14/16Bit ADC
                | Raspberry Pi for processing/WiFi | Raspberry PI for WiFi only
                |         | 72Mhz Arm+FPU
                |         | PI can be replaced with CAN/RF/Ethernet/GSM module


Capacitive PSU design
---------------------

![capacitive PSU](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/images/capacitive-psu.png)

Design notes:

  * Input is fused and protected by a varistor. 
  * R25 for bleeding C1 and suppressing spikes.
  * 12mA output, we are driving it at 10mA through a regulator to the isolation amplifier (see below).

Measurement isolation design
----------------------------

![capacitive PSU](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/images/measurement-isolation.png)

Design notes:

  * Measurement is isolated via TI [amc1100](http://www.ti.com/product/amc1100) isolation amplifier.
  * Resistor divider for voltage measurement.
  * Shielded resistors for divider.

Layout
------

(Sergey, please add a section about layout here.)


Safety
------

We have domain knowledge in measurement/DSP, but not PSU design and consumer products. From a safety perspective, we have implemented the following:

  * Isolated PSU for measurements and communications.
  * EMI, fuse, component rating... etc.
  * Isolation for measurement.
  * Capacitive power supply, according to Microchip [AN954](http://ww1.microchip.com/downloads/en/AppNotes/00954A.pdf).

Additional design documents
---------------------------

 
  * [OPQBOX2 pdf schematic](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2.pdf)
  * [Bill of Materials](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/Schematics/BOM.txt)
  * [Mentor graphics PADS schematic of OPQBOX2](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2.sch)
  * [PADS library](https://github.com/openpowerquality/opqbox2/tree/master/Schematics/Library)
  


Summary of questions for review
-------------------------------

Here are the issues we are most concerned about.

  * Do you have any recommendations to improve safety?
  * Do you have any recommendations to improve measurement accuracy, precision, or reliability?
  * Do you have any recommendations should we decide to pursue UL certification?
  * Is there a way to shield the measurements circuit (such as adding a shielding can or PCB moat)? Is it worth the trouble?
  
If you would like to meet in person or via teleconference to discuss this design, we would be happy to arrange that. If you can reply with comments to johnson@hawaii.edu, that would be great. 

Thanks so much for your time!  
