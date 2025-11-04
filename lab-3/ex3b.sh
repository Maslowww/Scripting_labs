#!/bin/bash
check_ips() {
  infile="$1"
  : > alive_hosts.txt
  if [ -z "$infile" ] || [ ! -f "$infile" ]; then
    echo "Usage: check_ips <file-with-text-or-ips>"
    return 1
  fi
  # take out unique ipv4
  mapfile -t ips < <(grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' "$infile" | sort -u)
  for ip in "${ips[@]}"; do
    ( ping -c1 -W1 "$ip" &>/dev/null && echo "$ip" >> alive_hosts.txt ) &
  done
  wait
  echo "Saved alive hosts to alive_hosts.txt"
}
