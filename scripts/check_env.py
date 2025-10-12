#!/usr/bin/env python3
"""Environment validation script for the workshop."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def check_environment() -> bool:
    """Validate required environment variables and setup."""
    # Load .env file
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        print("   Run: cp .env.sample .env")
        print("   Then add your OPENAI_API_KEY")
        return False

    load_dotenv()

    # Check OPENAI_API_KEY
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY not set in .env")
        print("   Get your key from: https://platform.openai.com/api-keys")
        return False

    if api_key.strip() == "":
        print("❌ OPENAI_API_KEY is empty in .env")
        print("   Get your key from: https://platform.openai.com/api-keys")
        return False

    print("✅ Environment configured correctly")
    print(f"   OPENAI_API_KEY: {api_key[:8]}...{api_key[-4:]}")
    return True


if __name__ == "__main__":
    success = check_environment()
    sys.exit(0 if success else 1)
