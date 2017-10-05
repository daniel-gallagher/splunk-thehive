# splunk_thehive event settings

action.splunk_thehive = [0|1]
* Enable thehive_create_case notification

action.splunk_thehive.param.title = <string>
* Case Title to use in TheHive.
* (required)

action.splunk_thehive.param.description = <string>
* The description of the case to send to TheHive.
* (required)

action.splunk_thehive.param.severity = [0|1|2|3]
* The severity of the new case. 1 = low, 2 = medium, 3 = high
* Default is "1" (low)
* (optional)

action.splunk_thehive.param.owner = <string>
* Case owner. Defaults to user name that creates the case.
* (optional)

action.splunk_thehive.param.tlp = [-1|0|1|2|3]
* Traffic Light Protocol for this case. 0 = White, 1 = Green, 2 = Amber, 3 = Red
* TLP affects releasability of information. Some analyzers will not be available on higher TLP settings.
* Defaults to "2" (Amber)
* (optional)

action.splunk_thehive.param.tags = <string>
* The tags to put on the case. Use a single, comma-separated string (ex. "badIP,trojan").
* (optional)
