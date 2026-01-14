from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
import base64


encrypted_data = "FDGi0pewGc2RIVu2J3imYTtZnZ9amLQjAPBWyOcwxJYsHFf8c+UmXkC+xWuyySB4bDH0g9vRSAVqdRWHHb+Kfs3x74jmTWO231vi2AK1jguqLR9piYWKJQ4rzztpMcgL6ebq+AwylW4hOtwbr2kRVMYHX4JJFjirhsOoZf5paHmbBC78tcuMYZT2OMigCTsi6rXuVclFc+9C/TrdevajlVHMltIcsBcy9WKaBqtPuQ3u2tW1q1wpXXeaMHulVmXxAfwE1/OGA1wLohs8W2ONJx6WR/VMepisFKH9w6xOZMY="


base64_key = "MTIzZDZjZWRmNjI2ZHk1NDIzM2FhMXc2"
base64_iv = "d0VpcGhUbiE="

key = base64.b64decode(base64_key)
iv = base64.b64decode(base64_iv)


decoded_encrypted_data = base64.b64decode(encrypted_data)

cipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(decoded_encrypted_data), DES3.block_size)

decrypted_data.decode('utf-8') 
print(decrypted_data)
