# Smart QR-Based Attendance System

🚀 **Revolutionizing Event Attendance and Activity Tracking**  

This smart QR-based attendance system was specially developed for the **International Olympiad on Astronomy and Astrophysics - Junior (IOAA-Jr.) 2024**, marking a historic event in South Asia. It seamlessly handled the entire event's attendance and activity tracking, ensuring a smooth and efficient experience for participants and organizers alike.

---

## 🌟 Key Features
- **Smart QR Code Authentication**: Unique QR codes for reliable and quick attendance logging. 
- **Real-Time Activity Tracking**: Monitors participant activities throughout the event.
- **Role-Based Access Control**: Secure login with separate functionalities for Superusers and Country Guides.
- **Data Storage and Management**: Efficient data management using SQLite.
- **User-Friendly Dashboard**: Admin dashboard for viewing and exporting attendance reports.

---

## ⚙️ Tech Stack
- **Backend**: Django
- **Database**: SQLite
- **Deployment**: [PythonAnywhere](https://www.pythonanywhere.com/)
- **Languages**: Python, HTML, CSS

---

## 🚀 Deployment
The system is deployed on PythonAnywhere, ensuring stability and scalability. 

> **Link to Live Site:** [Visit Here](https://suwarna.pythonanywhere.com/)

---

## 🔍 How It Works
1. **QR Code Generation**: Unique QR codes are generated for participants.
2. **Attendance Scanning**: Country guides scan the QR codes using the web interface.
3. **Real-Time Logging**: Attendance data is stored securely in an SQLite database.
4. **Admin Dashboard**: Superusers can view and export attendance reports for analysis.

---

## 🛠️ Installation Guide
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/suwarna-wave/qrauth.git
    cd qrauth
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Run the server:**
    ```bash
    python manage.py runserver
    ```
6. **Access the site locally at:** `http://127.0.0.1:8000`

---

## 🤝 Contribution & Support
Feel free to contribute to this project by creating pull requests or raising issues. For any queries, reach out to [Suwarna](mailto:bhattarai.suresh@gmail.com).

---

## 🙏 Acknowledgments
This system played a crucial role in the success of **IOAA-Jr. 2024**, thanks to the dedication and hard work of the organizing committee. Special appreciation goes to the entire team and participants who made the event memorable.

---

## 📄 License
This project is licensed under the MIT License. Feel free to use and contribute!

---

## 🌐 Connect
[GitHub](https://github.com/suwarna-wave) | [LinkedIn](https://www.linkedin.com/in/suwarnapyakurel)

---

> Developed with ❤️ by Suwarna for IOAA-Jr. 2024
