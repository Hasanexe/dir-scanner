<!-- Title -->
# Simple Directory Scanner

<!-- Description -->
This is a simple directory scanner that can be used to find hidden files and directories on a website.

<!-- Usage instructions -->
## Usage

To use the directory scanner, follow these steps:

1. Install Python 3 if you haven't already done so.
2. Clone or download the repository to your local machine.
3. Navigate to the directory containing the `dir-scanner.py` file.
4. Run the following command to see the available options:

    ```bash
    python dir-scanner.py -h
    ```

    This will display the help message with the available options for the scanner.

5. To start a scan, run the following command:

    ```bash
    python dir-scanner.py url wordlist [-n threads] [-l] [-s]
    ```

    - Replace `url` with the target URL that you want to scan.
    - Replace `wordlist` with the path to the wordlist file that you want to use.
    - The `-n` option specifies the number of threads to use for the scan. The default value is 2.
    - The `-l` option shows only good results, while the `-s` option stops the scan when a file is found.

6. Wait for the scan to complete. The scanner will try all the combinations of file and directory names in the wordlist, and it will display any successful hits.

<!-- Contributing guidelines -->
## Contributing

If you find any issues with the `dir-scanner` or would like to contribute to the project, please feel free to submit a pull request or open an issue on the Github repository.

## License

`dir-scanner` is licensed under the [Creative Commons Attribution-NonCommercial (CC BY-NC) license](https://creativecommons.org/licenses/by-nc/4.0/).


