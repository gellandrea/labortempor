# Define the time zone mappings
time_zone_mappings = {
    'Europe/Podgorica': 'Europe/Belgrade',
    # Add more mappings as needed
}

# Function to get the mapped time zone
def get_mapped_time_zone(time_zone):
    return time_zone_mappings.get(time_zone, time_zone)

# Example usage
original_time_zone = 'Europe/Podgorica'
mapped_time_zone = get_mapped_time_zone(original_time_zone)

print(f"Original Time Zone: {original_time_zone}")  # Output: Original Time Zone: Europe/Podgorica
print(f"Mapped Time Zone: {mapped_time_zone}")      # Output: Mapped Time Zone: Europe/Belgrade
