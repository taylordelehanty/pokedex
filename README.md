#Pokedex

##Dependencies
  -Must have PyQt4 installed to use the Pokedex
###If you have Ubuntu, this process is easy:
Type `sudo apt-get install python3-pyqt4` in the terminal and you're done!
###If you are running another OS, both SIP and PyQt4 must be installed.
Follow these links and their instructions (the links to the source files are in these links):
  - Installation instructions: [SIP] (http://pyqt.sourceforge.net/Docs/sip4/installation.html)
  - Installation instructions: [PyQt4] (http://pyqt.sourceforge.net/Docs/PyQt4/installation.html)
  
##Run Program
1. Open terminal
2. Navigate to top directory in Pokedex
3. Run `python3 pokedex_client_menu`


##Features
###Not case sensitive
  - whether you type in `charmander`, `Charmander`, or `ChArMaNdEr` it will find the desired pokemon

###Offers suggestions based on partial name
  - if you don't remember how to spell a part of a Pokemon's name you can enter a part of it and the Pokedex will offer suggestions
    - i.e. if you want to search for `chandelure` but can only remember `chand`, you can type in `chand` and the Pokedex will offer `chandelure` as a suggestion
