![Py2Marshal](https://img.shields.io/badge/Py2Marshal-v3.0-orange.svg)
![Python | Marshal](https://img.shields.io/badge/Python-Marshal-purple.svg)
![Python3](https://img.shields.io/badge/Python-V3-orange.svg)
![Python3](https://img.shields.io/badge/Python%20-Powered-pink.svg)
![Bash](https://img.shields.io/badge/Bash%20-Installer-magenta.svg)
<!--<p align="center">
  <img src="https://imgur.com/obwRNVf.png" width="200" height="200">
</p><hr>-->

# **Py2Marshal** 

<p align="center">
  <img width="130" height="133" src="https://imgur.com/WFurHjU.png">
</p>

### Compile Python code into Marshal from Termux, Windows or Linux. 
<hr>

#### Tested with Termux, Linux and Windows. Installer only works with Termux and Linux as of right now because, well, Windblows.
#### Features bash completion script if you have bash-completion installed. 

##### Or, just simply run `py2marshal.py` and you'll be prompted to enter the input and output names of the script you're trying to compile.
##### ***\*Now has tab suggestions at input prompts****
######  Uses all standard libraries execept in Windows. The script uses the library `readline` which comes standard in Termux/Linux when you install Python but it does not come standard in Windows when you install Python. The script will attempt to download pip, and will attempt to install the Windows equivalent: `pyreadline`. 
- When you're using it in interactive mode(not using the --input and --output flags) when at an input prompt, press tab and it will give you suggestions of files in the same working directory you're in.
<hr> 

|Feature            |Termux | Linux | Windows | WSL
|-------------------|-----|-------|---|------------|
|Compiles to Marshal    |✓    |✓      |✓  |   ✓
| Has installer | ✓    |    ✓   |   | ✓
| Has suggestion in-script | ✓ | ✓  | | ✓
| Has bash-completion|✓ |✓ |  | ✓

##### To run:
```shell
git clone https://github.com/Waxxx333/Py2Marshal
cd Py2Marshal
chmod +x py2marshal.py
./py2marshal.py -h
```
#### Example
```bash
./py2marshal.py -i script_to_encode.py -o new_marshal_script.py
```
##### To install: 
```bash
git clone https://github.com/Waxxx333/Py2Marshal
cd Py2Marshal
chmod +x install.sh
sudo ./install.sh
py2marshal -h
```



<p align="center">
  <img src="https://imgur.com/7mAzEXl.png">
</p> <br>

<p align="center">
  <img src="https://imgur.com/nsCFhlO.png">
</p> <br>

> Todos

- [ ] Make `install.sh` work with Winblows
  - [x] Include `pip`
  - [x] Create `install.sh`

##### ***__\*2nd revision__****
<hr><hr>

