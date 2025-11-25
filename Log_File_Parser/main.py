from pathlib import Path as P
import csv

pwd = P.cwd()
main_folder = pwd / "Log_Files"


with open("errors_output.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "message"])
    for subfolder in main_folder.iterdir():
        if subfolder.is_dir():
            print(f"Inside Folder: {subfolder.name}")

            for file in subfolder.iterdir():
                if file.is_file() and file.suffix == ".log":
                        print(f"Selected file: {file}")

                        file_text = file.read_text(errors="ignore")
                        lines = file_text.splitlines()

                        for line in lines:
                            parts = line.split()

                            if len(parts) < 5:
                                 continue
                            
                            timestamp_str = " ".join(parts[0:2])
                            error_msg_str = " ".join(parts[2:])


                            writer.writerow([timestamp_str, error_msg_str])