from urllib.request import urlopen
import doctest
global i
i=1
with urlopen('https://en.wikipedia.org/wiki/Ducati_Motor_Holding_S.p.A.') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
        print(i)
        i+=1
doctest.testmod()
