# SmartReceipt 🧾✨

**SmartReceipt** is a powerful, full-stack automated expense tracker that leverages AI to simplify financial management. Snap a photo of your receipt, and let our intelligent backend handle the rest—extracting merchant details, dates, and amounts instantly.

## 🚀 Features

- **📱 Cross-Platform Mobile App**: Built with **Flutter**, offering a smooth, responsive experience on Android and iOS.
- **🤖 AI-Powered OCR**: Automatically extracts text from receipt images using **Tesseract** and advanced image processing.
- **🔐 Secure Authentication**: Robust user management with **JWT** (JSON Web Tokens) and secure password hashing.
- **📊 Interactive Dashboard**: Visualize your spending habits with dynamic **Pie Charts** and expense lists.
- **🐳 Containerized Backend**: Fully Dockerized **FastAPI** backend with **MySQL** database for easy deployment.
- **🏗️ Clean Architecture**: modular code structure using **Riverpod** for state management and **SQLModel** for ORM.

## 🛠️ Tech Stack

### Mobile (Frontend)

- **Framework**: Flutter (Dart)
- **State Management**: Riverpod
- **Navigation**: GoRouter
- **Charts**: fl_chart
- **Networking**: Dio

### Backend (API)

- **Framework**: FastAPI (Python)
- **Database**: MySQL
- **ORM**: SQLModel
- **Authentication**: OAuth2 with Password + Bearer (JWT)
- **OCR**: Tesseract / Pytesseract

## ⚙️ Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
- [Flutter SDK](https://flutter.dev/docs/get-started/install) installed.

### 1. Start the Backend 🔙

The backend and database are containerized for zero-config setup.

```bash
cd SmartReceipt
docker compose up -d --build
```

_The API will be available at `http://localhost:8001`._

### 2. Run the Mobile App 📱

Launch the Flutter app on your preferred emulator or device.

```bash
cd mobile
flutter pub get
flutter run
```

_Note: The app is pre-configured to connect to the backend at `http://10.0.2.2:8001` (standard Android emulator localhost)._

## 📸 Screenshots

|       Login Screen       |          Dashboard           |      Scan Receipt       |
| :----------------------: | :--------------------------: | :---------------------: |
| _(Add Login Screenshot)_ | _(Add Dashboard Screenshot)_ | _(Add Scan Screenshot)_ |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
