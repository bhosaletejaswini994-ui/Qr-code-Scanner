
# import cv2

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     data, points, _ = detector.detectAndDecode(frame)

#     if data:
#         print("QR Code Detected:", data)

#     cv2.imshow("QR Code Scanner", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import webbrowser

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# last_data = ""

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     data, points, _ = detector.detectAndDecode(frame)

#     if data and data != last_data:
#         print("QR Code Detected:", data)
#         last_data = data

#         if data.startswith(("http://", "https://")):
#             webbrowser.open(data)

#     cv2.imshow("QR Code Scanner", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import customtkinter as ctk
# import webbrowser
# from PIL import Image
# from tkinter import messagebox

# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# window = ctk.CTk()
# window.title("QR Code Scanner")
# window.geometry("900x650")

# cap = None
# scanning = False
# last_data = ""

# # Camera preview
# camera_label = ctk.CTkLabel(
#     window,
#     text="Camera preview will appear here",
#     width=600,
#     height=350
# )
# camera_label.pack(pady=20)

# # Result label
# result_label = ctk.CTkLabel(
#     window,
#     text="Scan a QR code to see the result",
#     font=("Arial", 15),
#     wraplength=800
# )
# result_label.pack(pady=10)

# # Open scanned link
# def open_result():
#     data = result_label.cget("text")

#     if data.startswith(("http://", "https://", "upi://")):
#         try:
#             webbrowser.open(data)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#     else:
#         messagebox.showinfo(
#             "Information",
#             "This QR code does not contain a supported link."
#         )

# # Camera scanning
# def scan_qr():
#     global cap, scanning, last_data

#     if not scanning:
#         return

#     ret, frame = cap.read()

#     if ret:
#         detector = cv2.QRCodeDetector()
#         data, points, _ = detector.detectAndDecode(frame)

#         if data and data != last_data:
#             last_data = data
#             result_label.configure(text=data)
#             open_button.configure(state="normal")

#             print("QR Code:", data)

#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(frame)
#         image = image.resize((600, 350))

#         photo = ctk.CTkImage(
#             light_image=image,
#             dark_image=image,
#             size=(600, 350)
#         )

#         camera_label.configure(image=photo, text="")
#         camera_label.image = photo

#     window.after(15, scan_qr)

# # Start camera
# def start_scanning():
#     global cap, scanning, last_data

#     if scanning:
#         return

#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         messagebox.showerror("Camera Error", "Unable to open camera.")
#         cap.release()
#         cap = None
#         return

#     scanning = True
#     last_data = ""

#     result_label.configure(text="Looking for QR code...")
#     open_button.configure(state="disabled")

#     scan_qr()

# # Stop camera
# def stop_scanning():
#     global cap, scanning

#     scanning = False

#     if cap is not None:
#         cap.release()
#         cap = None

#     camera_label.configure(
#         image=None,
#         text="Camera stopped"
#     )

# # Buttons
# button_frame = ctk.CTkFrame(window, fg_color="transparent")
# button_frame.pack(pady=20)

# start_button = ctk.CTkButton(
#     button_frame,
#     text="Start Scan",
#     width=150,
#     command=start_scanning
# )
# start_button.pack(side="left", padx=10)

# stop_button = ctk.CTkButton(
#     button_frame,
#     text="Stop Scan",
#     width=150,
#     command=stop_scanning
# )
# stop_button.pack(side="left", padx=10)

# open_button = ctk.CTkButton(
#     button_frame,
#     text="Open Link",
#     width=150,
#     command=open_result,
#     state="disabled"
# )
# open_button.pack(side="left", padx=10)

# def close_app():
#     stop_scanning()
#     window.destroy()

# window.protocol("WM_DELETE_WINDOW", close_app)

# window.mainloop()


# import cv2
# import customtkinter as ctk
# import webbrowser
# from PIL import Image
# from tkinter import messagebox

# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# window = ctk.CTk()
# window.title("QR Code Scanner")
# window.geometry("900x650")

# cap = None
# scanning = False
# scanned_link = ""

# # Heading
# title = ctk.CTkLabel(
#     window,
#     text="QR Code Scanner",
#     font=("Arial", 26, "bold")
# )
# title.pack(pady=15)

# # Camera preview
# camera_label = ctk.CTkLabel(
#     window,
#     text="Click Start Scan",
#     width=700,
#     height=400
# )
# camera_label.pack(pady=10)

# # Clickable link
# link_label = ctk.CTkLabel(
#     window,
#     text="Your scanned link will appear here",
#     font=("Arial", 16, "underline"),
#     text_color="blue",
#     cursor="hand2"
# )
# link_label.pack(pady=15)

# # Open link
# def open_link(event=None):
#     if scanned_link.startswith(("http://", "https://")):
#         webbrowser.open(scanned_link)
#     elif scanned_link.startswith("upi://"):
#         webbrowser.open(scanned_link)
#     else:
#         messagebox.showinfo(
#             "QR Result",
#             scanned_link
#         )

# link_label.bind("<Button-1>", open_link)

# # Scan camera
# def scan_camera():
#     global cap, scanning, scanned_link

#     if not scanning:
#         return

#     ret, frame = cap.read()

#     if ret:
#         detector = cv2.QRCodeDetector()
#         data, points, _ = detector.detectAndDecode(frame)

#         if data:
#             if data != scanned_link:
#                 scanned_link = data
#                 link_label.configure(text=data)

#             # Draw QR detection box
#             if points is not None:
#                 points = points.astype(int)

#                 for i in range(4):
#                     p1 = tuple(points[0][i])
#                     p2 = tuple(points[0][(i + 1) % 4])

#                     cv2.line(
#                         frame, p1, p2,
#                         (0, 255, 0), 3
#                     )

#         else:
#             if not scanned_link:
#                 link_label.configure(
#                     text="Looking for QR code..."
#                 )

#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(frame)
#         image = image.resize((700, 400))

#         photo = ctk.CTkImage(
#             light_image=image,
#             dark_image=image,
#             size=(700, 400)
#         )

#         camera_label.configure(image=photo, text="")
#         camera_label.image = photo

#     window.after(15, scan_camera)

# # Start scanning
# def start_scan():
#     global cap, scanning, scanned_link

#     if scanning:
#         return

#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         messagebox.showerror(
#             "Camera Error",
#             "Unable to open camera"
#         )
#         cap.release()
#         cap = None
#         return

#     scanning = True
#     scanned_link = ""

#     link_label.configure(
#         text="Looking for QR code..."
#     )

#     scan_camera()

# # Stop scanning
# def stop_scan():
#     global cap, scanning

#     scanning = False

#     if cap is not None:
#         cap.release()
#         cap = None

#     camera_label.configure(
#         image=None,
#         text="Camera stopped"
#     )

# # Buttons
# button_frame = ctk.CTkFrame(
#     window,
#     fg_color="transparent"
# )
# button_frame.pack(pady=15)

# start_button = ctk.CTkButton(
#     button_frame,
#     text="Start Scan",
#     command=start_scan,
#     width=150
# )
# start_button.pack(side="left", padx=10)

# stop_button = ctk.CTkButton(
#     button_frame,
#     text="Stop Scan",
#     command=stop_scan,
#     width=150
# )
# stop_button.pack(side="left", padx=10)

# def close_app():
#     stop_scan()
#     window.destroy()

# window.protocol("WM_DELETE_WINDOW", close_app)

# window.mainloop()




# import cv2
# import webbrowser

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# scanned_link = ""
# last_opened = ""

# def mouse_click(event, x, y, flags, param):
#     global scanned_link

#     if event == cv2.EVENT_LBUTTONDOWN:
#         if scanned_link.startswith(("http://", "https://")):
#             webbrowser.open(scanned_link)

#         elif scanned_link.startswith("upi://"):
#             webbrowser.open(scanned_link)


# cv2.namedWindow("QR Code Scanner")
# cv2.setMouseCallback("QR Code Scanner", mouse_click)

# while True:

#     ret, frame = cap.read()

#     if not ret:
#         break

#     data, points, _ = detector.detectAndDecode(frame)

#     if data:
#         if data != scanned_link:
#             scanned_link = data

#     if points is not None and len(points) > 0:

#         points = points.astype(int)

#         for i in range(4):
#             p1 = tuple(points[0][i])
#             p2 = tuple(points[0][(i + 1) % 4])

#             cv2.line(
#                 frame, p1, p2,
#                 (0, 255, 0), 3
#             )

#     # Keep the scanned link displayed
#     if scanned_link:

#         display_link = scanned_link[:65]

#         cv2.rectangle(
#             frame,
#             (10, 10),
#             (850, 55),
#             (0, 100, 0),
#             -1
#         )

#         cv2.putText(
#             frame,
#             display_link,
#             (20, 40),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.6,
#             (255, 255, 255),
#             2
#         )

#     cv2.imshow("QR Code Scanner", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import webbrowser
# import time

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# scanned_link = ""
# hold_until = 0

# def mouse_click(event, x, y, flags, param):
#     global scanned_link

#     # Click on the displayed link
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if 10 <= x <= 850 and 10 <= y <= 65:
#             if scanned_link.startswith(("http://", "https://")):
#                 webbrowser.open(scanned_link)

#             elif scanned_link.startswith("upi://"):
#                 webbrowser.open(scanned_link)


# cv2.namedWindow("AI QR Scanner")
# cv2.setMouseCallback("AI QR Scanner", mouse_click)

# while True:

#     ret, frame = cap.read()

#     if not ret:
#         break

#     data, points, _ = detector.detectAndDecode(frame)

#     # Detect new QR code
#     if data:
#         scanned_link = data
#         hold_until = time.time() + 10

#     # Draw green box
#     if points is not None and len(points) > 0:
#         points = points.astype(int)

#         for i in range(4):
#             p1 = tuple(points[0][i])
#             p2 = tuple(points[0][(i + 1) % 4])

#             cv2.line(frame, p1, p2, (0, 255, 0), 3)

#     # Hold link for 10 seconds
#     if scanned_link and time.time() < hold_until:

#         display_link = scanned_link

#         if len(display_link) > 65:
#             display_link = display_link[:62] + "..."

#         cv2.rectangle(
#             frame,
#             (10, 10),
#             (850, 65),
#             (0, 100, 0),
#             -1
#         )

#         cv2.putText(
#             frame,
#             display_link,
#             (20, 35),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.6,
#             (255, 255, 255),
#             2
#         )

#         cv2.putText(
#             frame,
#             "CLICK HERE TO OPEN",
#             (20, 55),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.4,
#             (255, 255, 255),
#             1
#         )

#     else:
#         scanned_link = ""

#     cv2.imshow("AI QR Scanner", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import webbrowser
import time
import re

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

scanned_data = ""
hold_until = 0
last_scan = ""

def open_link(event, x, y, flags, param):
    global scanned_data

    if event == cv2.EVENT_LBUTTONDOWN:

        if 10 <= x <= 900 and 10 <= y <= 90:

            data = scanned_data

            # Website and social media links
            if data.startswith(("http://", "https://")):
                webbrowser.open(data)

            # UPI payment links
            elif data.startswith("upi://"):
                webbrowser.open(data)

            # Other supported application links
            elif data.startswith(("mailto:", "tel:", "sms:")):
                webbrowser.open(data)

            else:
                print("QR Information:", data)


cv2.namedWindow("Universal QR Scanner")
cv2.setMouseCallback("Universal QR Scanner", open_link)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    data, points, _ = detector.detectAndDecode(frame)

    # Detect a new QR code
    if data and data != last_scan:
        scanned_data = data
        last_scan = data
        hold_until = time.time() + 10

        print("Scanned:", data)

    # Draw QR detection box
    if points is not None and len(points) > 0:

        points = points.astype(int)

        for i in range(4):
            p1 = tuple(points[0][i])
            p2 = tuple(points[0][(i + 1) % 4])

            cv2.line(
                frame, p1, p2,
                (0, 255, 0), 3
            )

    # Display result for 10 seconds
    if scanned_data and time.time() < hold_until:

        display_data = scanned_data

        if len(display_data) > 75:
            display_data = display_data[:72] + "..."

        cv2.rectangle(
            frame,
            (10, 10),
            (900, 90),
            (0, 100, 0),
            -1
        )

        cv2.putText(
            frame,
            display_data,
            (20, 43),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "CLICK HERE TO OPEN",
            (20, 73),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

    elif time.time() >= hold_until:
        scanned_data = ""
        last_scan = ""

    cv2.imshow("Universal QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



