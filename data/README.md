# Dataset: Hotel Booking Demand

## 1. Source and License

- **Source:** Antonio, N., de Almeida, A., & Nunes, L. (2019). *Hotel booking demand datasets*. **Data in Brief**, 22, 41–49.
- **DOI:** [https://doi.org/10.1016/j.dib.2018.11.126](https://doi.org/10.1016/j.dib.2018.11.126)
- **Article page:** [https://www.sciencedirect.com/science/article/pii/S2352340918315191](https://www.sciencedirect.com/science/article/pii/S2352340918315191)
- **License:** Creative Commons Attribution 4.0 International (**CC BY 4.0**).

## 2. Which Files to Download and Where to Save Them

The analysis requires the two CSV files provided in the article's supplementary material, saved inside this directory (`data/`) with their original filenames:

- `data/H1.csv` — Resort Hotel bookings (Algarve, Portugal; 40,060 rows, 31 columns).
- `data/H2.csv` — City Hotel bookings (Lisbon, Portugal; 79,330 rows, 31 columns).

### Automated download

From the repository root, run:

```bash
python data/download.py
```

### Manual download

1. Open the [ScienceDirect article page](https://www.sciencedirect.com/science/article/pii/S2352340918315191) and scroll to **Appendix A. Supplementary material** (or click *"Download all supplementary files"*).
2. Download the archive `1-s2.0-S2352340918315191-mmc2.zip` ([direct link](https://ars.els-cdn.com/content/image/1-s2.0-S2352340918315191-mmc2.zip)), which is the first 1 MB `.zip` file listed and contains the datasets in `.csv` format (the second `.zip` file contains `.rds` files for R; the third contains the SQL extraction query).
3. Extract `H1.csv` and `H2.csv` directly into `data/`.

## 3. What a Row Represents

Each row represents **a single hotel booking transaction** scheduled to arrive between **July 1, 2015 and August 31, 2017** at either the Resort Hotel (`H1.csv`) or the City Hotel (`H2.csv`). The dataset includes both bookings that effectively checked in and bookings that were canceled or resulted in a no-show, described across 31 variables (booking lead time, arrival date, stay duration, guest composition, meal plan, distribution channel, average daily rate, deposit type, and reservation status).

## 4. How the Data Were Collected

These are **observational data**: administrative records of real booking transactions that occurred naturally, rather than data from a controlled experiment or a survey.

The records were extracted by the authors from the two hotels' **Property Management System (PMS)** databases in Portugal and anonymized to remove any personally identifiable information regarding guests or the specific properties. Because variables such as pricing (`ADR`), deposit policies (`DepositType`), and sales channels were not randomly assigned to bookings, statistical associations observed in the data may reflect confounding and selection effects rather than direct causal relationships.