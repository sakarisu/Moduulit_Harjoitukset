import mysql.connector
def etsiLentok(yhteys, ICAO):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT name, municipality FROM airport WHERE ident = '{ICAO}';")
    return kursori.fetchone()
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='0532189764',
         autocommit=True
         )
tulos=etsiLentok(yhteys, input('Anna lentokentän ICAO-tunniste: ').upper())
print(f'Lentokentän nimi on "{tulos[0]}" ja kunta, jossa se sijaitsee, on "{tulos[1]}"')
