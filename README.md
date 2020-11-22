# remotecat

remotecat is a simple wrapper for hashcat that loads rockyou.txt into memory from a remote source*, allowing anyone to crack a hash against it without needing to download the file onto disk! It's recommended that you have a high-speed internet connection, as rockyou.txt will need to be downloaded into memory each time the script is run (totaling ~134MB on each run).

## :wrench: Usage:

Usage for remotecat is identical to hashcat, minus the need to specify a wordlist.

```
./remotecat.py -m <mode> <hashfile.txt>
```




###### * rockyou source: https://github.com/skrmsh/rockyou-unzipped
