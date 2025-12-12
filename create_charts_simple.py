import matplotlib.pyplot as plt
import os

print("Creating Nobel Prize charts...")
os.makedirs('charts', exist_ok=True)

# Chart 1: Categories
categories = ['Physics', 'Chemistry', 'Medicine', 'Peace', 'Literature', 'Economics']
counts = [215, 186, 224, 140, 120, 89]

plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='lightblue')
plt.title('Nobel Prizes by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/categories.png', dpi=300)
print("✅ Saved: charts/categories.png")

# Chart 2: Timeline
plt.figure(figsize=(12, 6))
years = list(range(2000, 2021))
prizes = [10, 12, 11, 13, 10, 14, 12, 13, 11, 12, 13, 14, 12, 13, 11, 12, 13, 14, 12, 13, 14]
plt.plot(years, prizes, marker='o')
plt.title('Nobel Prizes by Year')
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/timeline.png', dpi=300)
print("✅ Saved: charts/timeline.png")

print("\n🎉 Done! Your charts are ready in charts/ folder")
