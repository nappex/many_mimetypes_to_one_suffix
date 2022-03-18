import subprocess

from pathlib import Path

def get_content_type():
    OUTPUT_DIR = Path("server_content")
    SOURCE_URL = "https://nappex.github.io/many_mimetypes_to_one_suffix/"

    for filename in OUTPUT_DIR.iterdir():
        url = SOURCE_URL + filename.name
        p1 = subprocess.Popen(['curl', '-Is', url], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(
            ['grep', 'content-type'],
            text=True, stdin=p1.stdout, stdout=subprocess.PIPE
        )
        p1.stdout.close()
        out, err = p2.communicate()
        yield (filename.suffix, out.lstrip('content-type: ').rstrip())


def main():
    with open('gh_pages_responses', mode='w') as file:
        for suffix, content in get_content_type():
            print(f"{suffix:9} {content}", file=file)

    print("Work done")


if __name__ == "__main__":
    main()


