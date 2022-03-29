import argparse
import sys

from core import LeagueNickChecker, REGIONS
from core.logger import Logger

__version__ = '1.0.0'

regions = ', '.join(REGIONS)

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--apikey', type=str, help='your riot dev API key', required=True)
parser.add_argument('-r', '--region', type=str, help=f'riot api region. Regions: {regions}', required=True)
parser.add_argument('-w', '--wordlist', type=str, help=f'wordlist file path', required=True)

parser.add_argument('--verbose', help="increase output verbosity", action="store_true")

parser.add_argument('-v', '--version', action='version', version=f'%(prog)s v{__version__ }')
#parser.add_argument('-o', '--output', help='output file name')

args = parser.parse_args()

logger = Logger(verbose=args.verbose)

def main():
  logger.banner(__version__)
  checker = LeagueNickChecker(args.apikey, args.wordlist, args.region, verbose=args.verbose)
  checker.start()
  

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print('\n\nbye!')
    sys.exit()