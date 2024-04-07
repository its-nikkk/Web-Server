import subprocess

def install_apache():
	print("Installing Apache web Server...")
	subprocess.run(["sudo", "apt", "update"])
	subprocess.run(["sudo", "apt", "install", "-y", "apache2"])

def configure_firewall():
	print("Configuring firewall to allow HTTP traffic...")
	subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", "80", "-j", "ACCEPT"])
	subprocess.run(["sudo", "iptables-save"])

def main():
	install_apache()
	configure_firewall()

	print("Apache web server deployment completed.")

if __name__ == "__main__":
	main()
