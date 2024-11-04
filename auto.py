import subprocess
import os
import shutil
import time

def main():
    # Gather user input for test details
    level = input("What grade level is this test: ")
    test_name = input("What is the test name: ")
    test_name_final = f"{level}_{test_name}"
    print("Creating test:", test_name_final)
    time.sleep(2)
    input("Make sure to edit the test.decaf with your desired test file before running this script (press enter to continue)")
    

    # Directories for input, output, expected results, and tests
    inputs_dir = "./tests/inputs"
    outputs_dir = "./tests/outputs"
    expected_dir = "./tests/expected"
    tests_dir = "./tests"
    os.makedirs(inputs_dir, exist_ok=True)
    os.makedirs(outputs_dir, exist_ok=True)
    os.makedirs(expected_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    # Paths for output and expected files
    output_file_path = os.path.join(outputs_dir, f"{test_name_final}.txt")
    expected_file_path = os.path.join(expected_dir, f"{test_name_final}.txt")
    test_decaf_path = "test.decaf"  # This is the fixed input file the user edits directly
    input_file_path = os.path.join(inputs_dir, f"{test_name_final}.decaf")  # This is the input file to be created

    # Copy the modified test.decaf to inputs/input_file.decaf
    shutil.copy(test_decaf_path, input_file_path)
    print(f"Copied {test_decaf_path} to {input_file_path}")
    time.sleep(2)

    # Run the compiler with --fdump-iloc to generate output
    try:
        result_iloc = subprocess.run(
            ['/cs/students/cs432/f24/decaf', '--fdump-iloc', test_decaf_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Save output to ./outputs
        with open(output_file_path, 'w') as f_output:
            f_output.write(result_iloc.stdout)
        print("Output saved to:", output_file_path)
        time.sleep(2)

        # Run the compiler without --fdump-iloc to generate expected output
        result_expected = subprocess.run(
            ['/cs/students/cs432/f24/decaf', test_decaf_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Save output to ./expected
        with open(expected_file_path, 'w') as f_expected:
            f_expected.write(result_expected.stdout)
        print("Expected output saved to:", expected_file_path)
        time.sleep(2)

        # Add the run_test command to ./test/itests.include
        itests_include_path = os.path.join(tests_dir, "itests.include")
        with open(itests_include_path, 'a') as f_include:
            f_include.write(f"run_test {test_name_final} ")
            f_include.write(f"\"inputs/{test_name_final}.decaf\" \n")
        print(f"Added test commands to {itests_include_path}")
        time.sleep(2)

    except subprocess.CalledProcessError as e:
        print(f"Error running compiler: {e.stderr}")

    print("MAKE SURE TO TURN DEBUG OFF IN MAIN.C IN ORDER TO PASS TESTS (CHANGE LINE 18 TO FALSE)")
if __name__ == '__main__':
    main()

