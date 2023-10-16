from Site import CVC
from Site import Decolar

def main():
    cvc_scraper = CVC()
    cvc_scraper.search_flights()

    decolar_scraper = Decolar()
    decolar_scraper.search_flights()

if __name__ == "__main__":
    main()
