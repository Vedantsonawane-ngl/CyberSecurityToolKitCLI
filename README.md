# 🔐 Cyber Security CLI Toolkit

A simple yet powerful **Command Line Cybersecurity Toolkit** built using Python.
This project provides essential security tools like password checking, hashing, cipher encryption, and breach detection — all in one CLI interface.

---

## 🚀 Features

* 🔑 **Password Checker**
  Evaluate password strength and detect weak/common passwords.

* 🔐 **Hash Generator**
  Generate secure hashes using:

  * MD5
  * SHA-256

* 🔄 **Caesar Cipher Tool**
  Encrypt and decrypt messages using shift-based cipher.

* ⚠️ **Breach Checker**
  Check if a password exists in a common leaked password dataset.

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Concepts Used:**

  * Hashing Algorithms
  * Encryption Techniques
  * File Handling
  * CLI Interaction

---

## 📂 Project Structure

```
cyber-cli-toolkit/
│
├── main.py
├── breach_checker.py
├── common_passwords.txt   # Used for breach detection
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/cyber-cli-toolkit.git
cd cyber-cli-toolkit
```

2. Run the program:

```
python main.py
```

---

## 🧠 How It Works

* The user enters a password to access the toolkit.
* After authentication, a menu appears:

  ```
  1. Password Checker
  2. Hash Generator
  3. Cipher Tool
  4. Breach Checker
  ```
* Each module performs its respective security operation.

---

## ⚡ Example Usage

```
Enter Command: breach
Checking password...
❌ Password found in breach database!
```

---

## 📌 Why `common_passwords.txt`?

This file contains a list of commonly used passwords collected from data breaches.
It allows the tool to:

* Quickly check weak passwords
* Simulate real-world breach detection

---

## 🏆 Future Improvements

* 🔍 API-based real breach checking (HaveIBeenPwned)
* 🔐 Advanced encryption (AES, RSA)
* 🌐 GUI version of the toolkit
* 📊 Password strength scoring system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Vedant Sonawane**
💡 Passionate about Cybersecurity & Development

---

## 🌟 Show Your Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧑‍💻 Share with others

---
