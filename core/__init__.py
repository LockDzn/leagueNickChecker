from time import sleep
import requests
import os.path
import sys

from core.logger import Logger

REGIONS = [
  "BR1",
  "EUN1",
  "EUW1",
  "JP1",
  "KR",
  "LA1",
  "LA2",
  "NA1",
  "OC1",
  "RU",
  "TR1",
]

logger = Logger()

class LeagueNickChecker():
  def __init__(self, key, wordlist, region, verbose):
    self.key = key
    self.wordlist = wordlist
    self.key_is_valid = self.verifyKey()
    self.words = self.read_wordlist()

    self.verifyRegion(region)

    logger.verbose = verbose

  def verifyKey(self):
    url = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/Skf9JdMnVgvf9G1w9wtBhNmawpcqJNyTz0PoNR8P3b-9y0I?api_key={self.key}'
    request = requests.get(url)
    code = request.status_code

    if code == '403':
      logger.error('riot dev API key invalid.\n')
      return False;
    else:
      logger.success('riot dev API key is ok.\n')
      return True;

  def verifyRegion(self, region):
    if region.upper() in str(REGIONS):
      self.region = region.upper()
    else: 
      regions = ', '.join(REGIONS)

      logger.error(f'region "{region}" does not exist')
      print(f'      Regions: {regions}\n')
      sys.exit()

  def read_wordlist(self):
    wordlist_exists = os.path.exists(self.wordlist)

    if wordlist_exists:
      f = open(self.wordlist, "r")
      words = f.read().split('\n')
      f.close()
      return words
    else:
      logger.error(f'file not found: {self.wordlist}\n')
      sys.exit()

  def request(self, word):
    url = f'https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{word}?api_key={self.key}'
    return requests.get(url)

  def start(self):

    #for i in progressbar(range(len(self.words)), "Computing: ", 40):
    #  sleep(0.1)

    active = True;
    word_index = 0;
    pause = False;

    while active:
      if len(self.words) == word_index:
        active = False;
        break

      if not pause:
        word = self.words[word_index]
        r = self.request(word)

        if word == '':
          print('\nfinished\n')
          active = False
          break

        if r.status_code == 200:
          summoner_name = r.json()["name"]
          summoner_level = r.json()["summonerLevel"]

          logger.info(verbose=f'{summoner_name} - Lvl: {summoner_level} (Already exists)')
          word_index += 1
        elif r.status_code == 404:
          logger.success(f'{word}', f'{word} (Doesn\'t exist)')
          word_index += 1
        elif r.status_code == 429:
          logger.error(verbose=f'API Rate Limit ({r.status_code})')
          sleep(120)
        else:
          logger.error(f'API Error ({r.status_code})')
        
