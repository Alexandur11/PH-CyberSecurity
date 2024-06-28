![PayHawk_Security](https://github.com/Alexandur11/PH-Security/assets/133868603/b9de5a5d-05e4-4636-afc7-c10942682898)

Welcome to PH-Security! This project provides tools for viewing and  analyzing network connections and visualizing Nessus scanning data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)




## Installation
1.  Ensure you have Python installed.
2.  To have access to past connection you will need to install and use WireShark. [Wireshark Tutorial for Beginners](https://www.youtube.com/watch?v=lb1Dw0elw0Q)
3.  To perform Vulnerability Scanning you will need to install and use Nessus. [Intruduction to vulnerability scanning with Nessus](https://www.youtube.com/watch?v=fG7HhqEJbTs&list=PLBf0hzazHTGM1gj702QWNKOjz12S0OWvx&pp=iAQB)
4.  Clone the repository:
     ```sh
      git clone https://github.com/Alexandur11/PH-Security.git
      ```
5.  Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Register to obtain API key from abuseIPDB and save it in your .env. [Register for API key](https://www.abuseipdb.com/register)


## Usage
1. To view the list with active and past connections you just have to run network_threat_checker/main.py
   ```sh
    I suggest commenting out one method, while running the other and not running them simultaneously for better experience.  
    ```
2. To view the charts for each report, run nessus_scannings/main.py
   ```sh
    This will load all charts, again comment out the methods you don't need.  
    ```
## Future usage
  If someone wants to use this project; 
  * To have your own reports to work with you will need to learn how to use Nessus. 
  * To use the feature for past connections with your personal past connections, you will need to learn how to use WireSHark to track those connections, and save them into a file.
