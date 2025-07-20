#!/usr/bin/env python3
import subprocess, time, os, signal, psutil

WALLET = "scash1qssvy8a0lrueh25j2rkzuv2lmsalgaemc6szj52.Danis"
POOL = "stratum+tcp://satoshicash.cedric-crispin.com:4474"
PROXY = ["proxychains"]  # Kosongkan [] jika tanpa proxy

def start_miner():
    cmd = PROXY + ["./minerd", "-a", "randomx", "-o", POOL, "-u", WALLET, "-p", "x"]
    return subprocess.Popen(cmd)

while True:
    p = start_miner()
    try:
        while True:
            cpu = psutil.cpu_percent(interval=5)
            if cpu > 90:
                print("[!] CPU tinggi, restart miner...")
                p.terminate()
                time.sleep(5)
                break
    except Exception as e:
        print("Error:", e)
        p.terminate()
        time.sleep(5)
