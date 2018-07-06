import sys
import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

def CreateJsonNode(data, source, note, typeOfData, links, master):
    json = "{"
    json += "\"Data\" : \"" + data + "\","
    json += "\"Source\" : \"" + source + "\","
    json += "\"Note\" : \"" + note + "\","
    json += "\"TypeOfData\" : \"" + typeOfData + "\""
    if master == True or len(links) > 1:
        json += ","
        json += "\"Link\" : ["
        if master == True:
            json += "{\"Uid\" : \"master\"}"
            if len(links) > 0:
                json += ","
        if len(links) > 0:
            i = 0
            for link in links:
                if i == len(links) - 1:
                    json += "{\"Uid\" : \"" + "mdr" + "\"}"
                else:
                    json += "{\"Uid\" : \"" + "mdr" + "\"},"
                i += 1
        json += "]"
    json += "}"
    return json


if len(sys.argv) != 3:
    print "Error need 2 arg"
    sys.exit(0)
    
jsonFileName = sys.argv[1]
nameDomain = sys.argv[2]

# Open the file with the json
fichier = open(jsonFileName, "r")
jsonText = fichier.read()
fichier.close()

data = Payload(jsonText)
listJsonData = list()
#data+typeOfdata POUR LES LINKS

#domain_whois
a = dict(data.domain_whois)

source = "Whois - Trouver le nom de l'enregistreur du domaine"
if "registrar" in a:
	if len(a["registrar"]) > 0:
		listJsonData.append(CreateJsonNode(a["registrar"], source, "Nom ou organisation qui a reserve le nom de domaine", "Nom", [], True))

# The json result
jsonResult = ""
for element in listJsonData:
    jsonResult += element + ","
jsonResult = jsonResult[0:len(jsonResult)-1]

#save in file
fichier = open(jsonFileName, "w")
fichier.write(jsonResult)
fichier.close()

