# aci_spine_portchecker

Check portstatus of aci spines
 
## Use Case Description

Describe the problem this code addresses, how your code solves the problem, challenges you had to overcome as part of the solution, and optional ideas you have in mind that could further extend your solution.

## Installation

Detailed instructions on how to install, configure, and get the project running. Call out any dependencies. This should be frequently tested and updated to make sure it works reliably, accounts for updated versions of dependencies, etc.

## Configuration

If the code is configurable, describe it in detail, either here or in other documentation that you reference.

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

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.


## Known issues

Document any significant shortcomings with the code. If using [GitHub Issues](https://help.github.com/en/articles/about-issues) to track issues, make that known and provide any templates or conventions to be followed when opening a new issue. 

## Getting help

Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](./CONTRIBUTING.md) file.

## Author(s)

This project was written and is maintained by the following individuals:

* Benjamin jung <jung@nscon.de>
