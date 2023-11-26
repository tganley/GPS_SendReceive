# GPS GPGLL Sender & Receiver
## Design
There are two components in this GPGLL handler. The Sender generates random GPGLL messages (some of which are invalid by design), and the Receiver parses those messages into user-readable output and compiles test results. The GPGLL reference is from [here](https://www.rfwireless-world.com/Terminology/GPS-sentences-or-NMEA-sentences.html).

## Install & Run
```
git clone git@github.com:tganley/GPS_SendReceive.git
python3 main_GPGLL.py
```