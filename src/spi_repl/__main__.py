import argparse
import os
import sys
from typing import NoReturn
from spi_repl.spi import SPI

def die(msg: str, code: int = 1) -> NoReturn:
    print(msg, file=sys.stderr)
    exit(code)


def main() -> None:
    if os.name == 'nt':
        die("Windows is not supported")

    parser = argparse.ArgumentParser(description="SPI REPL")
    parser.add_argument("--device", type=str, default="/dev/spidev0.0", help="SPI device. Default: %(default)s")
    parser.add_argument("--speed", type=int, default=1000000, help="SPI speed. Default: %(default)s")
    parser.add_argument("--bits-per-word", type=int, default=8, help="SPI bits per word. Default: %(default)s")
    parser.add_argument("--phase", type=bool, action='store_true',default=False, help="SPI phase. Default: %(default)s")
    parser.add_argument("--polarity", type=bool, action='store_true',default=False, help="SPI polarity. Default: %(default)s")
    parser.add_argument("--cs-high", type=bool,action='store_true', default=False, help="SPI chip select active level. Default: %(default)s")
    parser.add_argument("--lsb-first", type=bool, action='store_true',default=False, help="SPI bit order. Default: %(default)s")
    parser.add_argument("--three-wire", type=bool, action='store_true',default=False, help="SPI 3-wire mode. Default: %(default)s")
    parser.add_argument("--loop", type=bool, action='store_true',default=False, help="SPI loopback mode. Default: %(default)s")
    parser.add_argument("--no-cs", type=bool, action='store_true',default=False, help="SPI no chip select. Default: %(default)s")
    parser.add_argument("--ready", type=bool, action='store_true', default=False, help="SPI slave pulls low to pause. Default: %(default)s")
    args = parser.parse_args()

    s = SPI(
        device=args.device,
        speed=args.speed,
        bits_per_word=args.bits_per_word,
        phase=args.phase,
        polarity=args.polarity,
        cs_high=args.cs_high,
        lsb_first=args.lsb_first,
        three_wire=args.three_wire,
        loop=args.loop,
        no_cs=args.no_cs,
        ready=args.ready
    )

    print(f"SPI device: {args.device} speed: {args.speed} bits_per_word: {args.bits_per_word}")
    print("now enter hex strings to send to the device")
    device = args.device
    while True:
        try:
            data = input(f"{device} <<< ")
            if data.startswith("exit"):
                die("Bye!", code=0)

            if data.startswith("0x"):
                data = data[2:]

            databytes = bytes.fromhex(data)
            resp = s.transfer(databytes)
            print(f"{device} >>> {resp.hex()}")
            continue
        except ValueError:
            print("expected hex string ('00112233445566778899aabbccddeeff')")
            continue
        except EOFError:
            die("EOF")
        except KeyboardInterrupt:
            die("CTRL+C pressed")
        except Exception as e:
            die(f"Unexpected error: {e}", code=1)


if __name__ == "__main__":
    main()
