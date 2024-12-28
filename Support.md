# Support

## Security Disclaimer
The sensitive information (e.g., usernames and passwords) in this project is for demonstration purposes only. It is included to showcase how the project functions. 

For production environments, please follow these best practices:
1. Store sensitive information using environment variables.
2. Ensure that `.env` files or other configuration files are not committed to version control (e.g., by adding them to `.gitignore`).
3. Regularly update passwords and use strong passwords.

### Configuring Environment Variables
You can store sensitive information in a `.env` file and then use Python’s `os.getenv` method to retrieve it. For example:
```python
import os

DB_PASSWORD = os.getenv("DB_PASSWORD")