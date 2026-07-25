import alchemy.grimoire


def main() -> None:
    """Record a light spell; light magic avoids circular imports."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell = alchemy.grimoire.light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )
    print(f"Testing record light spell: {spell}")


if __name__ == "__main__":
    main()
