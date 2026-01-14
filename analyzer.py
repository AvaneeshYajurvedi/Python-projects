print("SIMPLE LOG ANALYZER MODULE\n")
log_file=input("Enter log file name: \n")
threshold=int(input("Enter threshold for error count: \n"))
failed_ips={}
try:
    file=open(log_file,'r')
    for line in file:
        if "Failed login" in line or "Failed password" in line:
            parts = line.split()
            if "from" in parts:
                ip = parts[parts.index("from") + 1]
            else:
                continue
            if ip in failed_ips:
                failed_ips[ip]+=1
            else:
                failed_ips[ip]=1
    file.close()
    print("SECURITY ALERTS:\n")
    alert_found=False
    for ip,count in failed_ips.items():
        if count>=threshold:
            print(f"Suspicious IP detected: {ip} ({count} failed attempts)")
            alert_found=True
    if not alert_found:
        print("No security alerts found.\n")
    print("\nLOG ANALYSIS COMPLETE.\n")
    print(f"Total failed login attempts: {sum(failed_ips.values())}")
    print(f"Unique IPs involved: {len(failed_ips)}")
except FileNotFoundError:  
    print(f"Error: The file '{log_file}' was not found.\n")
except ValueError:
    print("Error: Invalid input for threshold. Please enter a valid integer.\n")