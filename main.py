"""Entry for make.fun's The Robot Pickup Line Championship.

Writes one pickup line, in a robot's voice, to /output/entry.txt.
"""

LINE = "My sensors say you're 98% compatible — the other 2% is just my firmware being shy."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
