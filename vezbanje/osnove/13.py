import sys

pitanja = ["Ime", "Zanimanje", "Mesto rodjenja"]
odgovori = ["Pavle", "Student", "Arandjelovac"]

for a,b in zip(pitanja, odgovori):
    print("Tvoje " + a + " je: Moje " + a +" je "+ b)