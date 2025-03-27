# **Decentralized-Ledger-Python**

## **📌 Project Overview**  
This repository contains a **decentralized ledger** built from scratch using **Python**. It is a learning project that demonstrates the core concepts of blockchain, including block creation, hashing, Proof of Work (PoW), and chain validation.  

## **🚀 Features**  
- Block creation with SHA-256 hashing  
- Proof of Work (PoW) implementation  
- Chain validation and security  
- Flask API to interact with the blockchain  
- Fully implemented in **Python**  

## **📂 Folder Structure**  
```
Decentralized-Ledger-Python/
│── blockchain.py        # Core blockchain logic
│── node.py              # Flask API to interact with blockchain
│── utils.py             # Helper functions
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

## **⚙️ Installation**  
Make sure you have **Python 3.8+** installed. Then, follow these steps:  

```bash
# Clone this repository
git clone https://github.com/yourusername/Decentralized-Ledger-Python.git

# Navigate to the project directory
cd Decentralized-Ledger-Python

# Install dependencies
pip install -r requirements.txt

# Run the blockchain node
python node.py
```

## **📡 API Endpoints**  
Once the node is running, you can interact with the blockchain using these API endpoints:  

| Method | Endpoint        | Description |
|--------|----------------|-------------|
| GET    | `/chain`       | Get the full blockchain |
| POST   | `/mine`        | Mine a new block |
| POST   | `/transaction` | Add a new transaction |

## **🛠️ Technologies Used**  
- **Python 3.8+**  
- **Flask** (for API)  
- **SHA-256** (for hashing)  
- **Proof of Work** (basic mining mechanism)  

## **📜 License**  
This project is open-source and available under the **MIT License**.  

---

### ✅ **Next Steps**  
- Add support for multiple nodes  
- Implement a peer-to-peer network  
- Add a simple front-end interface  

---

### **🔗 Contributing**  
Feel free to fork this repository and submit pull requests if you have improvements or new features to add!  

---

### **⭐ Star the Repo**  
If you find this project useful, don't forget to give it a ⭐ on GitHub!  

