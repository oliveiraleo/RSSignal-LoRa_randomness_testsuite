import os
from FrequencyTest import FrequencyTest
from RunTest import RunTest
from Serial import Serial
from ApproximateEntropy import ApproximateEntropy
from CumulativeSum import CumulativeSums

# NOTE: Code based on the file test_e.py

def main(fileName):
    # Vars
    file_format = ".txt"
    filename = fileName
    filename += file_format
    #open and read the binary data of file
    data_path = os.path.join(os.getcwd(), 'results', 'key-after-reconciliation', filename)
    handle = open(data_path)
    data_list = []

    for line in handle:
        data_list.append(line.strip().rstrip())

    binary_data = ''.join(data_list)
    binary_data_length = len(binary_data)
    binary_data_slice = binary_data[:1000000]

    #execute the tests and get their results
    test01_result = FrequencyTest.monobit_test(binary_data_slice)
    test02_result = FrequencyTest.block_frequency(binary_data_slice)
    test03_result = RunTest.run_test(binary_data_slice)
    test04_result = RunTest.longest_one_block_test(binary_data_slice)
    test11_result = Serial.serial_test(binary_data_slice)
    test12_result = ApproximateEntropy.approximate_entropy_test(binary_data_slice)
    test13_result_F = CumulativeSums.cumulative_sums_test(binary_data_slice, 0)
    test13_result_B = CumulativeSums.cumulative_sums_test(binary_data_slice, 1)

    #prints the results
    print("\n=>", filename)
    print(f"-> Input length: {binary_data_length} \n")
    print('2.1. Frequency Test:\t\t\t\t\t\t\t\t\t', test01_result)
    print('2.2. Block Frequency Test:\t\t\t\t\t\t\t\t', test02_result)
    print('2.3. Run Test:\t\t\t\t\t\t\t\t\t\t\t', test03_result)
    print('2.4. Run Test (Longest Run of Ones): \t\t\t\t\t', test04_result)
    print('2.11. Serial Test:\t\t\t\t\t\t\t\t\t\t', test11_result)
    print('2.12. Approximate Entropy Test:\t\t\t\t\t\t\t', test12_result)
    print('2.13. Cumulative Sums (Forward):\t\t\t\t\t\t', test13_result_F)
    print('2.13. Cumulative Sums (Backward):\t\t\t\t\t\t', test13_result_B)

    # TODO save the data on a file
    # return_data = [filename, binary_data_length, test01_result, test02_result, test03_result, test04_result, test11_result, test12_result, test13_result_F, test13_result_B]
    # return return_data

if __name__ == "__main__":
    main()