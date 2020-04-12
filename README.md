# Powerglot
Powerglot encodes an auto-run powershell script using polyglots. A loader is not needed.

In red-team exercises or offensive tasks, the masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc.

Powerglot is a multifunctional attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) in a digital image. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system.

PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first open-source tool that allows to search for the presence of masked information in polyglots, information that could be useful to achieve persistence in a system or to hide malware

Features:

1. Encode powershell/shell script in a image using steganography, difficulting its detection. It is not necessay a loader. The image is a polyglot. 
To execute the image allows to execute another code (polyglot) to recover/execute the hidden information (payload).

2. PowerGlot works with several formats. Mainly, JPEG format.

3. Powerglot is the first open-source tool to detect (malicious) polyglots, specially the result of some public tools as Truepolyglot or stegoSploit. 
We works in several formats: JPEG, PNG, GIF, BMP, ZIP, PDF, MP3, etc.

# Installation

# Usage & Parameters

# Future work. Doing

# Author & license

This project has been developed by Dr. Alfonso Muñoz and Abraham Pasamar. The code is released under the GNU General Public License v3.


