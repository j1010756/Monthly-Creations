# test comment for github
# import necessary packages for processing, parsing, and date
import subprocess
import argparse
from datetime import datetime

# vulnerability scan on single ip
def run_nmap_vuln_scan(target_ip):
    try:
        
        # print text showing can is running on target
        print(f"Running Nmap Vulnerability scan on {target_ip}")
        
        # get commands to run nmap, get version numbers, and find vulnerabilies by using scripts
        nmap_commands = ['nmap', '-sV', '--script', 'vuln', target_ip]
        
        # get results from scan, including output and error messages
        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        
        # return results if successful
        if results.returncode == 0:
            print("Sucessful Scan!\n")
            return results.stdout
        
        # error message if unsuccessful
        else:
            print(f"Error: {results.stderr}")
            return None
        
    # create exception if scan cannot start
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
   
# TCP SYN scan on single IP
def run_nmap_tcp_syn_scan(target_ip):
    try:
        
        # print text showing can is running on target
        print(f"Running Nmap TCP SYN scan on {target_ip}")
        
        # get commands to run nmap and TCP SYN scan
        nmap_commands = ['nmap', '-sS', target_ip]
        
        # get results from scan, including output and error messages
        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        
        # return results if successful
        if results.returncode == 0:
            print("Sucessful Scan!\n")
            return results.stdout
        
        # error message if unsuccessful
        else:
            print(f"Error: {results.stderr}")
            return None
        
    # create exception if scan cannot start
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# aggressive scan on single ip
def run_nmap_aggressive_scan(target_ip):
    try:
        # print text showing can in running on target
        print(f"Running Nmap Aggressive scan on {target_ip}")
        
        # get commands to run nmap and aggressive scan
        nmap_commands = ['nmap', '-A', target_ip]
        
        # get results from scan, including output and error messages
        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        
        # return results if successful
        if results.returncode == 0:
            print("Sucessful Scan!\n")
            return results.stdout
        
        # error message if unsuccessful
        else:
            print(f"Error: {results.stderr}")
            return None
        
    # create exception if scan cannot start
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
        
# ping scan on single ip
def run_nmap_ping_scan(target_ip):
    try:
        # print text showing can in running on target
        print(f"Running Nmap Ping scan on {target_ip}")
        
        # get commands to run nmap and aggressive scan
        nmap_commands = ['nmap', '-sn', target_ip]
        
        # get results from scan, including output and error messages
        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        
        # return results if successful
        if results.returncode == 0:
            print("Sucessful Scan!\n")
            return results.stdout
        
        # error message if unsuccessful
        else:
            print(f"Error: {results.stderr}")
            return None
        
    # create exception if scan cannot start
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
        
     
# save report
def save_report(target_ip, report, scan_type):
    # get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # create a report header with date and time
    report_header = f"Nmap {scan_type} Scan Report\nTarget: {target_ip}\nDate: {current_time}\n\n"
    
    # save the scan result to a text file
    filename = f"nmap_{scan_type}_scan_{target_ip}.txt"
    with open(filename, 'w') as file:
        file.write(report_header + report)
    
    print(f"Report saved as {filename}")
   
# main process to run functions    
def main():
    # set up argument parsing for the script
    parser = argparse.ArgumentParser(description='Automated Nmap Scanner')
    
    # add target
    parser.add_argument('target_ip', help='Target IP address or range')
    
    # save file option
    parser.add_argument('--save', action='store_true', help='Save the output to a text file')

    args = parser.parse_args()

    # display scan options
    print("Select the scan type you want to perform:")
    print("1. Vulnerability Scan")
    print("2. TCP SYN Scan")
    print("3. Aggressive Scan")
    print("4. Ping Scan")

    # input validation
    while True:
    # get user input
        scan_choice = input("Enter the number corresponding to your choice: ")
        if scan_choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Enter a number between 1 and 4.")

    # run the chosen scan
    if scan_choice == "1":
        scan_type = "vulnerability"
        scan_result = run_nmap_vuln_scan(args.target_ip)
    elif scan_choice == "2":
        scan_type = "TCP SYN"
        scan_result = run_nmap_tcp_syn_scan(args.target_ip)
    elif scan_choice == "3":
        scan_type = "aggressive"
        scan_result = run_nmap_aggressive_scan(args.target_ip)
    elif scan_choice == "4":
        scan_type = "ping"
        scan_result = run_nmap_ping_scan(args.target_ip)
    else:
        print("Invalid choice. Please select a valid scan option.")
        return

    # print scan results if scan works 
    if scan_result:
        print("\nScan Results:\n")
        print(scan_result)

        # save the report if prompted
        if args.save:
            save_report(args.target_ip, scan_result, scan_type)

if __name__ == "__main__":
    main()