# Password Encryption & Decryption App

This Python application allows users to encrypt and decrypt messages securely using a simple GUI built with Tkinter and CustomTkinter. The app uses a username-based mechanism to ensure only authorized users can decrypt the message.

## Features

- **Encrypt Message**: Input a message, and after entering the correct username, it will generate an encrypted string.
- **Decrypt Message**: Paste an encrypted string and provide the correct username to retrieve the original message.
- **Simple GUI**: A user-friendly interface with Tkinter and CustomTkinter.

## How It Works

1. **Encryption Process**:
   - Enter the message in the input field.
   - Click the **Encrypt** button.
   - A pop-up window will prompt you for your username.
   - Once you provide a username, the app generates and displays the encrypted message.

2. **Decryption Process**:
   - Open the **Decrypt** menu and paste the encrypted message.
   - Click the **Decrypt** button.
   - A pop-up window will ask for the username.
   - Provide the correct username to successfully decrypt and view the original message.

## Prerequisites

- Python 3.x
- Tkinter
- CustomTkinter

You can install the dependencies using:

```bash 
pip install tk
pip install customtkinter 
```

## Installation

1. Clone this repository:

   ```bash
   git clone git@github.com:Shana2002/encrypt-decrypter.git

1. Navigate to the project directory:

   ```bash
   cd password-encryption-app

3. Run the app
   ```bash
   python encryption.py

## Usage

1. Run the app.
2. To encrypt a message, enter the message and provide a username.
3. To decrypt a message, paste the encrypted string and provide the username.

## Future Improvements

- Add support for stronger encryption algorithms.
- Implement password management features.
