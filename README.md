IAXO LSC nodered
===
***

This repository includes the nodered flows of the IAXO LSC detector.

The repository is installed in `/home/iaxo/.node-red/`.

Functionalities or code that need To Be Checked is marked as (<mark>TBC</mark>).

# Flows

(<mark>TBC</mark>)

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
- Database tableName
- Migrate Slack messages to Mattermost
- Review Security Flow


