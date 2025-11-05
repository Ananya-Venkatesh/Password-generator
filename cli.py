# cli.py
import argparse
from string import ascii_lowercase, ascii_uppercase, digits
from password_gen import generate_password, estimate_entropy_bits, strength_label, build_pool

def main():
    ap = argparse.ArgumentParser(description="Secure password generator")
    ap.add_argument("-l","--length", type=int, default=16)
    ap.add_argument("--no-lower", action="store_true")
    ap.add_argument("--no-upper", action="store_true")
    ap.add_argument("--no-digits", action="store_true")
    ap.add_argument("--no-symbols", action="store_true")
    ap.add_argument("--exclude-similar", action="store_true", default=True)
    ap.add_argument("--allow-similar", action="store_true", help="override exclude-similar")
    ap.add_argument("--exclude", default="", help="characters to exclude")
    ap.add_argument("--no-repeat", action="store_true")
    args = ap.parse_args()

    exclude_similar = not args.allow_similar and args.exclude_similar

    req = []
    if not args.no_lower:  req.append("lower")
    if not args.no_upper:  req.append("upper")
    if not args.no_digits: req.append("digit")
    if not args.no_symbols:req.append("symbol")

    pwd = generate_password(
        length=args.length,
        require_classes=tuple(req) if req else (),
        exclude_similar=exclude_similar,
        exclude_chars=args.exclude,
        no_repeat=args.no_repeat,
    )
    pool = build_pool(
        not args.no_lower, not args.no_upper, not args.no_digits, not args.no_symbols,
        set(args.exclude) | (set() if not exclude_similar else set("Il1O0|`'\"\\"))
    )
    bits = estimate_entropy_bits(args.length, len(pool))
    print(pwd)
    print(f"~{bits:.1f} bits ({strength_label(bits)}) from pool size {len(pool)}.")

if _name_ == "_main_":
    main()
