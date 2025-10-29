import os

def parse_log(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write("=== Error and Warning Summary ===\n\n")

            error_count = 0
            warning_count = 0

            for line in infile:
                if "ERROR" in line:
                    outfile.write(line)
                    error_count += 1
                elif "WARNING" in line:
                    outfile.write(line)
                    warning_count += 1

            outfile.write(f"\nTotal Warnings: {warning_count}\n")
            outfile.write(f"Total Errors: {error_count}\n")

        print(f" Parsing complete! Summary saved to {output_file}")

    except FileNotFoundError:
        print(" Log file not found. Please check the file path.")
    except Exception as e:
        print(f" An error occurred: {e}")


if __name__ == "__main__":
    input_path = os.path.join(os.getcwd(), "PROJECTS", "sample.log")
    output_path = os.path.join(os.getcwd(), "PROJECTS", "error_summary.txt")
    parse_log(input_path, output_path)
