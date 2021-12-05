import requests
from optparse import OptionParser
import re

def getUserInput():
    parser = OptionParser()
    parser.add_option('-c', dest = 'company', type = 'string', help = 'Enter `-c domain` to get its acquisitions')
    (options, args) = parser.parse_args()
    if not options.company:
        raise SystemExit
    else:
        return options.company

def send_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:82.0) Gecko/20100101 Firefox/82.0"}
    req = requests.get(url, headers=headers)
    content = req.text
    return content

# Get Company Name
def get_company_name(content):
    content = content
    # print(content)
    names = []
    companies = re.findall('(?:<strong class="c_identityChip-name">)(.*?)</strong>', content)
    for line in companies:
        line = line.lower()
        if company not in line:
            if line not in names:
                names.append(line)
    return(names)


# Get Company Date
def get_company_date(content):
    content = content
    dates = []
    date = re.findall('(?:<span>20)(.*?)</span>', content)
    for line in date:
        dates.append(line)
    return dates

if __name__ == "__main__":
    company = getUserInput()
    company = company.split('.')[0]
    company_cap = company.capitalize()
    acq_ulr = "https://index.co/company/" + company_cap +"/acquirees"

    content = send_request(acq_ulr)
    name = get_company_name(content)
    date = get_company_date(content)
    if name:
        res = dict(zip(name, date))
        print("Acquisitions for " + company + " are:\n")
        for acq in res:
            print("Company Name: " + acq + "\nAcquired on: 20" + res[acq] + "\n")
    else:
        print("No Acquisitions Found !\n")
