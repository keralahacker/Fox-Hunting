import argparse
from access_points import get_scanner


def scan(tracked_bssid):
    tracked_bssid = 'a8:bd:27:8f:01:53'
    last_quality = 0;
    wifi_scanner = get_scanner()
    print('All Access Points:\n%s' % wifi_scanner.get_access_points())
    try:
        while True:
            for ap in wifi_scanner.get_access_points():
                if ap.bssid == tracked_bssid:
                    if (last_quality < ap.quality):
                        print('Hotter')
                    elif (last_quality > ap.quality):
                        print('Colder')
                    else:
                        print('Same')
                    last_quality = ap.quality
    except KeyboardInterrupt:
        print('\nHalting Scanning')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bssid', help='the bssid to track', type=str)
    args = parser.parse_args()
    scan(args.bssid)



if __name__ == '__main__':
    main()