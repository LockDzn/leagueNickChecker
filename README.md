<p align="center">
	<h1 align="center">leagueNickChecker</h1>
  <p align="center">bulk check unused nicks in League of Legends</p>
	<p align="center">
		<a href="https://asciinema.org/a/481829" target="_blank">
			<img src=".github/demo.gif" width="450" />
		</a>
	</p>
</p>

## Install

```console
# clone the repository
$ git clone https://github.com/lockdzn/leagueNickChecker.git

# go to folder
$ cd leagueNickChecker

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```console
# exemple:
$ python3 leagueNickChecker.py -k RGAPI-d5d7c315-8526-4f69-816e-81fa25702e4f -r BR1 -w /home/ryan/Documentos/verbs1.txt
```

```console
$ python3 leagueNickChecker.py -h

arguments:
  -h, --help            show this help message and exit
  -k APIKEY, --apikey APIKEY
                        your riot dev API key
  -r REGION, --region REGION
                        riot api region. Regions: BR1, EUN1, EUW1, JP1, KR, LA1, LA2, NA1, OC1, RU, TR1
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file path
  --verbose             increase output verbosity
  -v, --version         show program's version number and exit


```
