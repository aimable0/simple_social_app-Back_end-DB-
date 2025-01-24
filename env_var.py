from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")

print(os.getenv("PASSWORD"))
# print(f"here you have the hidden password: {PASSWORD}, username: {USERNAME} and host: {HOST}")