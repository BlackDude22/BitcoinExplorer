# BitcoinExplorer

Šioje repozitorijoje realizuota paprasta Bitcoin naršyklė.

# Diegimas

Programa parašyta Python 3 kalba. Reikalingi moduliai `django` ir `paramiko`. 

Direktorijoje `/bce/` paleiskite komandą `python manage.py runserver`

Naršyklėje nueikite į `127.0.0.1:8000/BitcoinExplorer`

# Funkcionalumai

Pradiniame lange rodomi 10 paskutinių iškastų blokų. Nurodomas bloko numeris, hash'as, iškasimo laikas, bei už bloką gautas atlygis. Paspaudus ant bloko numerio parodoma detalesnė informacija apie bloką. Be anksčiau minėtų savybių, bloko aprašyme galima pamatyti ankstesnio bloko hash'ą, patvirtinimų skaičių, nonce, visų bloko transakcijų skaičių, visų bloko transakcijų sumą ir visų bloko transakcijų mokestį.
