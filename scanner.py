import cv2
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyzbar.pyzbar import decode
from playsound import playsound  # Make sure to install playsound using `pip install playsound`

def scan_barcode(save_to_csv=False):
    """Scans barcodes from the webcam, interacts with a web form, and optionally saves data to CSV.

    Args:
        save_to_csv (bool, optional): If True, scanned barcode data will be saved to a CSV file. Defaults to False.
    """

    try:
        # Initialize Selenium driver
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/sales/creates")

        # Initialize webcam capture
        cap = cv2.VideoCapture(0)  # Try changing the index if needed

        if not cap.isOpened():
            print("Gagal membuka kamera. Pastikan DroidCam aktif dan terhubung dengan benar.")
            return

        last_save_time = None
        csv_file = None
        csv_writer = None

        if save_to_csv:
            csv_file = open('scanned_barcodes.csv', 'w', newline='')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Timestamp', 'Barcode'])

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Gagal membaca frame dari kamera.")
                break

            # Display the frame in a window
            cv2.imshow('Webcam Feed', frame)

            # Decode barcodes from the frame
            barcodes = decode(frame)

            if barcodes:
                for barcode in barcodes:
                    barcode_data = barcode.data.decode("utf-8")

                    # Check timestamp for saving to CSV
                    current_time = time.time()
                    if last_save_time is None or (current_time - last_save_time > 3):
                        # Update last save time
                        last_save_time = current_time

                        # Interact with the web form
                        input_element = driver.find_element(By.ID, "barcode_input")
                        input_element.clear()
                        input_element.send_keys(barcode_data)

                        if save_to_csv:
                            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                            csv_writer.writerow([timestamp, barcode_data])

                        print(f"Barcode {barcode_data} berhasil dipindai.")
                        
                        # Play beep sound
                        playsound('Beep.mp3')  # Adjust the file path as needed

                        # Submit the form by pressing Enter
                        input_element.send_keys(Keys.ENTER)
                        print("Form telah disubmit dengan menekan Enter.")

                    else:
                        print(f"Barcode {barcode_data} sudah dipindai dalam 3 detik terakhir, tidak disimpan.")

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Add a short delay to reduce CPU usage
            # time.sleep(0.1)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    finally:
        # Clean up resources
        if csv_file:
            csv_file.close()
        cap.release()
        cv2.destroyAllWindows()
        driver.quit()

if __name__ == "__main__":
    scan_barcode(save_to_csv=False)  # Change to True if saving to CSV
