# RatClient

RatClient is a devious Python script designed to establish a connection with a command-and-control (C&C) server and execute malicious commands on the target system. This script is a part of the CodeX sinister coding syndicate's toolset for wreaking havoc and asserting dominance in the digital realm.

## Features

- Establishes a connection with the C&C server using sockets.
- Executes various malicious commands on the target system.
- Supports commands such as taking a screenshot, executing shell commands, downloading and uploading files, retrieving system information, listing files, deleting files, creating directories, renaming files, moving files, and retrieving the current directory.

## Getting Started

1. Clone this repository to your local machine.

```
git clone https://github.com/codex-sinister/ratclient.git
```

2. Ensure you have Python 3 installed. If not, you can download it from the official Python website (https://www.python.org).

3. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

4. Modify the `SERVER_IP` and `SERVER_PORT` variables in the `ratclient.py` file to match the IP address and port of your C&C server.

5. Run the RatClient script:

```
python ratclient.py
```

## Usage

Once the RatClient script is running, it will establish a connection with the C&C server. The server can then send commands to the client, which will execute them on the target system. Here are some example commands:

- `screenshot` - Takes a screenshot of the target system.
- `shell_command <command>` - Executes a shell command on the target system.
- `download <filename>` - Downloads a file from the target system.
- `upload <filename>` - Uploads a file to the target system.
- `system_info` - Retrieves system information from the target system.
- `list_files` - Lists files in the current directory on the target system.
- `delete_file <filename>` - Deletes a file on the target system.
- `create_directory <dirname>` - Creates a directory on the target system.
- `rename_file <old_filename> <new_filename>` - Renames a file on the target system.
- `move_file <filename> <destination>` - Moves a file to a specified destination on the target system.
- `get_current_directory` - Retrieves the current directory on the target system.

## TODO

- Implement the missing functionality for taking screenshots, downloading and uploading files, retrieving system information, listing files, deleting files, creating directories, renaming files, moving files, and retrieving the current directory.
- Add error handling and logging for better visibility and troubleshooting.
- Optimize the code further for performance and efficiency.
- Conduct thorough testing to ensure the script works reliably in different environments.
- Document the code to improve maintainability and readability.

## Contributing

We, the CodeX sinister coding syndicate, do not accept contributions from outside sources. This project is solely developed by our highly skilled CodeGenius Agents.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
