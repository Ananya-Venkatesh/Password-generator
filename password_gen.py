# password_gen.py
from secrets import choice, SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits
import math

LOWER = set(ascii_lowercase)
UPPER = set(ascii_uppercase)
DIGIT = set(digits)
SYMBOL = set("!@#$%^&*()-_=+[]{};:,.?/")

SIMILAR_LOOKING = set("Il1O0|`'\"\\")
SYSTEM_RNG = SystemRandom()

class PolicyError(ValueError): pass

def build_pool(use_lower=True, use_upper=True, use_digits=True, use_symbols=True,
               exclude: set[str] | None = None) -> list[str]:
    pool = set()
    if use_lower:  pool |= LOWER
    if use_upper:  pool |= UPPER
    if use_digits: pool |= DIGIT
    if use_symbols: pool |= SYMBOL
    if exclude:
        pool -= set(exclude)
    pool = list(pool)
    if not pool:
        raise PolicyError("Character pool empty after exclusions.")
    return pool

def generate_password(length: int,
                      require_classes=("lower","upper","digit","symbol"),
                      exclude_similar=True,
                      exclude_chars: str = "",
                      no_repeat=False) -> str:
    if length <= 0:
        raise PolicyError("Length must be positive.")

    exclude = set(exclude_chars)
    if exclude_similar:
        exclude |= SIMILAR_LOOKING

    # Select pools & required picks
    pools = {
        "lower": list(LOWER - exclude),
        "upper": list(UPPER - exclude),
        "digit": list(DIGIT - exclude),
        "symbol": list(SYMBOL - exclude),
    }
    for k in require_classes:
        if not pools[k]:
            raise PolicyError(f"Required class '{k}' is empty after exclusions.")

    # Start by guaranteeing one from each required pool
    pwd_chars = [choice(pools[k]) for k in require_classes]

    # Build overall pool
    overall_pool = build_pool(True, True, True, True, exclude)

    # Fill the rest
    while len(pwd_chars) < length:
        c = choice(overall_pool)
        if no_repeat and pwd_chars and c == pwd_chars[-1]:
            continue
        pwd_chars.append(c)

    # Shuffle to avoid predictable positions of required chars
    SYSTEM_RNG.shuffle(pwd_chars)
    return "".join(pwd_chars)

def estimate_entropy_bits(length: int, pool_size: int) -> float:
    # Approximation assuming uniform selection with replacement.
    return length * math.log2(pool_size)

def strength_label(bits: float) -> str:
    if bits < 40: return "weak"
    if bits < 60: return "fair"
    if bits < 80: return "strong"
    return "very strong"
