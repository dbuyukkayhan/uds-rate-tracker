from playsound import playsound
from forex_python.converter import CurrencyRates
from time import sleep
c = CurrencyRates()

old = c.get_rate('USD', 'TRY')

while(True):
    print(c.get_rate('USD', 'TRY'))
    now =  c.get_rate('USD', 'TRY')
    print(f"eski deger = {old} \nyeni deger = {now}")

    if(now > old):
        print("yukseldi")
        playsound("zort.mp3")
        old = now
        break

    else:
        print("degisiklik olmadi\n\n")


    sleep(60)

