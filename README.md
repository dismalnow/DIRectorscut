# DIRector Cut 🎬

🚀 **DIRectorscut_v1.py** is a script that **renames movie directories** into a clean and standardized format.  
It ensures your collection's directories follow a sane naming convention structure like:

Movie Title (Year) [video codec] [audio encoding] [movie version]

## 🛠 Features
- Prompts for approval before renaming.
- Extracts key details: **Title, Year, Codec, Audio Format, Version (Unrated, Extended, etc.).**
- Skips unnecessary clutter like `[BluRay]`, `[WEBRip]`, `[YTS]`, etc.
- **Asks the user for the movie directory** instead of hardcoding it.
- Keeps your library **organized and beautiful**.

## 📌 Example
**Before:**  
Henry And Kitel Run From Kailoon Bay (2008) Unrated 1080p BluRay x264 English AC3 5.1 - BeAvIs  

**After:**  
Henry And Kitel Run From Kailoon Bay (2008) [x264] [AC3] [Unrated]

## 🔧 Installation & Usage
1. **Clone this repo**:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/DIRectorscut.git
   cd DIRectorscut
2. **Run the script**:  
   ```bash
   python DIRectorscut_v1.py
3. **Enter the path to your movie directory and approve each rename.**

## 🔖 License
DIRector Cut is released under the MIT License – feel free to use, modify, and share!

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
