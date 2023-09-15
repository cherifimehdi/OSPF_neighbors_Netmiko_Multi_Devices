# Import the ConnectHandler Function to create an Object for R1
from netmiko import ConnectHandler

# Parameters of Devices
password = "cisco"

R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.251",
    "username": "Admin",
    "password": password,
}

R2 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.252",
    "username": "Admin",
    "password": password,
}

R3 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.253",
    "username": "Admin",
    "password": password,
}

Devices=[R1, R2, R3]

# Connect to R1 via SSH
for Device in Devices:

    net_connect = ConnectHandler(**Device)

    # Retrieve the result of "show ip ospf neighbor" command with the hostname of each device and display it
    print(120*'*')
    print(net_connect.find_prompt()[:-1])
    output = net_connect.send_command('show ip ospf neighbor', use_textfsm=True)
    # For each neighbor N: access to its ID, Interface, Address and State
    for N in output:
        Id, Interface, Address, State=N.get('neighbor_id'), N.get('interface'), N.get('address'), ((N.get('state')).split('/'))[1]
        print(f"Neighbor {Id}\n     - Connected to it via the interface: {Interface} having the address: {Address}, its state is {State}")
        # End the SSH session for R1
        net_connect.disconnect()