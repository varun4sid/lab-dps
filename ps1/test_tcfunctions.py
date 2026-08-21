import unittest

from tcfunctions import (
    double_transposition_decrypt,
    double_transposition_encrypt,
    get_encryption_key,
    transposition_decrypt,
    transposition_encrypt,
)


class TranspositionCipherTests(unittest.TestCase):
    def test_encrypt_uses_key_order(self):
        key = get_encryption_key("ZEBRAS")

        self.assertEqual(
            transposition_encrypt("HELLOWORLD", key),
            "W_LLERLDHOO_",
        )

    def test_decrypt_reconstructs_unpadded_plaintext(self):
        key = get_encryption_key("ZEBRAS")

        self.assertEqual(
            transposition_decrypt("W_LLERLDHOO_", key),
            "HELLOWORLD",
        )

    def test_encrypt_and_decrypt_round_trip_with_padding(self):
        plaintext = "HELLO"
        key = get_encryption_key("ZEBRAS")
        ciphertext = transposition_encrypt(plaintext, key)

        self.assertEqual(transposition_decrypt(ciphertext, key), plaintext)

    def test_decrypt_can_preserve_padding(self):
        key = get_encryption_key("ZEBRAS")
        ciphertext = transposition_encrypt("HELLO", key)

        self.assertEqual(
            transposition_decrypt(ciphertext, key, strip_padding=False),
            "HELLO_",
        )

    def test_double_transposition_round_trip_known_case(self):
        key1 = get_encryption_key("ZEBRAS")
        key2 = get_encryption_key("MATRIX")
        plaintext = "PYTHON"

        ciphertext = double_transposition_encrypt(plaintext, key1, key2)

        self.assertEqual(ciphertext, "YNPHTO")
        self.assertEqual(double_transposition_decrypt(ciphertext, key1, key2), plaintext)

    def test_double_transposition_round_trip_with_intermediate_padding(self):
        key1 = get_encryption_key("nick")
        key2 = get_encryption_key("boat")
        plaintext = "HELLO"

        ciphertext = double_transposition_encrypt(plaintext, key1, key2)

        self.assertEqual(
            double_transposition_decrypt(ciphertext, key1, key2),
            plaintext,
        )

    def test_encrypt_rejects_empty_input(self):
        key = get_encryption_key("ZEBRAS")

        self.assertEqual(
            transposition_encrypt("", key),
            "Invalid input: key and plaintext cannot be empty",
        )

    def test_decrypt_rejects_empty_input(self):
        key = get_encryption_key("ZEBRAS")

        self.assertEqual(
            transposition_decrypt("", key),
            "Invalid input: key and ciphertext cannot be empty",
        )


if __name__ == "__main__":
    unittest.main()
