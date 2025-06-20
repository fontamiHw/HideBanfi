import subprocess
import time

def ping(host):
    try:
        output = subprocess.run(
            ["ping", "-c", "4", host],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(output.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ping failed:\n{e.stderr}")

if __name__ == "__main__":
    while True:
        ping("1.1.1.1")
        time.sleep(30)
