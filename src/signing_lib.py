"""
Library containing functions related to the ECDSA
"""

from hashlib import sha256


def sign_message(msg: str):
    msg_hash = sha256(msg.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    sign_message("asdf")