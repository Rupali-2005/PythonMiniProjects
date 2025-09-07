import re

def to_snake_case(s):
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)   # camelCase → snake_case
    s = s.replace("-", "_")                          # kebab-case → snake_case
    return s.lower()

def to_camel_case(s):
    parts = to_snake_case(s).split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def to_pascal_case(s):
    parts = to_snake_case(s).split('_')
    return ''.join(word.capitalize() for word in parts)

def to_kebab_case(s):
    return to_snake_case(s).replace("_", "-")


def main():
    text = input("Enter a string: ").strip()
    
    print("\nChoose conversion:")
    print("1. snake_case")
    print("2. camelCase")
    print("3. PascalCase")
    print("4. kebab-case")

    choice = input("Enter choice (1-4): ").strip()

    if choice == '1':
        print("snake_case:", to_snake_case(text))
    elif choice == '2':
        print("camelCase:", to_camel_case(text))
    elif choice == '3':
        print("PascalCase:", to_pascal_case(text))
    elif choice == '4':
        print("kebab-case:", to_kebab_case(text))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
