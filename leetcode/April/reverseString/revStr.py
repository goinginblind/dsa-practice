
def reverseWords(s: str) -> str:
    return ' '.join(reversed(s.strip().split()))


def main():
    print(reverseWords('the sky is blue'))


if __name__ == '__main__':
    main()