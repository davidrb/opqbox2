OPQBOX 2
========

Overview
--------

This repository provides the proposed schematics for the second generation Open Power Quality metering device (OPQBox2). 

Currently, OPQBox2 is in the design stage.  We are circulating its design now in order to solicit feedback and make improvements prior to layout. We greatly appreciate your willingness to provide us with feedback.

High level requirements
-----------------------

The design of OPQBox2 is influenced by our experience with the first generation OPQBox.  Design information about our first generation hardware is available at the [OPQBox1 repository](https://github.com/openpowerquality/opqbox1). 

We performed a [pilot study of our first generation hardware and software](http://openpowerquality.org/technology/g1-pilot-study.html), and one of the results of this study are the following major requirements for OPQBox2:

  * **Support event recording upon power cutout.** OPQBox2 includes a Li-Po battery so that the box can record an event if power is interrupted prior to shutdown. Also to support this requirement, OPQBox2 includes nonvolatile 64K EEPROM memory.
  
  * **Satisfy IEEE PQ standards.**  This includes 256 samples per waveform and locking to 60Hz input.
  
  * **Improve data quality through dual transformers**. OPQBox2 is designed so that the transformer used to power the device is independent from the transformer used to collect PQ data.
  
Summary of component changes
----------------------------

Here is a summary of component changes proposed for OPQBox2:

 
                | OPQBox1 | OPQBox2
--------------- | ------- | -------
**Power**       |         | 
                | 12V transformer for measurement | Isolated 5V DC-DC
                | 40-10V DC for power | Unisolated capacitive PSU
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

  * Measurement is isolated via amc1100 isolation amplifier.
  * Resistor divider for measurement.
  * Shielded resistors for divider.

Safety
------

We have domain knowledge in measurement/DSP, but not PSU design and consumer products. From a safety perspective, we have implemented the following:

  * Isolated PSU for measurements and communications.
  * EMI, fuse, component rating... etc.
  * Isolation for measurement.
  * Capacitive power supply.

Additional design documents
---------------------------

 
  * [OPQBOX2 pdf schematic](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2.pdf)
  * [Bill of Materials](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/Schematics/BOM.txt)
  * [Mentor graphics PADS schematic of OPQBOX2](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2.sch)
  * [PADS library](https://github.com/openpowerquality/opqbox2/tree/master/Schematics/Library)
  


Summary of questions for review
-------------------------------

  * Do you have any recommendations to improve safety?
  * Do you have any recommendations to improve measurement accuracy, precision, or reliability?
  * Do you have any recommendations should we decide to pursue UL certification?
  * Is there a way to shield the measurements circuit (such as adding a shielding can or PCB moat)? Is it worth the trouble?
  
Thanks so much for your time!