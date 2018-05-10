#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script.
"""



import sys
import os
import getopt





#
#börja bygga mitt script
#

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Georges Kayembe"
EMAIL = "kayss.g@gmail.com"
VERSION = "1.0"
USAGE = """{program} - Print my name. By {author} ({email}), version {version}.
Usage:
    {program} [options] name
Options:
-h, --help           Visa hjläptext.
-v, --version        Visa versionen av programmet.
-s, --silent         Visa inga detaljer.
--verbose            Visa mindre text.

ping=<url>           pinga en webbsida.
get=<url>            Hämta och skriv ut innehållet i en en webbsida.
output=<filename>    Hämta och spara webbsida på en file.
input=<filename>     Hämta dagens citat på JSon format.
quote=<url>          Visa upp dagens citat.
title=<url>          Hämta och visa titeln för en webbsida.

""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)


#parameters
SILENT = 'code.txt'
VERBOSE = True
OUTPUT = 'default.out'
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def printUsage(exitStatus):
    """
    informationen om scripten och exit
    """
    print(USAGE)
    sys.exit(exitStatus)


def printVersion():
    """
    skriva ut versionen av programmet
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)


def pinga(pingaHemsida):
    """
    pinga en webbsida
    """
    import requests

    url = pingaHemsida
    req = requests.head(url)

    print("Request to ", url)
    print("Recieved status code: ", req.status_code)
    sys.exit(EXIT_SUCCESS)

def pingaCode(pingaHemsida):
    """
    pinga en webbsida
    """
    import requests

    url = pingaHemsida
    req = requests.head(url)

    print("Recieved status code: ", req.status_code)
    fhand = str(req.status_code)
    htmlfile = open(SILENT, 'a')
    htmlfile.write(str(fhand)+'\n')
    htmlfile.close()
    print("code saved in code.txt")
    sys.exit(EXIT_SUCCESS)

def code(fhand):
    """spara code i en fil"""
    files = open(fhand, 'r')
    line = files.read()
    print(line)
    sys.exit(EXIT_SUCCESS)


def geta(getHemsida):
    """
    hämta en hemsida
    """
    from bs4 import BeautifulSoup
    import requests

    url = getHemsida
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup)
    sys.exit(EXIT_SUCCESS)

def out(webbsite):
    """
    spara en hemsida i en file
    """
    from bs4 import BeautifulSoup
    import requests

    url = webbsite
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    fhand = str(soup)
    htmlfile = open(OUTPUT, 'w')
    htmlfile.write(fhand)
    htmlfile.close()
    print("file saved")
    sys.exit(EXIT_SUCCESS)

def citat(citation):
    """
    hämta dagens citat
    """
    import requests
    url = citation
    req = requests.get(url)

    print("\nThe response status code is:\n", req.status_code)

    print("\nThe response body is:\n", req.text)

    json = req.json()
    print("\nQuote of today is:\n\"{quote}\"\n".format(quote=json["quote"]))
    sys.exit(EXIT_SUCCESS)

def inputQuote(jsonObject):
    """
    hämta json objekt
    """
    import json

    jsonfile = open(jsonObject, "r")
    jsonObject = json.load(jsonfile)

    for quote in jsonObject['quotes']:
        print(quote + '\n')
    sys.exit(EXIT_SUCCESS)


def getSeo(webbsite):
    """
    Get the title seo
    """
    import requests
    from bs4 import BeautifulSoup as bs


    r = requests.get(webbsite)
    r.enconding = "utf-8"
    page = bs(r.text, "html.parser")
    patternTitle = page.find_all("title")

    patternH1 = page.find_all("h1")
    nombreH1 = len(patternH1)

    patternH2 = page.find_all("h2")
    nombreH2 = len(patternH2)

    patternA = page.find_all("a")
    nombreA = len(patternA)


    if len(patternTitle) == 1:
        print("\nSidan har (endast) ett element <title> :")
        print(patternTitle[0].get_text())
        print("Som innehåller %s tecken"%(len(patternTitle[0].get_text())))
        print("---------------------------\n")

    else:
        print("Sidan har fler än ett element <title> eller inget alls!")
        print(patternTitle)

    if nombreH1 != 0:
        print("Sidan innehåller %s element <h1>"%(nombreH1))
    else:
        print("Sidan innehåller inga element <h1>")

    if nombreH2 != 0:
        print("Sidan innehåller %s element <h2>"%(nombreH2))
    else:
        print("Sidan innehåller inga element <h2>")

    if nombreA != 0:
        print("Sidan innehåller %s element <a>"%(nombreA))
    else:
        print("Sidan innehåller inga element <a>")

def getSeoFile(filename):
    """
    Get the title seo
    """
    from bs4 import BeautifulSoup

    fhand = open(filename, 'r')
    lines = fhand.read()

    soup = BeautifulSoup(lines, 'html.parser')

    patternTitle = soup.find_all("title")

    patternH1 = soup.find_all("h1")
    nombreH1 = len(patternH1)

    patternH2 = soup.find_all("h2")
    nombreH2 = len(patternH2)

    patternA = soup.find_all("a")
    nombreA = len(patternA)


    if len(patternTitle) == 1:
        print("\nSidan har (endast) ett element <title> :")
        print(patternTitle[0].get_text())
        print("Som innehåller %s tecken"%(len(patternTitle[0].get_text())))
        print("---------------------------\n")

    else:
        print("Sidan har fler än ett element <title> eller inget alls!")
        print(patternTitle)

    if nombreH1 != 0:
        print("Sidan innehåller %s element <h1>"%(nombreH1))
    else:
        print("Sidan innehåller inga element <h1>")

    if nombreH2 != 0:
        print("Sidan innehåller %s element <h2>"%(nombreH2))
    else:
        print("Sidan innehåller inga element <h2>")

    if nombreA != 0:
        print("Sidan innehåller %s element <a>"%(nombreA))
    else:
        print("Sidan innehåller inga element <a>")


def getSeoJson(webbsite):
    """
    Get the title seo
    """
    import requests
    from bs4 import BeautifulSoup as bs
    import json


    myObj = json.loads('{"website" : "", "title" : "", "title_antal_tecken" : "0",\
     "h1" : "0", "h2" : "0", "a" : "0"}')


    r = requests.get(webbsite)
    r.enconding = "utf-8"
    page = bs(r.text, "html.parser")
    patternTitle = page.find_all("title")

    patternH1 = page.find_all("h1")
    nombreH1 = len(patternH1)

    patternH2 = page.find_all("h2")
    nombreH2 = len(patternH2)

    patternA = page.find_all("a")
    nombreA = len(patternA)

    myObj["website"] = webbsite
    myObj["title"] = patternTitle[0].get_text()
    myObj["title_antal"] = len(patternTitle)
    myObj["title_antal_tecken"] = len(patternTitle[0].get_text())
    myObj["a"] = nombreA
    myObj["h2"] = nombreH2
    myObj["h1"] = nombreH1

    #parsed = json.loads(myObj)
    print(json.dumps(myObj, indent=4, sort_keys=True))

def getSeoFileJson(filename):
    """
    Parse fil and print to json
    """
    from bs4 import BeautifulSoup
    import json

    myObj = json.loads('{"filename" : "", "title" : "", "title_antal_tecken" : "0",\
     "h1" : "0", "h2" : "0", "a" : "0"}')

    fhand = open(filename, 'r')
    lines = fhand.read()

    soup = BeautifulSoup(lines, 'html.parser')

    patternTitle = soup.find_all("title")

    patternH1 = soup.find_all("h1")
    nombreH1 = len(patternH1)

    patternH2 = soup.find_all("h2")
    nombreH2 = len(patternH2)

    patternA = soup.find_all("a")
    nombreA = len(patternA)

    myObj["filename"] = filename
    myObj["title"] = patternTitle[0].get_text()
    myObj["title_antal"] = len(patternTitle)
    myObj["title_antal_tecken"] = len(patternTitle[0].get_text())
    myObj["a"] = nombreA
    myObj["h2"] = nombreH2
    myObj["h1"] = nombreH1

    #parsed = json.loads(myObj)
    print(json.dumps(myObj, indent=4, sort_keys=True))


def titre(title):
    """
    Show off how to scrape information from a webpage.
    """
    import urllib.request
    import  urllib.parse
    import  urllib.error
    import re
    url = title
    html = urllib.request.urlopen(url).read()
    links = re.findall(b'<title.*?>(.+?)</title>', html)
    print(links)
    sys.exit(EXIT_SUCCESS)

def titreFile(files):
    """
    Show off how to scrape information from a webpage.
    """
    import re
    fhand = open(files, 'r')
    lines = fhand.read()
    links = re.findall('<title.*?>(.+?)</title>', lines)
    print(links)
    sys.exit(EXIT_SUCCESS)


def parseOptions():
    """
    options and arguments
    """

    # Switch through all options
    try:
        global OUTPUT

        opts, args = getopt.getopt(sys.argv[1:], "hv:oji", [
            "help",
            "version",
            "output",
            "json",
            "input"
        ])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                exitStatus = EXIT_SUCCESS
                printUsage(exitStatus)

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-o", "--output"):
                OUTPUT = args[0]
                webbsite = args[2]
                out(webbsite)

            elif opt in ("-json", "--json"):
                if args[0] == "seo":
                    getSeoJson(args[1])
                    sys.exit(EXIT_SUCCESS)
                elif args[1] == "seo":
                    getSeoFileJson(args[0])
                    sys.exit(EXIT_SUCCESS)


            elif opt in ("-input", "--input"):
                if args[1] == "seo":
                    getSeoFile(args[0])
                    sys.exit(EXIT_SUCCESS)



            else:
                assert False, "Unhandled option"

        if args[0] == 'ping':
            arg = args[1]
            pinga(arg)

        elif args[0] == 'ping-history':
            fhand = 'code.txt'
            code(fhand)

        elif args[0] == 'quote':
            citation = 'http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php'
            citat(citation)

        elif args[0] == 'get':
            arg = args[1]
            geta(arg)


        elif args[0] == 'silent':
            arg = args[2]
            pingaCode(arg)
        elif args[0] == 'input':
            if args[2] == 'quote':
                jsonObject = args[1]
                inputQuote(jsonObject)
            elif args[2] == 'title':
                files = args[1]
                titreFile(files)

        elif args[0] == 'title':
            arg = args[1]
            titre(arg)

        elif args[0] == 'seo':
            arg = args[1]
            getSeo(arg)


        else:
            exitStatus = EXIT_USAGE
            printUsage(exitStatus)


    except Exception as err:
        print(err)
        """""exitStatus = EXIT_USAGE
        print(printUsage(exitStatus))"""
        # Prints the callstack, good for debugging, comment out for production
        # traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)


def main():
    """
    Main function to carry out the work.
    """

    parseOptions()



if __name__ == "__main__":
    main()
