from ncclient import manager
import xml.dom.minidom

# Create a new manager object
m = manager.connect (
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False,
    )
'''
print("#Supported Capabilities (YANG models):") 
for capability in m.server_capabilities: 
    print(capability)
'''
# variable to filter for data returned by cisco ios xe 'native' YANG model
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
""" 
# <config> variable to change the hostname
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CRS1kv</hostname>
    </native>
</config>
"""
# <config> variable to create a loopback interface
netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My Number 1 loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
# <config> variable to change the loopback description
netconf_loopback_description = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My Number 1 loopback RENAMED</description>
            </Loopback>
        </interface>
    </native>
</config>
"""

# <config> variable to create a new loopback interface with same ip as previous to force an error
netconf_loopback_error = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                <description>My Number 2 loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""



# get NETCONF data from device
netconf_reply = m.get_config(source="running", filter=netconf_filter)
# print a pretty formatted XML reply
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

'''
# update hostname
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''

'''
# create loopback interface
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''

'''
# create loopback interface with same ip as previous to force an error
netconf_reply = m.edit_config(target="running", config=netconf_loopback_error)
'''

# change loopback description
# netconf_reply = m.edit_config(target="running", config=netconf_loopback_description)    
