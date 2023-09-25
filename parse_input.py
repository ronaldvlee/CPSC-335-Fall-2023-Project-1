import ast

def parse_input(fileName: str):
    data = []

    # Read input.txt line by line
    with open(fileName, 'r') as file:
        sch = []
        for line in file:
            line = line.strip() # Remove leading and trailing whitespace
            line = line.replace("':'", "','")
            
            # Convert the line to its proper type using ast.literal_eval
            try:
                converted_data = ast.literal_eval(line)
                sch.append(converted_data)

                if isinstance(converted_data, int):
                    data.append(sch)
                    sch = []
            except (SyntaxError, ValueError):
                print(f"Error converting line: {line}")
    return data