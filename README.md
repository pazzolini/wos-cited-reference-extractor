# 📚 WoS Cited Reference Extractor

A Python toolkit for parsing and analyzing **cited references** from **Web of Science** plain text exports.

> This project helps researchers extract and analyze citation data from Web of Science exports, enabling frequency analysis, network modeling, and bibliometric insights.

---

## 🔍 Why this exists

When exporting data from **Web of Science**, especially in **plain text** format using "Full Record and Cited References", the cited references are embedded in a non-tabular format. This makes them hard to extract, analyze, or count.

This repository provides:
- Clean **parsing** of cited references from `.txt` WoS exports
- Generation of **one row per cited reference**
- **Frequency analysis** to identify the most commonly cited works

---

## 📦 Features

- ✅ Parse WoS plain text exports (`.txt`)
- ✅ Output a DataFrame of all cited references
- ✅ Explode into **one cited reference per row**
- ✅ Compute how many articles cite each reference
- ✅ Ready for integration with bibliometric tools

---

## 🗂️ Project Structure

```text
wos-cited-reference-extractor/
├── data/                          # Example input files
│   └── sample_input.txt
├── scripts/
│   ├── extract_cited_refs.py     # Main extraction script
│   └── count_reference_frequency.py
├── outputs/
│   └── cited_reference_frequency.csv
│   └── exploded_references.csv
├── notebooks/
│   └── cited_reference_analysis.ipynb 
├── .gitignore
├── LICENSE                        # MIT License
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:pazzolini/wos-cited-reference-extractor.git
cd wos-cited-reference-extractor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the extraction

```bash
python scripts/extract_cited_refs.py data/sample_input.txt
```

This will generate:

```
outputs/exploded_references.csv
```

### 4. Run frequency analysis

```bash
python scripts/count_reference_frequency.py outputs/exploded_references.csv
```

This will generate:

```
outputs/cited_reference_frequency.csv
```

---



## 🧪 Sample Data

Place your **plain text export from Web of Science** in the `data/` folder.  
Make sure you choose **"Full Record and Cited References"** and **plain text format** when exporting.

---

## 🛠️ Requirements

- Python 3.8+
- `pandas`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📜 License

MIT License — feel free to use, fork, and adapt.

---

## 🤝 Contributing

Pull requests, suggestions, and stars are welcome!  
Feel free to open issues or reach out.

---

## ✨ Credits

Created by [@pazzolini](https://github.com/pazzolini)  
Inspired by the needs of bibliometric analysis and citation network studies.