# Video Converter

A Python-based video conversion application that utilizes a Tkinter GUI for ease of use. This tool allows users to select a video file, specify a desired output format, and define the output directory. The program then modifies and runs a batch script to perform the conversion. After completing one conversion, users are prompted to convert additional files with the same settings if desired.

## Features

- **Easy File Selection**: A user-friendly GUI enables file browsing and format selection.
- **Batch Script Modification**: Automatically customizes a batch script based on user input to perform file conversions.
- **Multiple Conversions**: Allows users to continue converting additional files with the same settings.
- **Error Handling**: Displays error messages for issues during the process.

## Requirements

- **Python 3.x**: Make sure Python is installed.
- **Tkinter**: Used for the GUI (usually comes pre-installed with Python on Windows).
- **FFmpeg**: Required for the actual conversion process.
- **Run.bat**: A batch script that performs the conversion. It must contain placeholders (`{start_format}`, `{end_format}`, `{output_path}`, `{input_file}`) for the script to work correctly.

### Installing FFmpeg

To install FFmpeg, follow these steps:

1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
2. Follow the installation instructions for your operating system.
3. Ensure FFmpeg is added to your system PATH so that it can be accessed globally from the command line.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. Run the Python script:
    ```bash
    python Converter.py
    ```

3. In the GUI:
   - Select the file to convert.
   - Enter the desired output format (e.g., `mp4`).
   - Choose the output path.
   - Click **Run** to start the conversion.

4. After the conversion, a prompt will ask if you'd like to convert another file with the same settings.

## Customizing `Run.bat`

The batch script (`Run.bat`) should contain placeholders:
   - `{start_format}` - The original file format (extension).
   - `{end_format}` - The user-specified output format.
   - `{output_path}` - The directory where the converted file will be saved.
   - `{input_file}` - The full path of the file to be converted.

These placeholders are automatically replaced with the appropriate values from the GUI inputs when the script runs.

## Example `Run.bat` Template

Here's a sample `Run.bat` template with placeholders:
```bat
ffmpeg -i "{input_file}" "{output_path}\output.{end_format}"
```

## Error Handling

If an error occurs during the conversion, a message box will appear, displaying the error details. Ensure all fields are filled out correctly to avoid issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
