#!/bin/python3
import os, sys, marshal, getpass;
from argparse import ArgumentParser
from time import sleep;
WHITE=('\033[38;5;15m');
GREEN=('\033[38;5;10m');
PURPLE=('\033[38;5;93m');
DARK=('\033[38;5;245m');
BLUE=('\033[38;5;50m');
RED=('\033[38;5;9m');
BOLD=('\033[01m');
script = (os.path.basename(sys.argv[0]))
sig = (r'\x57\x61\x58\x78\x58\x20\x77\x34\x73\x20\x68\x33\x72\x65\x0a')
sig2 = (r'\x57\x61\x58\x78\x58')
user = (getpass.getuser())
if os.path.isdir("/data/data/com.termux"):
    banner = ('one')
elif os.path.isdir(f"/home/{user}"):
    banner = ('two')
if ".py" in script:
    script_pretty = (script.replace(".py",""))
else:
    script_pretty = script
def lock():
    print(f"""{BOLD}
            ┳━┓┓ ┳┏━┓┏┏┓┳━┓┳━┓┓━┓┳ ┳┳━┓┳
            ┃━┛┗┏┛┏━┛┃┃┃┃━┫┃┳┛┗━┓┃━┫┃━┫┃
            ┇   ┇ ┗━━┛ ┇┛ ┇┇┗┛━━┛┇ ┻┛ ┇┇━┛
            {RED} kOcoOcoOcoOOOOOOOOOOO: '
            {RED}.OOcdOcdOcdOOOOOOOOOOO: Ok,  ;::,
            {RED}.OOd;,ckO,lOd;,ckOx;,cl :xxo. ,dx
            {RED}.OO .o ;O ,O .d ;O .d ;x:;;;;; 'x
            {RED}.OO..; cO ,O..; cO..; cOOOOOOO 'x
            {RED};OOOolxOOldOOolxOOOolxOOOOOOOO 'x
            {RED},',;cdOOOOOl...cO..Ol...cO..OO 'x    
        {DARK}:;lxO0Oko,.{RED},xOO..O..O..O..O..O..OO 'x
       {DARK}:KXo{PURPLE},...,{DARK}oKK: {RED}lOo...lO'.Oo...lO'.OO 'x
      {DARK}lXO   {PURPLE}kOOd'{DARK} kXl {RED}dOkcxOxccxOOxccxOOOO 'x
      {DARK}XX'   {PURPLE}.OOOO.{DARK}.XX {RED};Od lx '; dx '; dOOO 'x
      {DARK};;    {PURPLE}.OOOO.{DARK}.XX {RED},Od lx ;: ox ;: oOOO 'x
            {PURPLE}ldddd.{DARK}.OO {RED}'dx;dOd:;oOOd:;oOOOO 'x
   {BLUE}..................... {RED}lOk:xOxc:dOk:xOOO 'x
   {BLUE}ccccccccccccccccccccc {RED},Od lx ,; dd lOOO 'x
  {BLUE}.cccccccc:...:cccccccc {RED},Od lx ,: od lOOO 'x
  {BLUE} cccccccc. . .cccccccc {RED},Ok:xOd::dOk:xOOO 'x
  {BLUE} ccccccccc. .ccccccccc {RED},Oxxxxxxxxxxxxxxl ;x
  {BLUE} cccccccccc;cccccccccc {RED},k'''''''''''''',lxx
  {BLUE} ccccccccccccccccccccc {RED}  .................
{BLUE}┌────────────────────────────────────────────────────────────┐
{PURPLE}│{DARK}{sig}{GREEN}{PURPLE}│
└────────────────────────────────────────────────────────────┘
""")
    return
def lock_termux():
    print(f"""{BOLD}
           {DARK}.:llll:.
         {DARK}cxlloooollxc
        {DARK}0:ox.    {DARK}.xo:0
       {DARK}ldck        {DARK}kcdl
       {DARK}dlol        {DARK}ldcd
     {BLUE}'okkkkllllllllkkkOo'
     {BLUE}X,{DARK}................,X
     {BLUE}X{DARK}'......{RED}cddc{DARK}......'{BLUE}X
     {BLUE}X{DARK}'.....{RED}dk..kd{DARK}.....'{BLUE}X
     {BLUE}X{DARK}'.....'{RED}0ll0'{DARK}.....'{BLUE}X
     {BLUE}X{DARK}'......{RED}dxxd{DARK}......'{BLUE}X
     {BLUE}X{DARK}'......{RED}'oo'{DARK}......'{BLUE}X
     {BLUE}X{DARK},................,X
     {BLUE}.llllllllllllllllll.{BLUE}
    ┌─────────────────────┐
    {PURPLE}│{DARK}{sig2}{GREEN}{PURPLE} │
    └─────────────────────┘
 """)
    return
def echo_s(data):
	blank = ' '
	s = ''
	for l in blank:
		sys.stdout.write('\r')
		sys.stdout.write(f"{PURPLE}[{BLUE}-{GREEN}*{BLUE}-{PURPLE}] {BLUE}{data} {PURPLE}[{BLUE}-{GREEN}*{BLUE}-{PURPLE}]")
		s += (f"{l}")
		sys.stdout.flush()
		sleep(0.3)
	print()
def msg(name=None):                                                            
    add_help = (f'''{script}
{WHITE}./{PURPLE}{script} {WHITE}-i {GREEN}script{WHITE}.{GREEN}py {WHITE}-o {GREEN}new_marshal_script{WHITE}.{GREEN}py
''')
    return add_help
def advanced_usage():
    print(f'''
{RED}HINT{WHITE}: {BLUE}If the script you{WHITE}'{BLUE}re trying to encode is not in the same directory{WHITE} - 
{BLUE}you{WHITE}'{BLUE}re currently in{WHITE}, {BLUE}you will need to enter the whole path to the script{WHITE}.
{BLUE}Or just run this script in the same directory as the script you want to encode{WHITE}.
{BLUE}Example{WHITE}: 
{WHITE}./{PURPLE}{script} {WHITE}-i {GREEN}/home/{user}/Documents/{GREEN}script{WHITE}.{GREEN}py {WHITE}-o {GREEN} new_script{WHITE}.{GREEN}py
{BLUE}If you forget an arg in the command{WHITE}, {BLUE}you will just be prompted to enter it{WHITE}.
    ''')
class encrypt():
    def __init__(self):
        if banner == ("one"):
            lock_termux()
        elif banner == ("two"):
            lock()
        parser = ArgumentParser(description=(f"{WHITE}::{PURPLE}{script_pretty}{WHITE}::") , usage=(msg()))
        parser.add_argument('-i', '--input' ,required=False, action='store', help=f"{BLUE}Input script")
        parser.add_argument('-o', '--output' ,required=False, action='store', help=f"{BLUE}Output script")
        parser.add_argument('-u', '--usage' ,required=False, action='store_true', help=f"{BLUE}Advanced Usage")
        args = parser.parse_args()
        if args.usage:
            advanced_usage()
            sys.exit()
        try: 
            if args.input: 
                input_file = (args.input)
            else:
                data = ("You didn't supply the name of the script to encode | Enter it now")
                echo_s(data)
                input_file = input( f"{PURPLE}[ {DARK}{user}{BLUE}@{DARK}{script_pretty}{WHITE} ~ {PURPLE}]{WHITE}$ {BLUE} " )
            if args.output:
                new_script = (args.output)
            else:
                data = ("You didn't supply a name for the new Marshal encoded script | Enter it now")
                echo_s(data)
                new_script = input( f"{PURPLE}[ {DARK}{user}{BLUE}@{DARK}{script_pretty}{WHITE} ~ {PURPLE}]{WHITE}$ {BLUE} " )
            if input_file == new_script:
                data = (f"{RED} You cannot name the new Marshal encoded script the same as the origianl script")
                echo_s(data)
                sys.exit()
            elif input_file != new_script:
                self.py3encode(input_file, new_script)
        except KeyboardInterrupt:
            data = (f"{RED}\n\nKeyboard interruption\nExiting\n")
            echo_s(data)
            sys.exit()    
    def py3encode(self, input_file, new_script):
        data = (f"Encoding script{WHITE}: {PURPLE}{input_file} {BLUE}to {PURPLE}{new_script}")
        echo_s(data)
        out_file = input_file.replace('.py', '')
        lolol = open(input_file, 'r').read()
        code = compile(lolol,'','exec')
        data = marshal.dumps(code)
        line0 = ("#!/bin/python3")
        line1 = ("import marshal")
        line2 = (f"#{sig}")
        line3 = (f"exec(marshal.loads({repr(data)}))")
        with open(f"{new_script}" ,'a') as out:
            out.write(f'{line0}\n{line1}\n{line2}\n{line3}\n')
        out.close()
encrypt()