#!/bin/bash
ping_sweep() {
  subnet="${1:-172.17.0}"
  for i in {1..10}; do
    ip="$subnet.$i"
    ( ping -c1 -W1 "$ip" &>/dev/null && echo "[+] $ip alive" ) &
  done
  wait
}
