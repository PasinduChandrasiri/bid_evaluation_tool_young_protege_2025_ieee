# Automated Bid Evaluation and Quoting System — Sri Lanka

Welcome to the **Automated Bid Evaluation and Quoting System**, an end-to-end modern web application tailored to revolutionize construction procurement processes in Sri Lanka. This project streamlines and digitizes the traditionally manual tendering workflow — from bid submission to evaluation, committee review, and finally contract award — all in one secure, transparent platform.

---

## 🚀 Project Overview

Construction tendering involves complex, time-consuming steps that require accuracy, fairness, and compliance with regulations. This system automates key bid evaluation phases:

- **Preliminary Checks:** Automatic eligibility and document completeness validation
- **Detailed Evaluation:** Price and compliance scoring for submitted bids
- **Post Qualification:** Verification of bidder credentials and capacity
- **Committee Review:** Digital dashboard for multiple committee members to review and approve bids
- **Letter of Acceptance (PDF):** Instant generation and downloadable official contract award letter

Designed to integrate easily with Sri Lankan procurement standards, it accelerates decision-making and reduces human errors while improving transparency and auditability.

---

## 🧩 Features

- User authentication and role-based access (client, committee, admin)
- Secure bid document uploads with Firebase Cloud Storage
- Automated rule-based bid evaluation logic
- Live committee voting and decision tracking
- Dynamic dashboards for clients and committee members
- PDF generation of formal Letters of Acceptance
- Modular, scalable backend built with FastAPI (Python)
- Responsive ReactJS frontend powered by Vite

---

## 🛠 Tech Stack

| Layer          | Technology                         |
| -------------- | ---------------------------------|
| Frontend       | ReactJS, Vite, Firebase SDK       |
| Backend        | Python, FastAPI, SQLAlchemy       |
| Database       | MySQL (XAMPP, phpMyAdmin)         |
| Cloud Storage  | Firebase Cloud Storage             |
| Authentication | JWT Tokens with OAuth2 flow       |
| PDF Generation | ReportLab (Python)                 |

---

## 🗄 Database

- Use MySQL via XAMPP.
- Create the database and tables using the provided SQL scripts or phpMyAdmin interface.
- Use the supplied sample users for login and testing.

---

## 🔐 Authentication

- Uses JWT tokens.
- Roles: `client`, `committee`, `admin`.
- Role-based access to features and UI.

---

## ☁️ Firebase Integration

- Frontend uses Firebase Web SDK for file uploads.
- Backend uses Firebase Admin SDK with service account JSON for secure file storage handling.
- Enables robust, scalable, and secure bid document management.

---

## 🧪 Testing & Development Tips

- Add test users via SQL insert commands.
- Use Postman or similar to test backend APIs independently.
- Check Firebase Storage after bid uploads for correct file placement.
- Monitor logs during development for debugging bid evaluation logic.

---

## 📄 PDF Letter of Acceptance

- Automatically generated on bid selection.
- Downloadable by committee members.
- Formatted cleanly with customizable contract info.

---

## 🎯 Future Enhancements

- AI-powered document analysis & compliance checks.
- Bidder-side portal for bid submissions & status tracking.
- Notification system for deadlines and approvals.
- Advanced analytics dashboard for procurement trends.

---

## ✨ Contribution

Eager to improve or customize?  
Fork this repository, submit issues or pull requests, and collaborate to build smarter procurement solutions.

---

## 👤 Author

Built and maintained by a Pasindu Chandrasiri [LinkedIn](www.linkedin.com/in/pasinduchandrasiri)

---

*Empowering fair tendering — one bid at a time.*
