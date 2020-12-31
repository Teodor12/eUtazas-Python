
data_list = []
input_file = open('utasadat.txt')
for line in input_file:
    data_list.append(line.strip())
   

print('2. feladat')
print('A buszra ' + str(len(data_list)) + ' utas akart felszallni.')

print('3. feladat')
counter = 0
for data in data_list:
    x = data.split(' ')
    if x[3] == 'JGY':
        if x[4] == '0':
            counter +=1
    else:
        date = x[1].split('-')[0]
        if date > x[4]:
            counter +=1
print('A buszra ' + str(counter) + ' utas nem szallhatott fel.' )

print('4. feladat')
stations = {}
for data in data_list:
    x = data.split(' ')
    if x[0] not in stations.keys():
        stations[x[0]] = 0##adds a new key-value pair

for data in data_list:
    x = data.split(' ')
    stations[x[0]] += 1##counts passengers for eache station

max_station_key = list(stations.keys())[0]##first value's key!
for station, passenger in stations.items():
    if passenger > stations[max_station_key]:##key's value
        max_station_key = station##change key
print('A legtobb utas (%d fo) a %s. megalloban probalt felszallni.'%(stations[max_station_key], max_station_key))

print('6. feladat')
free_counter = 0
discount_counter = 0
for data in data_list:
    x = data.split(' ')
    if x[3] == 'JGY':
        continue
    if x[3] == 'NYB' or x[3] == 'TAB' and x[1].split('-')[0] < x[4]:
        discount_counter += 1
    if x[3] == 'RVS' or x[3] == 'GYK' or x[3] == 'NYP' and x[1].split('-')[0] < x[4]:
        free_counter +=1
print('Ingyenesen utazok szma : %d fo'%free_counter)
print('A kedvezmenyesen utazok szma : %d fo'%discount_counter)

def napokszama(e1,h1,n1,e2,h2,n2) -> int:
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1//4 - e1//100 + e1//400 + (h1*306+5)// 10 + n1-1
    h2 = (h2+9) % 12
    e2 = e2-h2 // 10
    d2 = 365*e2 + e2//4 - e2//100 + e2//400 + (h2*306+5)// 10 + n2-1
    return d2-d1

output_file = open('figyelmeztetes.txt', 'w')
for data in data_list:
    x = data.split(' ')
    if x[3] != 'JGY':
        start_date = x[1]
        end_date = x[4]
        e1 = int(start_date[0:4])
        h1 = int(start_date[4:6])
        d1 = int(start_date[6:8])

        e2 = int(end_date[0:4])
        h2 = int(end_date[4:6])
        d2 = int(end_date[6:8])
        if (napokszama(e1,h1,d1,e2,h2,d2)>=0 and napokszama(e1,h1,d1,e2,h2,d2) <= 3):
           output_file.write('%s %s\n'%(x[2], end_date[0:4] +'-'+end_date[4:6]+'-'+end_date[6:8]))

        
