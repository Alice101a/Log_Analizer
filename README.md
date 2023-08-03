# Log_Analizer
The Python script is a flexible log file parser that reads a log file, extracts IP addresses, and identifies suspicious IPs with a high number of failed login attempts. It provides several options to customize the parsing behavior.


The script reads the specified log file (e.g., "auth.log" or "syslog") and processes each line. It uses regular expressions to extract IP addresses from log lines. If a log line contains the phrase "Failed login," the script considers it as a failed login attempt and counts the number of attempts for each IP address.

After processing the entire log file, the script identifies IPs that have more failed login attempts than the specified threshold. It then outputs the list of suspicious IPs along with the number of failed attempts for each IP.

Features:

Command-line Interface: The script uses the argparse module to handle command-line arguments, making it easy to customize the parsing behavior.

IP Extraction: The script uses regular expressions to identify IP addresses in log lines, allowing it to handle log files in different formats.

Failed Login Detection: The script looks for log lines containing the phrase "Failed login," enabling it to count the failed login attempts.

Failed Login Threshold: The user can specify the threshold for failed login attempts. IPs with more failed attempts than the threshold will be considered suspicious.

Date Range Filtering: Users can provide a date range to filter log lines. Only log lines containing dates within the specified range will be processed.

Output to File: The user can specify an output file to save the results. If no output file is provided, the results will be printed to the console.

Usage on Kali Linux:
To use the script on Kali Linux, follow these steps:

Save the Script: Copy the enhanced log file parsing script code and save it to a Python file (e.g., log_file_parser.py) on your Kali Linux system.

Install Python: Kali Linux typically comes with Python pre-installed. You can check the Python version by running the following command in the terminal:


python --version


If Python is not installed, you can install it using the package manager apt:

sudo apt update
sudo apt install python3


Install Required Modules: The script uses regular expressions, which are included in the Python standard library. No additional modules need to be installed.

Make the Script Executable: If necessary, make the Python script executable:


chmod +x Log_Analizer.py

Run the Script: Now, you can run the script from the terminal with the desired options:

python log_file_parser.py /path/to/log_file.log -t 5 -d "Aug 1" "Aug 2" -o output.txt


Replace /path/to/log_file.log with the actual path to the log file you want to analyze. The script will process the log file and display the list of suspicious IPs with more than 5 failed login attempts between "Aug 1" and "Aug 2". If an output file is specified (e.g., output.txt), the results will be saved to that file; otherwise, they will be printed to the console.

