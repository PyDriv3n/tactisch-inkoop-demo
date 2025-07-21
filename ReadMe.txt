📋 Overzicht
In deze demo vind je:

src/demo.py: Python-script om inkoopdata in te lezen en een Excel- en PDF-rapport te genereren
data_example/inkoop_export.xlsx: voorbeeldinput (maak zelf aan volgens instructies)
output_example/: map waarin de gegenereerde rapporten komen
requirements.txt: lijst met benodigde Python-pakketten
LICENSE: MIT-licentie

📂 Repository-structuur
├── src/
│   └── demo.py              	# Hoofdscript voor één-klik rapportage
├── data_example/
│   └── inkoop_export.xlsx   	# Voorbeeldinput (maak dit bestand zelf aan volgens onderstaande instructies)
├── output_example/         	# Map voor gegenereerde rapporten
├── requirements.txt         	# Benodigde Python-packages
├── README.md                	# Deze documentatie
└── LICENSE                  	# MIT-licentie

📄 Voorbeeldinput (inkoop_export.xlsx)
Maak in de map data_example een Excelbestand inkoop_export.xlsx met ten minste de volgende kolommen:
Kolom	Beschrijving
leverancier	Naam van de leverancier (tekst)
bedrag	Bestedingsbedrag per order (getal)
levertijd	Levertijd in dagen (getal, optioneel)
Je kunt hiervoor:
1.	Een nieuw Excelbestand openen en de kolomnamen invoeren.
2.	Enkele voorbeeldrijen toevoegen, bijvoorbeeld:

leverancier | bedrag | levertijd
--------------------------------
Bedrijf A   | 1250   | 3
Bedrijf B   |  750   | 5
Bedrijf A   | 1800   | 2
3.	Opslaan als data_example/inkoop_export.xlsx.
Zo heb je direct een werkend voorbeeld om het script te testen.

▶️ Gebruik
Vanuit de projectroot (tactisch-inkoop-demo)

python src/demo.py --input data_example/inkoop_export.xlsx --output output_example/kpi_rapport

Parameters:
--input of -i: pad naar het Excelbestand

--output of -o: basisnaam voor outputbestanden (zonder extensie)

Na uitvoering vind je in output_example/:
kpi_rapport.xlsx
kpi_rapport.pdf


Veelvoorkomende fouten
Errno 2: No such file or directory: controleer of je in de projectroot zit en dat data_example/inkoop_export.xlsx bestaat.
Onjuiste mapstructuur: zorg dat src/demo.py, data_example/inkoop_export.xlsx en output_example/ op de juiste plek staan.
Parameters missen: geef altijd zowel --input als --output op, anders stopt het script met een fout.

📝 requirements.txt

Plaats de volgende regels in requirements.txt zodat het script alle benodigde dependencies installeert:
pandas
openpyxl
matplotlib
reportlab

License

Dit project is gelicenseerd onder de MIT License.



