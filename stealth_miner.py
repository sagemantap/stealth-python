#!/usr/bin/env python3
import subprocess, time, os, signal, random

WALLET = "scash1qssvy8a0lrueh25j2rkzuv2lmsalgaemc6szj52.Danis"
POOL = "stratum+tcp://satoshicash.cedric-crispin.com:4474"
PROXY = ["./proxychains4"]  # Non-root proxychains dummy path

def start_miner():
    cmd = PROXY + ["./minerd", "-a", "randomx", "-o", POOL, "-u", WALLET, "-p", "x"]
    return subprocess.Popen(cmd)

while True:
    print("[*] Menjalankan miner...")
    miner = start_miner()

    try:
        while True:
            time.sleep(random.randint(300, 600))  # 5-10 menit
            print("[*] Restart miner untuk penyamaran...")
            miner.terminate()
            miner.wait()
            break
    except Exception as e:
        print("Error:", e)
        miner.terminate()
        miner.wait()
        time.sleep(10)
