import sys


def print_lines(lines):
    for line in lines:
        print(line, end='')

def copy_header_lines(lines, result_lines):
    if len(lines) < 1:
        return

    if lines[0].startswith("Server"):
        return

    while len(lines) >= 2:
        if lines[1].startswith("Server"):
            break;
        line = lines.pop(0)
        if line.strip():
            result_lines.append(line)

    if len(result_lines) > 0:
        result_lines.append("\n")

def copy_country_servers(lines, countries, result_lines):
    for country in countries:
        country_lwr = country.lower()
        country_ok = False
        index = 0
        while index < len(lines):
            line = lines[index]
            if line.startswith("##") and len(line) > 2:
                if line.lower().find(country_lwr, 2) > 0:
                    country_ok = True
                    result_lines.append(line)
                    del lines[index]
                    continue
                else:
                    country_ok = False
            elif country_ok:
                result_lines.append(line)
                del lines[index]
                continue

            index += 1

def make_sorted_lines(lines, countries):
    result_lines = []
    copy_header_lines(lines, result_lines)
    copy_country_servers(lines, countries, result_lines)
    result_lines.extend(lines)
    return result_lines

def uncomment_servers(lines):
    for index, item in enumerate(lines):
        if item.startswith("#Server"):
            lines[index] = item.replace("#Server", "Server", 1)

def usage():
    print(f"{sys.argv[0]} <mirrorlist_file> [country 1] [country 2] ... [country N]");

def main():
    argv = sys.argv[1:]
    countries = argv[1:]
    if (len(argv) == 0
            or argv[0] == "--help"
            or argv[0] == "-h"):
        usage()
        return -1

    with open(argv[0]) as mrfile:
        lines = mrfile.readlines()

    if len(lines) < 1:
        return -1

    uncomment_servers(lines)
    if len(countries) > 0:
        lines = make_sorted_lines(lines, countries)

    print_lines(lines)

if __name__ == "__main__":
    main()
else:
    print("unexpected call mode")
