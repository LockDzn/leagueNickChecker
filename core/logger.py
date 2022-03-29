class colors: 
  CEND      = '\33[0m'
  CBOLD     = '\33[1m'
  CITALIC   = '\33[3m'
  CURL      = '\33[4m'
  CBLINK    = '\33[5m'
  CBLINK2   = '\33[6m'
  CSELECTED = '\33[7m'

  CBLACK  = '\33[30m'
  CRED    = '\33[31m'
  CGREEN  = '\33[32m'
  CYELLOW = '\33[33m'
  CBLUE   = '\33[34m'
  CVIOLET = '\33[35m'
  CBEIGE  = '\33[36m'
  CWHITE  = '\33[37m'

  CBLACKBG  = '\33[40m'
  CREDBG    = '\33[41m'
  CGREENBG  = '\33[42m'
  CYELLOWBG = '\33[43m'
  CBLUEBG   = '\33[44m'
  CVIOLETBG = '\33[45m'
  CBEIGEBG  = '\33[46m'
  CWHITEBG  = '\33[47m'

  CGREY    = '\33[90m'
  CRED2    = '\33[91m'
  CGREEN2  = '\33[92m'
  CYELLOW2 = '\33[93m'
  CBLUE2   = '\33[94m'
  CVIOLET2 = '\33[95m'
  CBEIGE2  = '\33[96m'
  CWHITE2  = '\33[97m'



class Logger:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def banner(self, version):
    version_text = f'{colors.CGREEN2}{version}{colors.CEND}'
    github_text = f'{colors.CBLUE2}github.com/lockdzn/leagueNickChecker{colors.CEND}'

    print(f"""
  _                        _  _ _    _    ___ _           _           
 | |___ __ _ __ _ _  _ ___| \| (_)__| |__/ __| |_  ___ __| |_____ _ _ 
 | / -_) _` / _` | || / -_) .` | / _| / / (__| ' \/ -_) _| / / -_) '_|
 |_\___\__,_\__, |\_,_\___|_|\_|_\__|_\_\\___|_||_\___\__|_\_\___|_|  
            |___/ {version_text} - {github_text}
""")

  def info(self, string="", verbose=""):
    if self.verbose and verbose != "":
      print('[-]', verbose)
      return
    elif string != "":
      print('[-]', string)

  def success(self, string="", verbose=""):
    if self.verbose and verbose != "":
      print(f'{colors.CGREEN}[+]{colors.CEND}', verbose)
      return
    elif string != "":
      print(f'{colors.CGREEN}[+]{colors.CEND}', string)

  def error(self, string="", verbose=""):
    if self.verbose and verbose != "":
      print(f'{colors.CRED}[!]{colors.CEND}', verbose)
      return
    elif string != "":
      print(f'{colors.CRED}[!]{colors.CEND}', string)
  
  def warn(self, string="", verbose=""):
    if self.verbose and verbose != "":
      print(f'{colors.CRED}[!]{colors.CEND}', verbose)
      return
    elif string != "":
      print(f'{colors.CYELLOW}[*]{colors.CEND}', string)
    print(f'', string)
