import sys, os, random
import numpy

def applyRulesDetection(suspectFile):
        print(".",end="")
        #print("\n[Malicious file] -",suspectFile)

def detect(path):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)):
            print(os.path.join(path,i))
            #applyRulesDetection(os.path.join(path,i))
        if os.path.isdir(os.path.join(path,i)):
            detect(os.path.join(path,i))

def copyArray(src,dst,start,end,prefix_src,prefix_dst):
    for i in range(start,end):
        #print("start:",start," end:",end," pSrc:",prefix_src," pDst:",prefix_dst," lenSrc:",len(src)," lenDst:",len(dst))
        #print("dst:",(prefix_dst+i)," src:",(prefix_src+i))
        dst[prefix_dst+i] = src[prefix_src+i]

def encodeScriptPolyglot(script,imgSrc,imgDst):

    with open(imgSrc,'rb') as f1: bytesImgSrc = f1.read(10000000);
    with open(script,'rb') as f3: linesScriptToHide = f3.read(10000000); # payload js
    payloadLen = len(linesScriptToHide)

    leidos = len(bytesImgSrc)
    #en el fichero no puede haber 0x27
    # Si no tiene 0x27 entonces al final del script pongo : ' y al final de fichero '
    # // FF D8 FF E0 00 10 bla bla --> posicion 4 y 5 tam de cabecera
    tamCabeceraActual = bytesImgSrc[4]*256+bytesImgSrc[5]

    jpgFinal = bytearray(leidos+tamCabeceraActual+291)
    # 291=0x0123 - Todo tal cual le quito la cabecera, le pongo el tamano nuevo de cabecera
    copyArray(bytesImgSrc,jpgFinal,0,4,0,0)  #copio los primeros 4 bytes --> tipicamente FFD8 FFE0, la cabecera
    jpgFinal[4] = 0x01; jpgFinal[5] = 0x23; #copio nuevo tamano

    copyArray(bytesImgSrc,jpgFinal,6,10,0,0)

    for i in range(0,tamCabeceraActual-6):
        if bytesImgSrc[10+i] == 0x00:
        #if ByteToHex(bytesImgSrc[10+i]) == "00":
            jpgFinal[10+i] = 0x01
        else:
            jpgFinal[10+i] = bytesImgSrc[10+i]

    for i in range(0,291-tamCabeceraActual):
        jpgFinal[(10+tamCabeceraActual-6)+i] = 0x01;  # es 0x01 pq el 0x00 da error en script bash

    jpgFinal[tamCabeceraActual+4] = 0x0D;
    jpgFinal[tamCabeceraActual+4+1] = 0x0A;

    copyArray(linesScriptToHide,jpgFinal,0,payloadLen,0,tamCabeceraActual+4+2)
    copyArray(bytesImgSrc,jpgFinal,0,leidos-tamCabeceraActual-4,tamCabeceraActual+4,291+4)

    with open(imgDst,'wb') as f2: f2.write(jpgFinal)


def menu():
    print("\n====================================================================")
    print("   _____                                      _____   _           _   ")
    print("  |  __ \                                    / ____| | |         | |  ")
    print("  | |__) |   ___   __      __   ___   _ __  | |  __  | |   ___   | |_ ")
    print("  |  ___/   / _ \  \ \ /\ / /  / _ \ | '__| | | |_ | | |  / _ \  | __|")
    print("  | |      | (_) |  \ V  V /  |  __/ | |    | |__| | | | | (_) | | |_ ")
    print("  |_|       \___/    \_/\_/    \___| |_|     \_____| |_|  \___/   \__|")
    print("\n    ")
    print(" -- --=[ PowerGlot 0.1 (April 2020)]")
    print(" -- --=[ Author: Dr. Alfonso Munoz (@mindcrypt) & Abraham Pasamar]")
    print("====================================================================")

    print("\n Usage: powerglot [-d | -o ] [payload] [image src] [image output]")

    print("\n Powerglot encodes an auto-run powershell script using polyglots. A loader is not needed.")
    print("\n optional arguments:\n")
    print("  -o  Offensive mode - Encode/Hide a script in a file using polyglots");
    print("")
    print("\n  -d  Defensive mode - Allow to detect and analyze the presence of polyglots in any file in the filesystem (recursive from path)")
    print("")
    print(" examples:\n")
    print("  #powerglot -o script.ps1 cat.jpg catMalicious.jpg")
    print("  #powerglot -o script.sh cat.jpg catMalicious.jpg")
    print("  #powerglot -o script.php cat.jpg catMalicious.jpg")

    print("  #powerglot -d ./")
    print("")
    print("------------------------")

def main(paramIn):

    if len(sys.argv)<2:
        menu()
    else:
        if (sys.argv[1] == "-o") and len(sys.argv)==5:
               if sys.argv[1] == "-o":
                   encodeScriptPolyglot(sys.argv[2],sys.argv[3],sys.argv[4])

        elif sys.argv[1] == "-d" and len(sys.argv)==3:
               print("--= [Detecting polyglots]...")
               detect(sys.argv[2])
        else:
            menu()

main(sys.argv)
