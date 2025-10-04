# 🚀 FastAPI Starter Project

This is a simple **FastAPI** application demonstrating how to create RESTful APIs with both **GET** and **POST** methods.  
The project also uses **Pydantic** for data validation and **type hinting** to ensure cleaner and safer code.

---

## 🧠 Features

- Fast and modern API framework using **FastAPI**
- Input validation using **Pydantic**
- Two example endpoints:
  - `GET /{text}` → Returns a greeting message
  - `POST /postname` → Accepts a JSON body with `firstname` and `lastname`, and returns a formatted greeting

---

## 📁 Project Structure

```
First/
│
├── main.py               # Main FastAPI application
├── pyproject.toml        # Project dependencies and configuration
├── uv.lock               # Uv dependency lock file
├── README.md             # Project documentation
└── .venv/                # Virtual environment (ignored)
```

---

## 🧩 Requirements

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/fastapi-starter.git
cd fastapi-starter
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies using [uv](https://github.com/astral-sh/uv)
```bash
uv pip install -r pyproject.toml
```
or if using pip:
```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Server

Use **Uvicorn** to start the FastAPI app:

```bash
uvicorn main:app --reload
```

The server will run at:
```
http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### **GET /**`{text}`
Example:
```
GET /tahir
```
Response:
```json
"Hello Tahir"
```

---

### **POST /**`postname`
Example request:
```
POST /postname
Content-Type: application/json
```

Request body:
```json
{
  "firstname": "tahir",
  "lastname": "shaikh"
}
```

Response:
```json
"Hello Tahir Shaikh"
```

---

## 🧰 Tools Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [uv](https://github.com/astral-sh/uv) (for dependency management)

---

## 💡 Author

**Tahir Abbas Shaikh**  
Machine Learning & Backend Engineer  
📧 [tahirabbasshaikh555@gmail.com](mailto:tahirabbasshaikh555@gmail.com)  
🌐 [GitHub](https://github.com/Tahir-Abbas-555)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.
