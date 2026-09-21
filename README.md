IAXO LSC nodered
===
***

This repository includes the nodered flows of the IAXO LSC detector.

The repository is installed in `/home/iaxo/.node-red/`.

Functionalities or code that need To Be Checked is marked as (<mark>TBC</mark>).

# Flows

(<mark>TBC</mark>)

The code is composed of the following flows:

 - **CAEN** 
 	 + High Voltage Power Supply (HVPS) for TPC
 	 	+ Cathode: *channel0* 
 	 	+ Mesh:  *channel1*
 	 	+ Top:  *channel2*
 	 	+ Bottom:  *channel3*
 	 + CAEN DT5521HE 
		+ Before 2025/12/10 it was a N1471HA
	 + SerialPort `dev/ID1_CT_HV` 
 - **Multicomp**
     + Voltage supply for DAQ
	 + Multicomp MP710086
	 + SerialPort `/dev/ID1_DAQ_PS`
 - **MZD/SMART MT20 MoistureAnalyzer**
     + Moisture Analyzer
     + Communication using RS485 and DA-70157 USB adapter
       + Adator cabling A+ and B-
 - **Southland EMD 485 Oxygen Analyzer**
     + Oxygen Analyzer
     + Communication using RS485 and DA-70157 USB adapter
       + Adator cabling A+ and B-
       + Sensor Cabling: TH:White / TH: Blue / - Black / + Red

## Database

- Postgressql Database
- Database: iaxoLSCslowctldb
- User: postgres
- Password: bujaruelo

# Operation Notes

(<mark>TBC</mark>)

# NODERED NOTES

## Memory Leaks
Nodered is prone to memory leaks. 

To avoid memory leaks it is important to avoid errors in the code.

In **serial ports** it is important to:

 - Check the status of the response from the serial port and filter the message only when the `msg.status` is  `OK`.
 - Send messages to the serialport only when the port is connected
	 + If messages are always sent nodered is not able to reconnect upon a communication error.
	 
In **Databases** (or in **join** nodes):

 - It is important that in a join node all input messages are sent. If a device is disconnected but a node keeps input to join (e.g. TableName) there may be a memory leak.


## USB Configuration
The serialport configuration is included in `/etc/udev/rules.d/99-usb-serial.rules

For information on the serial ports  `devadm info --name=/dev/<device>`

For reloading the rules:

```
	sudo udevadm control --reload-rules
  	sudo udevadm trigger
```

## Credentials
Credentials are set in `settings.js`.

Credentials are encrypted usin `node-red admin hash-pw`.

# TODO LIST

- Serial In Check & Connection Management
  - Update of serialport node is necessary
- Debug different flows
- Review Security Flow


