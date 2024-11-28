# Automated Nmap Scanner

## Overview
This script automates the process of running various Nmap scans on a target IP address, including vulnerability, TCP SYN, aggressive, and ping scans. It provides flexibility in scan options to gather a range of network information and potential vulnerabilities, making it a versatile tool for network audits and vulnerability assessments. The script also allows users to save scan reports in text files, CSV, or JSON format with a timestamp.

## Key Features
- Automates multiple scan types on a specified target IP, including vulnerability, TCP SYN, aggressive, and ping scans
- Utilizes Nmap’s options:
    - -sV with --script vuln to detect service versions and known vulnerabilities
    - -sS for a TCP SYN scan to identify open ports
    - -A for an aggressive scan, which combines version detection, OS detection, and more
    - -sn for a ping scan to quickly check host availability
- Allows users to save results into either text, CSV, or JSON files with time-stamped information for audit and tracking purposes


## Installation

### System Requirements
- Python 3.9+ installed on your machine
- Nmap installed and added to the system PATH

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/j1010756/Monthly-Creations.git
    ```

2. Navigate to the directory:
    ```bash
    cd Monthly-Creations
    ```

3. Run the script using Python:
    ```bash
    py monthly_creation.py <target_ip>
    ```

## Save Results to File
Use the `--save` flag to save the results to a text, JSON, or CSV file:

  ```bash
  py monthly_creation.py <target_ip> --save
  ```

## Scan Types
When prompted, you can select from the following scan types:

- Vulnerability Scan
- TCP SYN Scan
- Aggressive Scan
- Ping Scan

## File Save Types
When prompted, you can select from the following file types to save to:
- TXT (Default)
- JSON
- CSV

## Example Usage
Run Nmap TCP SYN scan on single IP address and save results as text file:
```bash
py monthly_creation.py 192.168.56.102 --save
```

_Select the scan type you want to perform:_
1. Vulnerability Scan
2. TCP SYN Scan
3. Aggressive Scan
4. Ping Scan

_[Selecting scan 2]_

## Example Output
Sucessful Scan!

Scan Results:

Starting Nmap 7.95 ( https://nmap.org ) at 2024-10-30 22:08 Mountain Daylight Time

Nmap scan report for 192.168.56.102

Host is up (0.00088s latency).

Not shown: 977 closed tcp ports (reset)

PORT      STATE SERVICE

21/tcp    open  ftp

22/tcp    open  ssh

80/tcp    open  http

135/tcp   open  msrpc

139/tcp   open  netbios-ssn

445/tcp   open  microsoft-ds

3306/tcp  open  mysql

3389/tcp  open  ms-wbt-server

4848/tcp  open  appserv-http

5985/tcp  open  wsman

7676/tcp  open  imqbrokerd

8080/tcp  open  http-proxy

8181/tcp  open  intermapper

8383/tcp  open  m2mservices

9200/tcp  open  wap-wsp

49152/tcp open  unknown

49153/tcp open  unknown

49154/tcp open  unknown

49155/tcp open  unknown

49156/tcp open  unknown

49157/tcp open  unknown

49158/tcp open  unknown

49159/tcp open  unknown

MAC Address: 08:00:27:99:1C:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.81 seconds

_Choose a file format to save the report:_
1. TXT (Default)
2. JSON
3. CSV
_Enter your choice (1/2/3):_

_[Selecting option 3]_

Report saved as nmap_TCPSYN_scan_192.168.56.101.csv

## Proof of Value
While this tool does not provide a full and comprehensive vulnerability assessment, it automates several important steps of using Nmap for network enumeration and vulnerability scanning and provides a detailed report of its findings that can be exported in a number of formats, as depicted in the demonstrations below. It can provide an excellent and quick starting point for a full vulnerability assessment, or can be used on its own to quickly identify a system’s most glaring vulnerabilities.


## Demonstration (Metasploitable Server):
### TCP SYN Scan
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_tcpsyn.png?raw=true)
### Aggressive Scan
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_aggressive1.png?raw=true)
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_aggressive2.png?raw=true)
### Ping Scan
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_ping.png?raw=true)
### Vulnerability Scan
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_vuln1.png?raw=true)
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_vuln2.png?raw=true)
### JSON Export
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_json.png?raw=true)
### CSV Export
![alt text](https://github.com/j1010756/Monthly-Creations/blob/main/img/demo_csv.png?raw=true)
