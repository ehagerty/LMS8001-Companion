Detailed Description
====================

A more detailed description of the LMS8001 Companion board components and interconnections is given in this chapter.

Digital Connectivity
--------------------

The board is controlled via USB using the :doc:`LMS8 Suite software </software/index>`. In its default configuration, all commands to the LMS8001A chip are generated and sent by the MCU via the SPI bus. An advanced option allows the use of GPIO signals for fast switching between predefined LMS8001A configurations, where the chip has several states already stored. This is explained in detail in the `LMS8001 Reference Manual`_.

There are two 10-pin headers where the aforementioned signals are connected. For further details see also :ref:`hardware/detailed:Digital and Control Signals Network`.

.. table:: Table 2. Pin header P2 detailed description. 
   :widths: auto

   +--------+-------+-----------------------------------------------------+
   | Pin    | Name  | Description                                         |
   | Number |       |                                                     |
   +========+=======+=====================================================+
   | 1      | GND   | Global ground                                       |
   +--------+-------+-----------------------------------------------------+
   | 2      | GPIO8 | Connected to MCU **PC1** and through **R17** to     |
   |        |       | LMS_GPIO8                                           |
   +--------+-------+-----------------------------------------------------+
   | 3      | GPIO0 | Connected to MCU **PB12** and through **R28** to    |
   |        |       | LMS_GPIO0                                           |
   +--------+-------+-----------------------------------------------------+
   | 4      | GPIO7 | Connected to MCU **PB1** and through **R21** to     |
   |        |       | LMS_GPIO7                                           |
   +--------+-------+-----------------------------------------------------+
   | 5      | GPIO1 | Connected to MCU **PB13** and through **R27** to    |
   |        |       | LMS_GPIO1                                           |
   +--------+-------+-----------------------------------------------------+
   | 6      | GPIO6 | Connected to MCU **PB0** and through **R22** to     |
   |        |       | LMS_GPIO6                                           |
   +--------+-------+-----------------------------------------------------+
   | 7      | GPIO2 | Connected to MCU **PB15** and through **R25** to    |
   |        |       | LMS_GPIO2                                           |
   +--------+-------+-----------------------------------------------------+
   | 8      | GPIO5 | Connected to MCU **PC4** and through **R24** to     |
   |        |       | LMS_GPIO5                                           |
   +--------+-------+-----------------------------------------------------+
   | 9      | GPOI3 | Connected to MCU **PB14** and through **R26** to    |
   |        |       | LMS_GPIO3                                           |
   +--------+-------+-----------------------------------------------------+
   | 10     | GPIO4 | Connected to MCU **PC5** and through **R23** to     |
   |        |       | LMS_GPIO4                                           |
   +--------+-------+-----------------------------------------------------+

.. table:: Table 3. Pin header P3 detailed description.
   :widths: auto

   +--------+-------------+------------------------------------------------+
   | Pin    | Name        | Description                                    |
   | Number |             |                                                |
   +========+=============+================================================+
   | 1      | +3.3V_EXT   | External 3.3 V DC supply signal                |
   +--------+-------------+------------------------------------------------+
   | 2      | GND         | Global ground                                  |
   +--------+-------------+------------------------------------------------+
   | 3      | SDO         | OUT data signal of SPI bus (MCU is master on   |
   |        |             | SPI bus)                                       |
   +--------+-------------+------------------------------------------------+
   | 4      | CORE_LDO_EN | Global power down for LMS8001A chip            |
   +--------+-------------+------------------------------------------------+
   | 5      | SDIO        | IN/OUT data signal of SPI bus (MCU is master   |
   |        |             | on SPI bus)                                    |
   +--------+-------------+------------------------------------------------+
   | 6      | RESETN      | Reset of LMS8001A chip                         |
   +--------+-------------+------------------------------------------------+
   | 7      | SCLK        | Clock signal of SPI bus                        |
   +--------+-------------+------------------------------------------------+
   | 8      | SAEN        | Select enable for LMS8001A chip on SPI bus     |
   +--------+-------------+------------------------------------------------+
   | 9      | NC          | Not connected                                  |
   +--------+-------------+------------------------------------------------+
   | 10     | NC          | Not connected                                  |
   +--------+-------------+------------------------------------------------+


.. note::
   For more information about +3.3V_EXT see section DC signals.

RF Network 
----------

LMS8001 Companion is based upon the LMS8001A 4-channel up/down conversion RFIC. There are a total of 8 signals, 4 inputs and 4 outputs. Depending on whether
upconversion or downconversion, the input signals are either in IF (lower frequency bands) or RF (higher frequency bands). 

Similarly and depending upon whether it is upconversion or downconversion, the output signals are in RF (higher frequency bands) or IF (lower frequency bands). All these signals are connected to either SMA or U.FL connectors. 

LMS8001A can be configured so that the internal PLL is not active and instead an external LO signal is provided to the board via SMA connector J3.

.. table:: Table 4. RF signals and their connectors.
   :widths: auto

   +---------------+------------+--------------+----------------+-------------+
   | Signal Name   | IN/OUT     | Connector    | Conversion     | Connector   |
   |               | Type       | Type         | Type           | Designation |
   +===============+============+==============+================+=============+
   | CHAI          | IN         | U.FL         | Upconversion   | J5          |
   +---------------+------------+--------------+----------------+-------------+
   | CHAO          | OUT        | SMA          | Upconversion   | J8          |
   +---------------+------------+--------------+----------------+-------------+
   | CHBI          | IN         | U.FL         | Upconversion   | J6          |
   +---------------+------------+--------------+----------------+-------------+
   | CHBO          | OUT        | SMA          | Upconversion   | J9          |
   +---------------+------------+--------------+----------------+-------------+
   | CHCI          | IN         | SMA          | Downconversion | J7          |
   +---------------+------------+--------------+----------------+-------------+
   | CHCO          | OUT        | U.FL         | Downconversion | J10         |
   +---------------+------------+--------------+----------------+-------------+
   | CHDI          | IN         | SMA          | Downconversion | J4          |
   +---------------+------------+--------------+----------------+-------------+
   | CHDO          | OUT        | U.FL         | Downconversion | J11         |
   +---------------+------------+--------------+----------------+-------------+
   | EXT_LO        | IN         | SMA          | None           | J3          |
   +---------------+------------+--------------+----------------+-------------+

.. figure:: /images/LMS8001_Companion_Board-RF_Block_Diagram.svg
   :alt: LMS8001 Companion RF Block Diagram
   :align: center

   Figure 5. LMS8001 Companion Board 3v2 RF block diagram.

Reference Clock Network
-----------------------

This block generates REF CLK signal which is used for the internal PLL
circuit to generate the LO signal. The entire block is shown in Figure 6.
The main part of this block is comprised of a PLL circuit which generates REF
CLK of 40 MHz in its default mode. This PLL consists of the clock
buffer (U21), the PLL chip (U18), RC low pass filter (RC LPF) and one of
XO3 or XO4 voltage controlled oscillators (VCO). 

Furthermore, by using J13, an external reference signal can be connected to the board and in this case, the 40 MHz REF CLK is locked to this external reference. In most cases this is a 10 MHz signal obtained from a frequency standard such as a GPSDO. By choosing which resistor, R104, R105 or R107, is fitted on the board, the user can select either XO3 or XO4 as VCO. The corresponding R107 or R108 must be fitted as well, please see Table 5.

.. table:: Table 5. Selection options for XO3 and XO4.
   :widths: auto

   +-------------+--------+------------+------------+------------+------------+------------+
   |             | R104   | R105       | R107       | R108       | R110       | R80        |
   +=============+========+============+============+============+============+============+
   | XO3         | Not    | **Fitted** | Not fitted | **Fitted** | Not fitted | Not fitted |
   |             | fitted |            |            |            |            |            |
   +-------------+--------+------------+------------+------------+------------+------------+
   | XO4         | Not    | Not fitted | **Fitted** | Not fitted | **Fitted** | Not fitted |
   |             | fitted |            |            |            |            |            |
   +-------------+--------+------------+------------+------------+------------+------------+
   | X03 drives  | Not    | **Fitted** | Not fitted | **Fitted** | Not fitted | **Fitted** |
   | additional  | fitted |            |            |            |            |            |
   | ext. board  |        |            |            |            |            |            |
   | via J13     |        |            |            |            |            |            |
   +-------------+--------+------------+------------+------------+------------+------------+
   | XO4 drives  | Not    | Not fitted | **Fitted** | Not fitted | **Fitted** | **Fitted** |
   | additional  | fitted |            |            |            |            |            |
   | ext. board  |        |            |            |            |            |            |
   | via J13     |        |            |            |            |            |            |
   +-------------+--------+------------+------------+------------+------------+------------+

.. note::
   R104 connects CP output of the ADF4002 (U18) to GND.

.. figure:: /images/LMS8001_Companion_Board-REF_CLK_Block_Diagram.svg
   :alt: LMS8001 Companion Reference Clock Block Diagram
   :align: center

   Figure 6. LMS8001 Companion Board 3v2 Reference Clock block diagram.

Digital and Control Signals Network
-----------------------------------

The core of the digital block is an MCU (STM32F105). All communication
between the GUI and the board, in both directions, is handled by the MCU
via USB. The MCU acts as the master on the SPI bus, through which it
controls the LMS8001A and ADF4002 chips. In addition to the SPI bus,
several predefined GPIO pins are used for digital control signals such
as RESET, ENABLE, etc.

Another group of GPIO signals can be used to preconfigure the LMS8001A into one of its already saved states. Using GPIO pins for reconfiguration is the fastest method, compared to SPI, and is particularly advantageous in frequency-hopping
applications involving the LMS8001A.

MCU GPIO signals are also used to control indicator LEDs (LED1, LED2, LED3).

.. figure:: /images/LMS8001_Companion-Digital_Block_Diagram.svg
   :alt: LMS8001 Companion Digital Block Diagram
   :align: center

   Figure 7. LMS8001 Companion Board 3v2 Digital block diagram.

Power Distribution
------------------

The LMS8001 Companion board has an external 5V (+5V_EXT) power
connector (J2) that supplies power to the board. This is the recommended
configuration. Alternatively, 5V can be supplied via the USB connector
(J1). One of these two options is selected using the JP1 jumper. 

U14, shown in Figure 9, is protection circuit which ensures proper power-on
of the board. 

An auxiliary 3.3V supply can also be provided to the
board via the P3 connector pin 1 and for details see Table 3.

.. figure:: /images/LMS8001_Companion-Power_Block_Diagram.svg
   :alt: LMS8001 Companion Power Block Diagram
   :align: center

   Figure 8. LMS8001 Companion Board 3v2 Power block diagram.

Further Reading
---------------

For further details please refer to the `LMS8001 Companion GitHub repository`_