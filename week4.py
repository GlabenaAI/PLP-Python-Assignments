def modify_content(content):
    """
    Modify the content in some way.
    For this example, we'll convert all text to uppercase.
    """
    return content.upper()


def main():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the filename to read: ").strip()

        # Try reading the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new output file name
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified file has been saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()