import streamlit as st
import csv
import pandas as pd
from collections import defaultdict
from datetime import datetime

FILE_NAME = 'expenses.csv'

def add_expense_ui():
    st.subheader("➕ Add a New Expense")

    date = st.date_input("Date", datetime.today())
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_input("Description")

    if st.button("Add Expense"):
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        st.success("Expense added!")

def view_summary_ui():
    st.subheader("📊 Expense Summary")

    try:
        df = pd.read_csv(FILE_NAME)
        df['amount'] = df['amount'].astype(float)
    except FileNotFoundError:
        st.info("No expenses added yet.")
        return

    st.dataframe(df)

    total = df['amount'].sum()
    st.markdown(f"### 💵 Total Spent: ${total:.2f}")

    chart = df.groupby('category')['amount'].sum()
    st.bar_chart(chart)

def main():
    st.title("💰 Simple Expense Tracker")

    menu = ["Add Expense", "View Summary"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Expense":
        add_expense_ui()
    elif choice == "View Summary":
        view_summary_ui()

if __name__ == '__main__':
    main()
