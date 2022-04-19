# clients = ['A-company', 'B-company']
# projects = [300,400,1500,2340,50]

# investments = {c:p for c in clients for p in projects if c == 'A-company' and p<1000 or c == 'B-company' and p>1000}

# print(investments)


ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
port_connections1 = [(port1,port2) for port1 in ports for port2 in ports]

port_connections = [(port1,port2) for port1 in ports for port2 in ports if port1 != port2 ]

no_doublets = list(set(tuple(sorted(x)) for x in port_connections))



print(port_connections1)
print(len(port_connections1))
print('------------------------')

print(port_connections)
print(len(port_connections))

print('------------------------')


print(no_doublets)
print(len(no_doublets))
