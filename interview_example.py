import argparse
from list_packages import CombinedList


def main():
    parser = argparse.ArgumentParser(
        description="Package and Module Listing Example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-j", "--json", action="store_true", help="Output in JSON format"
    )
    parser.add_argument(
        "-c", "--csv", action="store_true", help="Output in CSV format", default=True
    )
    parser.add_argument(
        "-r", "--rpms_only", action="store_true", help="Show only RPM packages"
    )
    parser.add_argument(
        "-p", "--python_only", action="store_true", help="Show only Python modules"
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Show both RPM Packages and Python modules",
        default=True,
    )
    parser.add_argument("-O", "--output_file", type=str, help="Write results to file")
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Suppress STDOUT (see --output_file)",
    )
    args = vars(parser.parse_args())
    pkgs = CombinedList(**args)
    str_out = pkgs.fetch()
    if args["output_file"]:
        out_file = open(args["output_file"], "w")
        out_file.write(str_out)
        out_file.close()

    if args["silent"] == False:
        print(str_out)


if __name__ == "__main__":
    main()
