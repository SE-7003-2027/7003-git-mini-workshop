import hashlib
asda
def generate_anonymous_id():
    print("--- Git Lab Privacy ID Generator ---")
    full_name = input("Enter your full legal name: ").strip().lower()
    student_id = input("Enter your University ID: ").strip()

    # Standardize string formatting to prevent hash mismatches
    raw_identifier = f"{full_name}:{student_id}".encode('utf-8')
    hashed_id = hashlib.sha256(raw_identifier).hexdigest()

    print("\n---------------------------------------------------")
    print(f"Your Anonymous Hash ID is:\n{hashed_id}")
    print(f"\nInstructions: Create your submission file at:")
    print(f"profiles/{hashed_id[:12]}.json")
    print("---------------------------------------------------")

if __name__ == "__main__":
    generate_anonymous_id()
sdfsf
7bb82961ead18ac0ffefe3fd8d0ce2da6651aac8
asdsadasdad
