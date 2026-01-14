# A lightweight Python-based log analysis tool designed to detect suspicious login activity by scanning authentication logs for repeated failed login attempts.

## This project simulates a basic blue-team security task: identifying potential brute-force attacks using real-world style log files such as auth.log.

## Features

 Reads system authentication logs (auth.log)

 Detects failed login attempts (Failed login, Failed password)

 Extracts and tracks IP addresses

 Flags suspicious IPs based on a user-defined threshold

 Displays summary statistics:

Total failed attempts

Unique IPs involved

 Graceful error handling for missing files and invalid inputs

## How It Works

1.The program reads a log file line by line.

2.It searches for failed authentication messages.

3.Extracts IP addresses following the keyword from.

4.Counts failed attempts per IP.

5.Compares counts against a threshold.

6.Prints security alerts if suspicious behavior is detected.

## Example Log File (auth.log)

This project includes an example log file (auth.log) used as input.

## Usage
Run The Script

analyzer.py
Provide inputs when prompted

Enter log file name:

auth.log

Enter threshold for error count:

3

## Sample Output
SECURITY ALERTS:

Suspicious IP detected: 192.168.1.10 (5 failed attempts)

LOG ANALYSIS COMPLETE.

Total failed login attempts: 12

Unique IPs involved: 4

## Requirements

Python 3.x

A log file formatted similarly to Linux authentication logs

No external libraries required — pure Python, pure logic.

## Future Improvements

Export alerts to a file

Add timestamp-based detection

Support multiple log formats

Real-time log monitoring

IP reputation lookup

