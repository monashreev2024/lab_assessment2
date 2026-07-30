outage_records = [
    ("North Region", 4.5, 6200),
    ("South Region", 2.0, 1500),
    ("East Region", 7.5, 4800),
    ("West Region", 3.0, 8500),
    ("Central Region", 5.0, 3100)
]

longest_outage_record = max(outage_records, key=lambda x: x[1])
print(f"Region with the longest outage: {longest_outage_record[0]} ({longest_outage_record[1]} hours)")

total_duration = sum(record[1] for record in outage_records)
print(f"Total outage duration: {total_duration} hours")

print("Regions affecting more than 5,000 consumers:")
for region, duration, consumers in outage_records:
    if consumers > 5000:
        print(f" - {region} ({consumers} consumers affected)")

average_duration = total_duration / len(outage_records)
print(f"Average outage duration: {average_duration:.2f} hours")

sorted_records = sorted(outage_records, key=lambda x: x[1], reverse=True)
print("Regions sorted by outage duration (longest first):")
for region, duration, consumers in sorted_records:
    print(f" - {region}: {duration} hours")
