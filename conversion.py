# Conversion rate: 1 ETH = 3000 USD
CONVERSION_RATE = 3000.0

def convert_usd_to_eth(usd_value):
    try:
        usd = float(usd_value)
        eth = usd / CONVERSION_RATE
        # Format the result to 6 decimal places for clarity
        return f"{eth:.6f}"
    except ValueError:
        # If conversion fails, return the original string
        return usd_value

def process_line(line):
    # Split the line into parts based on commas
    parts = [part.strip() for part in line.split(",")]
    values = []
    for part in parts:
        # Split each part into key and value using the first colon
        try:
            key, value = part.split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            # If the key is "amount", convert USD to ETH
            if key == "amount":
                value = convert_usd_to_eth(value)
            values.append(value)
        except ValueError:
            # If no colon found, add the whole part
            values.append(part.strip())
    return values

def process_file(input_file, output_file):
    output_lines = []
    with open(input_file, "r") as infile:
        for line in infile:
            line = line.strip()
            if line:
                values = process_line(line)
                # Ensure the processed record has exactly 5 elements
                if len(values) == 5:
                    output_lines.append(str(values))
                else:
                    print("Warning: The following line does not have exactly 5 elements:")
                    print(line)
    # Write the output to cleaneddata.txt
    with open(output_file, "w") as outfile:
        for out_line in output_lines:
            outfile.write(out_line + "\n")

if __name__ == "__main__":
    process_file("data.txt", "cleaneddata.txt")
