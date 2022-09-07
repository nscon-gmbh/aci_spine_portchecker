# aci_spine_portchecker

Check portstatus of aci spines
 
## Use Case Description

The code is used to check the port status of all spine switches in an cisco application centric infrastructure via api. 
The code is used for a one time live check.

## Installation

You need to install python3.8 or higher to run the code. 
You need to install the following modules:
- requests
- json
- os

## Configuration

You can define enviroment variables (ACI_URL, ACI_USER, ACI_PASS) or enter the parameters initial at the start of the script. 
For multiple use, we recommand to configure enviroment variables.

## Usage

```bash
(venv) $ python aci_spine_portchecker.py

Enter ACI url: https://10.10.20.14/

Enter ACI username: admin

Enter ACI password: C1sco12345

Host: https://10.10.20.14/

Device  |  Interface  |  Status
spine-1  |  eth14/32  |  up
spine-1  |  eth14/3  |  up
spine-1  |  eth17/30  |  up
spine-1  |  eth14/7  |  up
spine-1  |  eth9/3  |  up
spine-1  |  eth9/13  |  up
spine-1  |  eth14/5  |  up
spine-1  |  eth14/29  |  up
<output omitted>
```

### DevNet Sandbox

Tested with [Cisco ACI Multi-Site Orchestrator](https://devnetsandbox.cisco.com/RM/Diagram/Index/94913e15-002f-4b2a-b241-8eeed50ebbf8) reservable sandbox.

## How to test the software

Last tested un August 2022.

## Known issues

Some json format issus when login or data gathering fails will be fixed in the future.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Author(s)

This project was written and is maintained by the following individuals:

* Benjamin jung <jung@nscon.de>
