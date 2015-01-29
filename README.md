Overview
--------

The mission of the Open Power Quality project is to design and implement open source hardware, software, and data for low cost, crowd-sourced power quality monitoring, storage, and analysis. For more details, please see our [home page](http://openpowerquality.org).

This repository provides the proposed schematics for the second generation Open Power Quality metering device (OPQBox2). 

OPQBox2 is in the final design stage.  We are circulating this design to solicit feedback and make improvements prior to production. We greatly appreciate your willingness to provide us with feedback.

Goals
-----

The purpose of the OPQBox is to monitor voltage and frequency and detect departures from nominal levels.  It accomplishes this by sampling the waveform 256 times per cycle, extracting power quality measures (including frequency, RMS voltage, and THD), and then uploading data about these measures to the OPQHub service. 

The OPQBox can be configured to send a "heartbeat" message to the OPQHub to indicate that it is connected and functioning. This message normally includes low resolution voltage and frequency data.   

When a power quality disturbance is detected by the OPQBox, it sends a message to the OPQHub that includes high resolution voltage samples. 

We expect that OPQBoxes will be synchronized to within 1 millisecond through the use of NTP. This enables data from multiple OPQBoxes to be used to generate a global perspective on the state of the grid.  As a simple example, it can enable users to determine if their event is local to their own residence or instead grid-wide. 

Operational requirements
------------------------

The design of OPQBox2 is influenced by our experience with the first generation OPQBox.  Design information about our first generation hardware is available at the [OPQBox1 repository](https://github.com/openpowerquality/opqbox1). 

We performed a [pilot study of our first generation hardware and software](http://openpowerquality.org/technology/g1-pilot-study.html), and one of the results of this study are the following major requirements for OPQBox2:

 * **Safety.**   Our device plugs is ment to  bypass power filters and surge protectors. Thus it incorporates extra protection elements to keep the device operating safely during power disruptions. Fuses will disable OPQBox2 in case of a fault. All of the user accesible components are isolated from the mains.

 * **Satisfy IEEE PQ standards.**  OPQBox2 can be plugged into a standard U.S. two prong outlet with expected power at a frequency of 60 Hz and with a voltage of 120 V. It can operate under a frequency range of 50 Hz to 70 Hz and under a voltage range of 80 Vac to 200 Vac. Sampling is phase locked to the utility frequency. The 16 bit 100KSPS ADC allows for 5mV resolution with over 1024 points per grid cycle. On board ARM floating point DSP is able to perform the IEEE 1159 outlined analysis, as well as user defined code.

 * **Support event recording upon power failure.** OPQBox2 adds up to 512k of ferromagnetic RAM(FRAM) IC.  Fram will be used as a circular buffer, containing up to 1 min of high resolution voltage measurements. Fram will maintain its state through a power cycle, which will be sent to the cloud once the power-grid comes back online.

* **Connectivity** OPQBox 2 is designed to be the deployed as a part of a distributed real-time power quality monitoring network. As such it offers a large number of interface options, including serial, USB, WIFI and cellular network. The initial development will focus on WIFI, and serial communication.
  
Changes From OPQBox 1.
----------------------------
OPQBox2 is a complete redesign from the previous generation. It replaces the voltage sensing transformer with an isolation amplifier. The sampling rate has increased from 4kSPS to up to 100kSPS. In order to keep up with the faster acquisition a dedicated ARM DSP is used to control the sampling and realtime processing. Here is a summary of component changes proposed for OPQBox2:

 
                | OPQBox1 | OPQBox2
--------------- | ------- | -------
**Voltage sensing/Isolation** | 12V transformer wall plug transformer | Isolation amplifier.
**Power**       | 12V transformer | Isolated 5V DC-DC,  Unisolated capacitive PSU
**ADC**         | 4KSPS 16Bit ADC | 100 KSPS 16Bit ADC
**Processing**  | Raspberry Pi for processing/WiFi | Dedicated ARM DSP for real time processing.
                |         | Raspberry PI for communication and configuration only.
                |         | PI can be replaced with CAN/RF/Ethernet/GSM module


Capacitive PSU Design
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

  * Measurement is isolated via TI [amc1100](http://www.ti.com/product/amc1100) isolation amplifier.[AD7684](http://www.analog.com/en/analog-to-digital-converters/ad-converters/ad7684/products/product.html) ADC.
  * Flame proof, pulse withstanding resistors for voltage measurement
  * [TMOV25SP230M ](http://www.littelfuse.com/products/varistors/thermally-protected/tmov25s/tmov25sp230m.aspx) MOV and a TVC for surge protection. 

Layout
------
PCB layout is available in the schematics folder. It is provided as a PADs Layout file, as well as gerbers and pdf/image files. This design calls for a 2 layer FR4 board, and measures 200mm by 80mm.  PCB passed DFM check and is ready to be manufactured. This device is intended as an engineering sample. We expect to go through several iterations refining the design. Additional we are solicit comments and sugestions from the open source community. If you share our interest in distributed power quality measurement, don’t hesitate to contact us. 

![layout](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/images/layout.png)
Full Layout. The Isolation barrier is clearly visible. Perhaps a cutout is appropriate to improve isolation?

![layout](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/images/layout-top.png)
Top copper, soldermask and silkscreen.
![layout](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/images/layout-bottom.png)
Bottom copper, soldermask and silkscreen.
Safety
------

We have domain knowledge in measurement/DSP, but not PSU design and consumer products. From a safety perspective, we have implemented the following:

  * Creepage/Clearance appropriate for mains power.
  * Isolated power and sensing for all user serviceable components.
  * Circuit Protection (MOV, TVC, etc).
  * EMI, fuse, component rating... etc.

Additional design documents
---------------------------

 
  * [OPQBOX2 pdf schematic](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2_schematic.pdf)
  * [OPQBOX2 pdf layout](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2_layout.pdf)
  * [Bill of Materials](https://raw.githubusercontent.com/openpowerquality/opqbox2/master/Schematics/BOM.txt)
  * [Mentor graphics PADS schematic of OPQBOX2](https://github.com/openpowerquality/opqbox2/blob/master/Schematics/opq2.sch)
  * [PADS library](https://github.com/openpowerquality/opqbox2/tree/master/Schematics/Library)
  


Summary of questions for review
-------------------------------

Here are the issues we are most concerned about.

  * Do you have any recommendations to improve safety?
  * Do you have any recommendations to improve measurement accuracy, precision, or reliability?
  * Do you have any recommendations for certifications?(UL, IEEE, IEC, etc)
  
If you would like to meet in person or via teleconference to discuss this design, we would be happy to arrange that. If you can reply with comments to johnson@hawaii.edu, that would be great. 

Thanks so much for your time!  
