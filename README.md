# DIRector Cut 🎬

🚀 **DIRectorscut_v2.py** is a Python script that **renames movie directories** into a clean and standardized format.  
It ensures your collection follows a proper naming convention:

Movie Title (Year) [movie version] [resolution] [video codec] [audio encoding] 

## 🛠 Features
- **Removes website references** (e.g., `www.Torrenting.com -`).
- **Prompts for approval** before renaming.
- **Skip (S) Option** – Skip renaming without logging.
- **Supports common video/audio formats** like `[x265]`, `[DTS]`, `[TrueHD]`.
- **Handles multiple movie versions** like `[Unrated]`, `[Extended]`, `[Director’s Cut]`.
- **"Approve All" (A) feature** – Includes commented-out "Approve All" (`A`) feature.

## 🚨 Executable File Warning
Before renaming, **DIRectorscut_v2.py** scans for **.exe files** inside your movie directories.  
If found, you will be prompted to **delete or keep each one manually**.  

**Example Warning:**
Found: X:\Movies\DangerousFile.exe Delete this file? (Y/N/Q to quit)

You can choose to:
- **(Y)** Delete the file.
- **(N)** Keep the file.
- **(Q)** Quit the script immediately.

This prevents **potential malware or unnecessary executables** from staying in your collection.

## 📌 Example Renaming
**Before:**  
www.web-site.poop - Mervie (1988) EXTENDED 1080p BluRay 5.1-DuDu
**After:**  
Mervie (1988) [Extended] [1080p] [5.1]

## 🔧 Installation & Usage
1. **Clone this repo**:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/DIRectorscut.git
   cd DIRectorscut
2. **Run the script**:
   ```bash
   python DIRectorscut_v2.py
3. **Enter the path to your movie directory and approve each rename.**

## 🔖 License
DIRector Cut is released under the MIT License – feel free to use, modify, and share!

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.