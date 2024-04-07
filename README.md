# Apache Web Server Deployment Script

## Overview
This script automates the deployment of an Apache web server on a Linux system. It installs the Apache web server package and configures the firewall to allow HTTP traffic (port 80) to the server.

## Prerequisites
- Linux operating system (tested on Ubuntu and Debian-based distributions)
- Administrative privileges to install packages and configure firewall rules

## Usage
1. Download the `deploy_apache.py` script onto your Linux system.
2. Open a terminal window.
3. Navigate to the directory containing the `deploy_apache.py` script.
4. Run the script with administrative privileges using the following command:
    ```bash
    sudo python3 ./Server.py
    ```
5. Follow the on-screen instructions. The script will automatically install Apache web server and configure the firewall.

## Notes
- This script is designed for deployment on Ubuntu and Debian-based Linux distributions. It may require modifications to work on other distributions.
- Always review and test the script in a controlled environment before deploying it to production servers.
- Customizations such as additional configurations or installation of other services like MySQL can be added to the script as needed.
