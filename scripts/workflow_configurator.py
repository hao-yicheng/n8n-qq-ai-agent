"""
n8n Workflow Redactor & Configuration Tool
==========================================
Purpose:
    This script is designed to automate the process of desensitizing private data
    within n8n workflow JSON files. It performs a global string replacement based
    on a mapping table to protect privacy before committing code to version control.

Usage:
    1. To REDACT (Before Git Push):
       Place your real IDs on the left and dummy values/REDACTED tags on the right.
    2. To SETUP (After Git Clone):
       Place the dummy values on the left and your own real data on the right.
    3. Run: `python n8n_redactor.py` from the project root.
"""

import os

# =========================================================
# 1. Configuration Area (Macros)
# =========================================================
# The directory containing the workflow JSON files to process
TARGET_DIR = "n8n/workflows"

# Redaction Mapping Table (Original Value -> Dummy Value)
# ---------------------------------------------------------
# - Keywords are prefixed with 'REDACTED_' for easy searching.
# - QQ IDs are replaced with 6-digit sequences for data type safety.
# - Group IDs are replaced with unique 6, 7, and 8-digit sequences.
# ---------------------------------------------------------
SENSITIVE_MAP = {
    # Infrastructure & Tokens
    "REDACTED_BARK_TOKEN":          "your_bark_token_here",
    "REDACTED_NAPCAT_HOST":         "napcat:3000",
    "REDACTED_NAPCAT_WEBHOOK_NAME": "your_webhook_name_here",
    "REDACTED_N8N_HOST":            "n8n:5678",
    "REDACTED_DOMAIN":              "n8n.example.com",
    "REDACTED_ITAD_API_KEY":        "your_itad_api_key_here",

    # Nicknames
    "REDACTED_NICKNAME_1": "nickname_1",
    "REDACTED_NICKNAME_2": "nickname_2",
    "REDACTED_NICKNAME_3": "nickname_3",
    "REDACTED_NICKNAME_4": "nickname_4",
    "REDACTED_NICKNAME_5": "nickname_5",
    "REDACTED_NICKNAME_6": "nickname_6",
    "REDACTED_NICKNAME_7": "nickname_7",
    "REDACTED_NICKNAME_8": "nickname_8",
    "REDACTED_NICKNAME_9": "nickname_9",
    # QQ IDs (Placeholders to be replaced by the user)
    # The example is set to the same dummy ID for safety.
    "111111": "111111",  # Admin QQ
    "222222": "222222",  # Bot QQ
    # Group IDs
    "6666666666": "6666666666",  # Group 1
    "7777777777": "7777777777",  # Group 2
    "8888888888": "8888888888",  # Group 3
}


def redact_workflows():
    # Check if the target directory exists
    if not os.path.exists(TARGET_DIR):
        print(f"Error: Directory '{TARGET_DIR}' does not exist.")
        return

    # List all JSON files in the directory
    json_files = [f for f in os.listdir(TARGET_DIR) if f.endswith(".json")]

    if not json_files:
        print(f"No .json files found in {TARGET_DIR}.")
        return

    print(f"Starting redaction on {len(json_files)} files...")
    print("-" * 40)

    for filename in json_files:
        file_path = os.path.join(TARGET_DIR, filename)

        # Read the file as plain text to perform global string replacement
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        modified_content = content

        # Perform simple global string replacement for each mapping
        for sensitive_val, dummy_val in SENSITIVE_MAP.items():
            if sensitive_val in modified_content:
                modified_content = modified_content.replace(sensitive_val, dummy_val)

        # Only overwrite the file if changes were actually made
        if modified_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print(f"Success: Redacted [{filename}]")
        else:
            print(f"Skipped: No sensitive data found in [{filename}]")

    print("-" * 40)
    print("Redaction process complete.")


if __name__ == "__main__":
    redact_workflows()
