# DNS Spoofing Detection Tool Client Side

## Overview

This project is a client side DNS spoofing detection tool that identifies whether a DNS response is legitimate or potentially spoofed. The system captures domain requests from a browser extension and verifies DNS responses using multiple parameters such as IP address TTL ASN and trust score.

## Features

* Real time domain monitoring using a Chrome extension
* DNS response verification using IP address comparison TTL validation and ASN lookup
* Trust score calculation based on multiple factors
* Classification of results as legitimate suspicious or spoofed
* Attack simulation module for demonstration
* Comparison of request and response DNS parameters
* Flask based web interface

## Working Principle

When a user visits a website the browser extension captures the domain name. The backend server performs DNS resolution using both local and trusted DNS servers. It then extracts key parameters such as IP address TTL and ASN. A trust score is calculated based on these parameters and the system classifies the response as legitimate suspicious or spoofed.

## Architecture

* Chrome Extension sends domain request to Flask API
* Flask API calls DNS resolver modules
* DNS responses are analyzed using trust score logic
* Final result is displayed in browser popup

## Detection Factors

* Domain represents the requested website
* IP address is compared between local and trusted DNS
* TTL indicates response validity
* ASN verifies network ownership
* Trust score combines all factors for classification

## Attack Simulation

The project includes a simulation module to demonstrate DNS spoofing without performing real network attacks. When simulation is enabled selected domains are intentionally manipulated to create mismatched DNS responses.

### Enable simulation

```bash
python simulate.py
```

### Disable simulation

```bash
python stop_simulation.py
```

## Example Output

Request domain google dot com
Request IP 142.12.20.36
Request TTL 120

Response domain google dot com
Response IP 1.2.3.4
Response TTL 300

Result score 20
Status spoofed

## Technologies Used

* Python with Flask framework
* dnspython for DNS resolution
* IPWhois for ASN lookup
* JavaScript for Chrome extension
* HTML and CSS for interface

## Limitations

* Direct DNS response capture is restricted by browser security
* DNS over HTTPS may prevent visibility of DNS traffic
* Depends on trusted DNS servers for validation

## Future Scope

* Integration with machine learning models
* Real time browser warning system
* Deployment as a full browser security extension
* Integration with external threat intelligence services

## Screenshots

```md
![Output](screenshots/output.png)
```

## Conclusion

This project demonstrates a practical method to detect DNS spoofing using client side request capture and backend DNS validation. It provides a clear understanding of DNS security and attack detection mechanisms.

## Author

Developed as a cybersecurity academic project
