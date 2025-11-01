# 🛡️ Secure Python Password Generator

A simple, command-line Python script for generating cryptographically strong, customizable passwords. This tool uses Python's `secrets` module to ensure high-quality, unpredictable randomness, suitable for all security applications.

---

## 🚀 Features

* **Cryptographically Strong:** Uses the `secrets` module instead of `random` for generating secure random numbers.
* **Guaranteed Characters:** Ensures that at least one of each selected character type (lowercase, uppercase, digit, special character) is included in the final password.
* **Customizable:** Allows you to specify the exact length and character types you want.
* **Input Validation:** Includes robust error handling for invalid length or no character types selected.
* **Secure Mixing:** The final password characters are shuffled to ensure guaranteed characters don't always appear at the beginning.

---

## 💻 Usage

To run this script, you will need Python 3 installed.

1.  **Clone the repository (or download the script):**
    ```sh
    git clone [https://github.com/YOUR-USERNAME/Secure-Password-Generator.git](https://github.com/YOUR-USERNAME/Secure-Password-Generator.git)
    cd Secure-Password-Generator
    ```

2.  **Run the script from your terminal:**
    ```sh
    python password_generator.py
    ```

3.  **Follow the prompts:**
    The script will ask you for your preferences, and then it will output the final password.

    ```
    --- Secure Password Generator ---
    Enter the desired password length (min 8): 16
    Include lowercase letters? (yes/no): yes
    Include uppercase letters? (yes/no): yes
    Include digits? (yes/no): yes
    Include special characters? (yes/no): yes
    
    Generated Password: 8K!p&w3jG$@T_vR5
    ```

---

## 🛠️ Code Explanation

This script is built around two key principles: security and robustness.

### 1. Security (`secrets` module)

The core of this script is the `secrets` module.

* `secrets.choice(list)` is used to pick characters. This is essential because the `random` module is a "pseudo-random" number generator, which is predictable and unsuitable for security. The `secrets` module uses the operating system's most secure source of randomness.

### 2. Robustness (Guaranteed Characters)

A simple `random.choice()` from a combined pool for the full length does *not* guarantee all character sets will be included. This script solves that:

1.  **Guarantee:** It first adds *one* securely chosen character from each *required* set to a list.
2.  **Fill:** It then fills the *remaining* length of the password by choosing from the *total pool* of all allowed characters.
3.  **Shuffle:** Finally, it uses `random.shuffle()` to mix the entire list of characters. This ensures the guaranteed characters (e.g., the one special character) don't always appear at the start of the password.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
