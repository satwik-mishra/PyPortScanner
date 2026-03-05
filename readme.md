# PyPortScanner 🔎

A fast **multithreaded TCP port scanner** built with Python.
This tool scans a target host for open ports, identifies common services, and attempts basic **banner grabbing** to detect running applications.

The project is built for **learning cybersecurity and networking concepts** such as reconnaissance, socket programming, and multithreaded scanning.

---

# 🚀 Features

* ⚡ **Multithreaded port scanning** for faster results
* 🔎 **Banner grabbing** to detect services running on open ports
* 🖥️ **Service detection** for common ports
* 🎨 **Colored terminal output** for better readability
* 💻 **CLI arguments** for flexible scanning
* 🌐 **Domain or IP support**

---

# 📂 Project Structure

```
pyportscanner
│
├── main.py
├── scanner.py
├── banner_grabber.py
├── services.py
├── utils.py
│
├── requirements.txt
└── README.md
```

| File                | Description                                             |
| ------------------- | ------------------------------------------------------- |
| `main.py`           | Entry point of the tool, handles CLI arguments          |
| `scanner.py`        | Core multithreaded scanning logic                       |
| `banner_grabber.py` | Retrieves service banners from open ports               |
| `services.py`       | Maps common ports to services                           |
| `utils.py`          | Helper functions like DNS resolution and colored output |
| `requirements.txt`  | Python dependencies                                     |

---

# 🛠️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/satwik-mishra/PyPortScanner.git
cd pyportscanner
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Usage

Basic command:

```
python main.py -t <target> -p <port-range> -th <threads>
```

### Example

```
python main.py -t scanme.nmap.org -p 1-1000 -th 200
```

Example output:

```
Scanning 45.33.32.156 from port 1 to 1000

[OPEN] Port 22 | Service: SSH | Banner: OpenSSH
[OPEN] Port 80 | Service: HTTP | Banner: Apache

Scan Complete
```

---

# ⚙️ Command Line Options

| Argument | Description                 | Example          |
| -------- | --------------------------- | ---------------- |
| `-t`     | Target domain or IP address | `-t example.com` |
| `-p`     | Port range to scan          | `-p 1-1000`      |
| `-th`    | Number of scanning threads  | `-th 200`        |

---

# 🧠 How It Works

1. The tool resolves the target domain into an IP address.
2. A **queue of ports** is created.
3. Multiple **threads scan ports simultaneously**.
4. If a port is open:

   * The service is identified using a port-service mapping.
   * A **banner grabbing attempt** is made.
5. Results are printed with colored output.

This scanning approach is similar to how professional tools like **Nmap** perform reconnaissance.

---

# 📚 Learning Objectives

This project helps understand:

* Python **socket programming**
* **TCP networking**
* **Multithreading**
* **Network reconnaissance**
* Basic **service fingerprinting**

---

# ⚠️ Disclaimer

This project is created **for educational purposes only**.

Do **NOT** scan systems without proper authorization. Unauthorized scanning may violate laws or network policies.

---

# 🔮 Future Improvements

Possible upgrades:

* Save scan results to **JSON / CSV**
* Add **progress bar for scanning**
* Implement **UDP scanning**
* Add **OS fingerprinting**
* Build a **GUI version**

---

# 👨‍💻 Author

Created as a beginner cybersecurity project to understand network scanning and reconnaissance techniques.
