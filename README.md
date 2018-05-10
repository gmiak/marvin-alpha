# marvin-alpha
Här utveckla jag nya moduler för att hämta tester från webbsidor och skriva data till fil.
Så här ser det ut när du kör programmet:

1. Generell användning av programmet 
* python3 marvin-cli.py [options] command [arguments-to-the-command]
    
2. Pinga en webbsida
* python3 marvin-cli.py ping http://google.com

3. Hämta och skriv ut innehållet i en webbsida
* python3 marvin-cli.py get https://google.com

4. Hämta och spara webbsidan på en fil
* python3 marvin-cli.py --output=humans.txt get https://google.com

5. Visa upp dagens citat genom att hämta det från en webbtjänst
* python3 marvin-cli.py quote

6. Hämta och visa titeln för en webbsida
* python3 marvin-cli.py title http://yahoo.fr

7. Visa help-meny
* python3 marvin-cli.py --help

# Syftet med projektet
När man jobbar med webbutveckling, eller utveckling i allmänhet, händer det att man vill hämta information från andra webbservrar, bearbeta informationen och lagra undan på filer eller i en databas.
Python via sina interna moduler stödjer sådana aktiviteter.
Jag använder några av dessa moduler för att utföra projektet till exempel :
1. json : som hjälper att läsa och skriva innehåll till och från en JSON-fil.
2. requests : Pinga en webbsida. Man skickar en HTTP-request till webbplatsen för att kontrollera att den är uppe och svarar.
3. BeautifulSoup : Scrapa information från en webbsida. Att scrapa information från webbsida innebär att man laddar hem webbsidan och låter ett program gå igenom innehållet på webbsidan för att hämta ut viss information.
4. Och m.m ..

