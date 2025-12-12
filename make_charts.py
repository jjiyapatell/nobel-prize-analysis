print("📊 Creating Nobel Prize charts for website...")
print("=" * 50)

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Load your Nobel Prize data
print("Loading laureates.csv...")
try:
    data = pd.read_csv("laureates.csv")
    print(f"✅ Successfully loaded {len(data)} rows, {len(data.columns)} columns")
    print(f"Columns: {list(data.columns)}")
except:
    print("❌ ERROR: Could not load laureates.csv")
    print("Make sure laureates.csv is in the same folder")
    exit()

# Chart 1: Nobel Prizes by Category
print("\n1. Creating 'Nobel Prizes by Category' chart...")
if 'category' in data.columns:
    category_counts = data['category'].value_counts()
    
    plt.figure(figsize=(12, 7))
    bars = plt.bar(category_counts.index, category_counts.values, color='lightblue', edgecolor='black')
    plt.title('Nobel Prizes by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Number of Prizes', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Add numbers on top of bars
    for bar, count in zip(bars, category_counts.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                str(count), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('charts/nobel_by_category.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: charts/nobel_by_category.png")
else:
    print("   ❌ Skipped: No 'category' column found")

# Chart 2: Prizes by Year
print("\n2. Creating 'Nobel Prizes by Year' chart...")
if 'year' in data.columns:
    data['year'] = pd.to_numeric(data['year'], errors='coerce')
    year_counts = data['year'].value_counts().sort_index()
    
    plt.figure(figsize=(14, 7))
    plt.plot(year_counts.index, year_counts.values, 
             linewidth=2.5, marker='o', markersize=4, color='darkgreen')
    plt.title('Nobel Prizes Awarded Each Year', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Prizes', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('charts/nobel_by_year.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: charts/nobel_by_year.png")
else:
    print("   ❌ Skipped: No 'year' column found")

# Chart 3: Simple summary chart
print("\n3. Creating 'Summary Chart'...")
plt.figure(figsize=(10, 6))

# Count total entries
total = len(data)

# Count by category if available
if 'category' in data.columns:
    top_categories = data['category'].value_counts().head(3)
    labels = [f"{cat}\n({count})" for cat, count in zip(top_categories.index, top_categories.values)]
    plt.pie(top_categories.values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Top 3 Nobel Prize Categories\nTotal: {total} entries', fontsize=14)
else:
    # Simple bar showing total count
    plt.bar(['Total Entries'], [total], color='skyblue')
    plt.title(f'Nobel Prize Dataset\nTotal: {total} entries', fontsize=14)
    plt.ylabel('Count')

plt.tight_layout()
plt.savefig('charts/summary_chart.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/summary_chart.png")

print("\n" + "=" * 50)
print("🎉 All charts created successfully!")
print("Check your charts folder:")
print("  ls charts/")
print("\nNext steps:")
print("1. Update index.html to show these charts")
print("2. Run: git add charts/ index.html")
print("3. Run: git commit -m 'Add charts'")
print("4. Run: git push origin main")