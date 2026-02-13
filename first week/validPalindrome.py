
def isPalindrome(s: str) -> bool:
    cleaned = ""
    for char in s:
        if not char.isalnum():
            continue
        cleaned += char.lower()

    L = 0
    R = len(cleaned) - 1
    while L < R:
        if cleaned[L] != cleaned[R]:
            return False
        L += 1
        R -= 1
    return True

def main():
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    
    s = "race a car"
    print(isPalindrome(s))

    s = " "
    print(isPalindrome(s))

if __name__ == "__main__":
    main()
        