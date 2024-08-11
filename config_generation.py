def commandset(count):
    file = open('D:/MMC-HC/test.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command1 = "interface " + x[2]
    command2 = "description connected to " + x[3]
    command3 = "switch port access vlan " + x[1]
    return(command1,command2,command3)

print(commandset(0))

