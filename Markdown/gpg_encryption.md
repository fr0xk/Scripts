### Script for Sender: `encrypt_message.sh`

```sh
#!/bin/sh

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 recipient_email message"
    exit 1
fi

RECIPIENT=$1
MESSAGE=$2

# Create a temporary file for the message
TEMP_MSG_FILE=$(mktemp)
echo "$MESSAGE" > "$TEMP_MSG_FILE"

# Encrypt the message
gpg --output message.txt.gpg --encrypt --recipient "$RECIPIENT" "$TEMP_MSG_FILE"

# Check if encryption was successful
if [ $? -eq 0 ]; then
    echo "Message encrypted successfully. Output file: message.txt.gpg"
else
    echo "Failed to encrypt the message."
fi

# Clean up temporary file
rm "$TEMP_MSG_FILE"
```

### Script for Recipient: `decrypt_message.sh`

```sh
#!/bin/sh

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 encrypted_message_file"
    exit 1
fi

ENCRYPTED_FILE=$1

# Decrypt the message
gpg --output decrypted_message.txt --decrypt "$ENCRYPTED_FILE"

# Check if decryption was successful
if [ $? -eq 0 ]; then
    echo "Message decrypted successfully. Output file: decrypted_message.txt"
else
    echo "Failed to decrypt the message."
fi
```

### Usage

1. **Encrypting the Message (Sender)**:
    ```sh
    ./encrypt_message.sh recipient@example.com "This is a secret message"
    ```
    This will produce `message.txt.gpg`.

2. **Decrypting the Message (Recipient)**:
    ```sh
    ./decrypt_message.sh message.txt.gpg
    ```
    This will produce `decrypted_message.txt`.

### Notes

- Make sure to replace `recipient@example.com` with the actual recipient's email address.
- Ensure both scripts have execute permissions:
    ```sh
    chmod +x encrypt_message.sh decrypt_message.sh
    ```

These scripts adhere to POSIX-compliant syntax, ensuring broader compatibility across different Unix-like systems.
