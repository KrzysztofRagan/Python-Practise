
#GENERATORY NIE PRZECHOWUJĄ MIEJSCA W PAMIĘCI. MOGĄ BYĆ WYKONYWANE TYLKO RAZ. 

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

port_connections1 = ((port1,port2) for port1 in ports for port2 in ports)

port_connections2 = ((port1,port2) for port1 in ports for port2 in ports if port1 != port2 )

port_connections3 = ((port1,port2) for port1 in ports for port2 in ports if port1 < port2 )

counter1 = 0
counter2 = 0
counter3 = 0

for x in port_connections1:
  counter1 += 1

for x in port_connections2:
  counter2 += 1

for x in port_connections3:
  counter3 += 1


print(counter1)
print(counter2)
print(counter3)