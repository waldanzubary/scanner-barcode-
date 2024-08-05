# Barcode Scanner and Web Form Interaction

A Python script that scans barcodes using a webcam, interacts with a web form, and optionally saves the scanned data to a CSV file.

## Features

- Scans barcodes using a webcam.
- Automatically inputs the barcode data into a web form.
- Optionally saves the scanned barcode data to a CSV file.
- Submits the web form after scanning a barcode.

## Requirements

- Python 3.6+
- OpenCV
- pyzbar
- Selenium
- Google Chrome
- ChromeDriver

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/waldanzubary/scanner-barcode.git
    cd barcode-scanner
    ```

2. **Install the required Python packages:**
    ```bash
    pip install opencv-python pyzbar selenium
    ```

3. **Download and install Google Chrome:**
    - [Google Chrome Download](https://www.google.com/chrome/)

4. **Download ChromeDriver:**
    - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/)

    Make sure to download the version of ChromeDriver that matches your installed version of Google Chrome. Add the `chromedriver` executable to your system's PATH.

## Usage

1. **Start the local server:**
    Ensure your web application is running locally on `http://127.0.0.1:8000`.  

2. **Run the script:**
    ```bash
    python scanner.py
    ```

    To save scanned barcode data to a CSV file, run the script with the `save_to_csv` argument set to `True`:
    ```bash
    python barcode_scanner.py --save_to_csv True
    ```

## Configuration

- **Web Form URL:**
    Modify the URL in the script to match the URL of the web form you want to interact with:
    ```python
    driver.get("http://127.0.0.1:8000/sales/create")
    ```

- **Web Form Input Element ID:**
    Ensure the ID of the input element in the web form matches the ID used in the script:
    ```python
    input_element = driver.find_element(By.ID, "barcode_input")
    ```

## Troubleshooting

- **Webcam not opening:**
    Ensure your webcam is properly connected and not being used by another application.

- **ChromeDriver not found:**
    Ensure ChromeDriver is installed and added to your system's PATH.

- **Barcode data not being entered into the form:**
    Ensure the URL and input element ID in the script match those of your web form.


## Acknowledgements

- [OpenCV](https://opencv.org/)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)
- [Selenium](https://www.selenium.dev/)

---

