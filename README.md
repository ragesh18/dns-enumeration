# dns-enumeration
A Python-based DNS reconnaissance tool that performs DNS record enumeration and attempts zone transfer (AXFR) attacks to identify misconfigured DNS servers.

# DNS Reconnaissance & Zone Transfer Tool

A Python-based **DNS reconnaissance tool** that performs DNS record enumeration and attempts DNS zone transfers (AXFR) to identify misconfigurations in domain name systems.  
This tool is intended for **offensive security labs, red-team engagements, and cyber security learning environments**.

---

## 🔍 Overview

DNS is a critical component of network infrastructure and often a valuable source of intelligence during reconnaissance.  
This script helps enumerate DNS records and test for **insecure DNS zone transfer configurations**, which can expose internal hostnames, subdomains, and network structure.

---

## ⚙️ Features

- Enumerates common DNS record types:
  - `A`, `MX`, `CNAME`, `TXT`, `SOA`, `CAA`
- Uses a DNS resolver to query authoritative records
- Attempts **DNS Zone Transfer (AXFR)** against discovered name servers
- Displays all retrieved zone data if AXFR is successful
- Simple interactive command-line interface

---

## 🛠️ Technologies Used

- **Python 3**
- **dnspython**
  - `dns.resolver` – DNS queries
  - `dns.zone` – Zone parsing
  - `dns.query` – AXFR requests

---

## 📌 Reconnaissance Workflow

```
Target Domain Input
↓
DNS Record Enumeration
↓
Name Server Identification
↓
AXFR (Zone Transfer) Attempt
↓
Zone Data Disclosure (if misconfigured)
```
---

## ▶️ Usage

### 1️⃣ Install Dependencies
```bash
pip3 install dnspython
```
### 2️⃣ Run the Script
```bash
python3 dns_enu__.py
```

### 3️⃣ Provide Input When Prompted
```text
Enter the target domain: example.com
Enter the DNS record type (A, MX, CNAME, TXT, SOA, CAA): A MX TXT
```

### 4️⃣ Optional Zone Transfer
```yaml
**Do you want to attempt a zone transfer? [YES/NO]: YES**
```
---
## 📤 Sample Output
```text
A Records for example.com:
 - 93.184.216.34

MX Records for example.com:
 - 10 mail.example.com.

[*] Trying AXFR on ns1.example.com (192.0.2.53)
❌ AXFR failed for ns1.example.com: Transfer failed


If successful:

Zone Transfer Successful from ns1.example.com!
www 3600 A 192.168.1.10
mail 3600 A 192.168.1.20
```
----
