# spi-repl

Pure python SPI REPL (Read-Evaluate-Print-Loop) which allows you to interact with SPI devices from the command line.

- 0 dependencies, only python.
- Python 3.7+.
- Windows is not supported.

## Installation

```
pip install spi-repl
```


## Example:


```bash
$ spi-repl --help
usage: spi-repl [-h] [--device DEVICE] [--speed SPEED] [--bits-per-word BITS_PER_WORD] [--phase] [--polarity] [--cs-high] [--lsb-first] [--three-wire] [--loop] [--no-cs] [--ready]

SPI REPL

options:
  -h, --help            show this help message and exit
  --device DEVICE       SPI device. Default: /dev/spidev0.0
  --speed SPEED         SPI speed. Default: 1000000
  --bits-per-word BITS_PER_WORD
                        SPI bits per word. Default: 8
  --phase               SPI phase. Default: False
  --polarity            SPI polarity. Default: False
  --cs-high             SPI chip select active level. Default: False
  --lsb-first           SPI bit order. Default: False
  --three-wire          SPI 3-wire mode. Default: False
  --loop                SPI loopback mode. Default: False
  --no-cs               SPI no chip select. Default: False
  --ready               SPI slave pulls low to pause. Default: False

$ spi-repl --speed 5000000
SPI device: /dev/spidev0.0 speed: 5000000 bits_per_word: 8
now enter hex strings to send to the device
/dev/spidev0.0 <<< 0100
/dev/spidev0.0 >>> 0008
/dev/spidev0.0 <<< 010000000000000000000000000
expected hex string ('00112233445566778899aabbccddeeff')
```
