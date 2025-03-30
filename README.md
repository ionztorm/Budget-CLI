# 💸 Budget CLI

A terminal-based personal finance tracker built with Python and SQLite. Easily track expenses and income, manage multiple accounts (like your current account, savings, or credit card), and export monthly reports to CSV or PDF — all from your terminal.

---

## 🚀 Features

- 🧾 **Add income and expenses** with category, description, and optional date
- 🏦 **Multi-account support** (e.g., Starling Current Account, Barclays Credit Card, Halifax Savings)
- 📊 **View summaries** by month or account
- 📁 **Export transactions** to CSV
- 🧾 **Generate monthly PDF reports** (print-ready)
- 🔍 **Search & filter** by date, category, or account
- ✅ Lightweight, fast, and offline-friendly

---

## 🛠 Tech Stack

- **Python 3**
- **SQLite3** — for persistent local data storage
- **FPDF2** — for PDF generation
- **argparse** — for building the CLI interface
- **tabulate** — for clean, formatted terminal tables

---

## 📦 Example Commands

```bash
# Create a new account
$ python main.py account create "Starling Current Account"

# Add an expense
$ python main.py add --account "Starling Current Account" --type expense --amount 45.99 \
                     --category groceries --desc "Weekly shop"

# View all transactions in March
$ python main.py list --month 2025-03

# View summary for Barclays Credit Card
$ python main.py summary --account "Barclays Credit Card"

# Export March 2025 report to CSV
$ python main.py export --account "Starling Current Account" --month 2025-03 --format csv

# Export PDF monthly report
$ python main.py export --account "Starling Current Account" --month 2025-03 --format pdf
```

---

## 👤 User Stories

> 🧍 **As a UK-based freelancer**, I want to keep my business and personal transactions separate across my bank accounts and cards.

> 🧍 **As a student**, I want to track my expenses across multiple accounts so I can stick to a monthly budget.

> 🧍 **As someone who prefers terminals to spreadsheets**, I want a simple, keyboard-only interface to manage my money and export monthly reports.

---

## 🗂 Planned Features

- 📅 Recurring transactions (monthly rent, salary)
- 📈 CLI-based visual charts (bar/pie)
- 🧠 Budget limits & overspending alerts
- 🔐 Password-protected or encrypted database (optional)

---

## 🧪 Getting Started

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/budget-cli.git
   cd budget-cli
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   python main.py
   ```

---

## 📝 Licence

MIT Licence. Use it, fork it, hack it — and feel free to contribute!
