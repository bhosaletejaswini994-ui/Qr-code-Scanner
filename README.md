The Universal QR Code Scanner is a real-time QR code scanning application developed using Python and OpenCV. It uses a webcam to detect and scan QR codes automatically.

The application can scan different types of QR codes, including website links, social media links, UPI payment links, email links, phone numbers, and SMS links.

After scanning, the QR code information is displayed on the camera screen for 10 seconds. Users can click on the displayed result to open supported links directly.
- Real-time QR code detection using a webcam.
- Automatically scans QR codes.
- Displays scanned information on the camera screen.
- Highlights detected QR codes with a green boundary.
- Displays scanned results for 10 seconds.
- Click-to-open functionality for supported links.
- Supports website and social media URLs.
- Supports UPI payment links.
- Supports email (mailto:), phone (tel:), and SMS (sms:) links.
- Displays other QR information in the terminal.
- Press Q to close the scanner.
- Python – Main programming language.
- OpenCV – QR code detection and webcam access.
- Webbrowser – Opens scanned links in the default browser.
- Time – Controls the 10-second display duration.
- Re – Python regular expression module.
```
Universal-QR-Scanner/
│
└── QRScanner.py
```
Download and install Python from:

https://www.python.org/
Open the VS Code terminal or PowerShell and run:
```
pip install opencv-python
```
Navigate to your project folder and execute:
```
python QRScanner.py
```
1. The webcam starts capturing live video.
2. OpenCV detects QR codes using QRCodeDetector().
3. When a QR code is detected, its information is extracted.
4. A green boundary is drawn around the detected QR code.
5. The scanned information appears on the camera screen for 10 seconds.
6. Click on the displayed result to open supported links.
7. Press Q to exit the application.
This project can be useful in different industries:
- Retail Stores: Scanning product information and payment QR codes.
- Banking & Payments: Reading UPI payment QR codes.
- Restaurants: Scanning digital menus.
- Education: Accessing learning materials through QR codes.
- Marketing: Opening websites and social media pages.
- Office Management: Scanning QR codes for visitor information.
Through this project, I learned:
- Real-time webcam access using OpenCV.
- QR code detection and information extraction.
- Mouse click event handling in OpenCV.
- Opening URLs using Python's Webbrowser module.
- Working with conditional statements and time-based events.
Tejaswini Bhosale
The Universal QR Code Scanner demonstrates how Python and OpenCV can be used to develop a practical real-time computer vision application. It makes scanning and accessing different types of QR code information simple and convenient.
