# Automated Nmap Scanner

## Overview
This script automates the process of running an Nmap vulnerability scan on a target IP address. It obtains open ports and potential vulnerabilities on a system by using Nmap’s built-in scripts, making it a valuable tool for network audits and vulnerability assessments. The script also allows users to save the scan report in a text file and choose from different types of scans.

## Key Features
- Automates vulnerability scanning on specified target IP
- Utilizes Nmap’s `-sV` option to detect service versions and `--script vuln` to check for known vulnerabilities
- Offers multiple scan types: Vulnerability Scan, TCP SYN Scan, Aggressive Scan, and Ping Scan
- Allows users to save results into a file with time-stamped information
- Includes input validation to ensure valid scan type selection

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
- Without Saving Text File: 
  ```bash
  py september_creation.py <target_ip>
  ```
- With Saving Text File: 
  ```bash
      py september_creation.py <target_ip> [--save]
  ```

## Save Results to File
Use the `--save` flag to save the results to a text file:
```bash
py september_creation.py 192.168.1.1 --save
```

## Example Usage
Run Nmap vulnerability scan on a single IP address and save results as a text file:
```bash
py september_creation.py 192.168.1.1 --save
```

## Example Output
When running the vulnerability scan on the target IP address, the output may look like this:

Running Nmap Vulnerability scan on 192.168.1.1
Successful Scan! 

Scan Results: 

Starting Nmap 7.91 ( https://nmap.org ) at 2024-09-30 12:41 UTC 

Nmap scan report for 192.168.1.1 

Host is up (0.013s latency).

PORT STATE SERVICE VERSION

22/tcp open     ssh            OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | vulners: 

| CVE-2018-15473: 5.0 MEDIUM 

|_ CVE-2020-15778: 7.8 HIGH 

Nmap done: 1 IP address (1 host up) scanned in 12.45 seconds


## Scan Types
When prompted, you can select from the following scan types:

- Vulnerability Scan
- TCP SYN Scan
- Aggressive Scan
- Ping Scan
