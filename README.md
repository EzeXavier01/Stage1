# Project Documentation

## **📌 Description**
This Django-based API classifies numbers based on mathematical properties and provides a fun fact about them. The API returns the following details in JSON format:

- Whether the number is **prime**.
- Whether the number is **perfect**.
- The **sum of its digits**.
- If the number is an **Armstrong number**.
- Whether the number is **odd or even**.
- A **fun fact** fetched from the Numbers API (`http://numbersapi.com/`).

The API is designed to be lightweight, efficient, and easy to integrate into other applications or services.

---

## **🚀 API Endpoint**

### **🔹 Classify a Number**
- **Endpoint:**  
  ```
  GET /api/classify-number?number=<integer>
  ```
- **Example Request:**
  ```
  GET http://127.0.0.1:8000/api/classify-number?number=371
  ```

- **Response (200 OK)**  
  ```json
  {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }
  ```

- **Response (400 Bad Request)**  
  ```json
  {
      "number": "alphabet",
      "error": true
  }
  ```

---

## **📌 Setup Instructions**

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Requests** (for fetching fun facts from the Numbers API)

---

### **2️⃣ Installation**

#### **📥 Clone the Repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

#### **🐍 Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### **📦 Install Dependencies**
```sh
pip install -r requirements.txt
```

---

### **3️⃣ Running the Application**
```sh
python manage.py runserver
```
The API will be available at:
```
http://127.0.0.1:8000/api/classify-number?number=<integer>
```


