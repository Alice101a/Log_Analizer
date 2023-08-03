import re
import argparse

def parse_log_file(log_file_path, threshold, log_format="auth.log", date_range=None, output_file=None):
    suspicious_ips = {}

    # Regular expression to match IP address in log lines
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    with open(log_file_path, "r") as file:
        for line in file:
            # Filter by date range if provided
            if date_range and not any(date in line for date in date_range):
                continue

            # Extract IP address using regex
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group()
                if "Failed login" in line:
                    suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1

    # Output results to console or file
    if output_file:
        with open(output_file, "w") as outfile:
            for ip, attempts in suspicious_ips.items():
                if attempts >= threshold:
                    outfile.write(f"Suspicious IP: {ip} with {attempts} failed login attempts.\n")
    else:
        for ip, attempts in suspicious_ips.items():
            if attempts >= threshold:
                print(f"Suspicious IP: {ip} with {attempts} failed login attempts.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log File Parser")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("-t", "--threshold", type=int, default=3, help="Failed login attempts threshold")
    parser.add_argument("-f", "--format", default="auth.log", help="Log file format (default: auth.log)")
    parser.add_argument("-d", "--date-range", nargs="+", help="Filter by date range (e.g., 'Aug 1', 'Aug 2')")
    parser.add_argument("-o", "--output", help="Output results to a file")

    args = parser.parse_args()

    parse_log_file(args.log_file, args.threshold, args.format, args.date_range, args.output)

