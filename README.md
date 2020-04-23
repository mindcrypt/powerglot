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
# Example de polyglot in PDF
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
Some examples to detect polyglots in our filesystem
```
```

# Future work. Doing
- We are working to support different file formats for encoding information in polyglots. Currently, we support several techniques in JPEG and PDF.
- We are working to incorporate rules for the detection of polyglots in different formats. Currently, the presence of StegoSploit in JPEG files is detected.

# Author & license

This project has been developed by Dr. Alfonso Muñoz and Abraham Pasamar. The code is released under the GNU General Public License v3.


