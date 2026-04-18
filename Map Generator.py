import random
import webbrowser
import time
import os

# Cord database generated with ChatGPT
CITY_COORDINATES = {
    # North Africa
    "Cairo": (30.0444, 31.2357),
    "Alexandria": (31.2001, 29.9187),
    "Giza": (29.9870, 31.2118),
    "Casablanca": (33.5731, -7.5898),
    "Rabat": (34.0209, -6.8416),
    "Marrakesh": (31.6295, -7.9811),
    "Fes": (34.0333, -5.0000),
    "Tangier": (35.7595, -5.8340),
    "Tunis": (36.8065, 10.1815),
    "Algiers": (36.7538, 3.0588),
    "Oran": (35.6971, -0.6308),
    "Tripoli": (32.8872, 13.1913),
    "Benghazi": (32.1167, 20.0667),
    "Khartoum": (15.5007, 32.5599),
    "Nouakchott": (18.0735, -15.9582),
    
    # West Africa
    "Lagos": (6.5244, 3.3792),
    "Abuja": (9.0765, 7.3986),
    "Kano": (12.0022, 8.5919),
    "Accra": (5.6037, -0.1870),
    "Kumasi": (6.6666, -1.6163),
    "Abidjan": (5.3200, -4.0167),
    "Dakar": (14.7167, -17.4677),
    "Bamako": (12.6392, -8.0029),
    "Ouagadougou": (12.3714, -1.5197),
    "Niamey": (13.5127, 2.1126),
    "Conakry": (9.5092, -13.7122),
    "Monrovia": (6.3106, -10.8048),
    "Freetown": (8.4657, -13.2317),
    "Cotonou": (6.3703, 2.3912),
    "Lomé": (6.1375, 1.2123),
    
    # East Africa
    "Nairobi": (-1.2921, 36.8219),
    "Mombasa": (-4.0435, 39.6682),
    "Addis Ababa": (9.0320, 38.7469),
    "Dar es Salaam": (-6.7924, 39.2083),
    "Zanzibar City": (-6.1659, 39.2026),
    "Kampala": (0.3136, 32.5811),
    "Kigali": (-1.9441, 30.0619),
    "Bujumbura": (-3.3614, 29.3599),
    "Mogadishu": (2.0469, 45.3182),
    "Djibouti City": (11.5721, 43.1456),
    "Asmara": (15.3229, 38.9251),
    "Juba": (4.8517, 31.5825),
    
    # Central & Southern Africa
    "Kinshasa": (-4.4419, 15.2663),
    "Brazzaville": (-4.2634, 15.2429),
    "Luanda": (-8.8390, 13.2894),
    "Yaoundé": (3.8480, 11.5021),
    "Douala": (4.0511, 9.7679),
    "Libreville": (0.4162, 9.4673),
    "Harare": (-17.8252, 31.0335),
    "Maputo": (-25.9692, 32.5732),
    
    # East Asia
    "Tokyo": (35.6895, 139.6917),
    "Yokohama": (35.4437, 139.6380),
    "Osaka": (34.6937, 135.5023),
    "Kyoto": (35.0116, 135.7680),
    "Beijing": (39.9042, 116.4074),
    "Shanghai": (31.2304, 121.4737),
    "Guangzhou": (23.1291, 113.2644),
    "Shenzhen": (22.5431, 114.0579),
    "Hong Kong": (22.3193, 114.1694),
    "Tianjin": (39.0841, 117.2009),
    "Chongqing": (29.5630, 106.5516),
    "Chengdu": (30.5728, 104.0668),
    "Xi'an": (34.3416, 108.9402),
    "Nanjing": (32.0603, 118.7781),
    "Wuhan": (30.5928, 114.3055),
    "Seoul": (37.5665, 126.9780),
    "Busan": (35.1796, 129.0756),
    "Incheon": (37.4563, 126.7052),
    "Pyongyang": (39.0392, 125.7625),
    "Ulaanbaatar": (47.8864, 106.9057),
    
    # Southeast Asia
    "Bangkok": (13.7367, 100.5231),
    "Chiang Mai": (18.7883, 98.9853),
    "Phuket": (7.8804, 98.3923),
    "Hanoi": (21.0285, 105.8542),
    "Ho Chi Minh City": (10.8231, 106.6297),
    "Da Nang": (16.0544, 108.2022),
    "Jakarta": (-6.2088, 106.8456),
    "Surabaya": (-7.2575, 112.7521),
    "Bandung": (-6.9175, 107.6191),
    "Denpasar": (-8.6705, 115.2126),
    "Manila": (14.5995, 120.9842),
    "Cebu City": (10.3157, 123.8854),
    "Davao City": (7.1907, 125.4553),
    "Kuala Lumpur": (3.1390, 101.6869),
    "George Town": (5.4149, 100.3288),
    "Johor Bahru": (1.4927, 103.7414),
    "Singapore": (1.3521, 103.8198),
    "Yangon": (16.8409, 96.1735),
    "Phnom Penh": (11.5564, 104.9282),
    "Siem Reap": (13.3633, 103.8564),
    "Vientiane": (17.9757, 102.6331),
    "Dili": (-8.5569, 125.5603),
    
    # Netherlands
    "Heerlen": (50.8882, 5.9795),
    "Brunssum": (50.9466, 5.9704),
    "Landgraaf": (50.8913, 6.0218),
    "Voerendaal": (50.8822, 5.9309),

    # South Asia
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Kolkata": (22.5726, 88.3639),
    "Chennai": (13.0827, 80.2707),
    "Bengaluru": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Ahmedabad": (23.0225, 72.5714),
    "Pune": (18.5204, 73.8567),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462),
    "Karachi": (24.8607, 67.0011),
    "Lahore": (31.5497, 74.3436),
    "Islamabad": (33.6844, 73.0479),
    "Rawalpindi": (33.5651, 73.0169),
    "Dhaka": (23.8103, 90.4125),
    "Chittagong": (22.3569, 91.7832),
    "Kathmandu": (27.7172, 85.3240),
    "Pokhara": (28.2096, 83.9856),
    "Colombo": (6.9271, 79.8612),
    "Male": (4.1755, 73.5093),
    "Thimphu": (27.4712, 89.6339),
    
    # Central Asia
    "Tashkent": (41.2995, 69.2401),
    "Samarkand": (39.6272, 66.9750),
    "Almaty": (43.2220, 76.8512),
    "Astana": (51.1694, 71.4491),
    "Bishkek": (42.8746, 74.5698),
    "Dushanbe": (38.5598, 68.7870),
    "Ashgabat": (37.9601, 58.3261),
    
    # West Asia (Middle East)
    "Tehran": (35.6892, 51.3890),
    "Isfahan": (32.6546, 51.6680),
    "Shiraz": (29.5918, 52.5837),
    "Baghdad": (33.3152, 44.3661),
    "Erbil": (36.1912, 44.0092),
    "Istanbul": (41.0082, 28.9784),
    "Ankara": (39.9334, 32.8597),
    "Izmir": (38.4189, 27.1287),
    "Riyadh": (24.7136, 46.6753),
    "Jeddah": (21.5433, 39.1728),
    "Mecca": (21.3891, 39.8579),
    "Medina": (24.5247, 39.5692),
    "Dubai": (25.2048, 55.2708),
    "Abu Dhabi": (24.4539, 54.3773),
    "Doha": (25.2854, 51.5310),
    "Manama": (26.2285, 50.5869),
    "Kuwait City": (29.3759, 47.9774),
    "Muscat": (23.5880, 58.3829),
    "Sana'a": (15.3694, 44.1910),
    "Amman": (31.9454, 35.9284),
    
    # Western Europe
    "London": (51.5074, -0.1278),
    "Manchester": (53.4808, -2.2426),
    "Birmingham": (52.4862, -1.8904),
    "Paris": (48.8566, 2.3522),
    "Marseille": (43.2965, 5.3698),
    "Lyon": (45.7640, 4.8357),
    "Berlin": (52.5200, 13.4050),
    "Munich": (48.1351, 11.5820),
    "Hamburg": (53.5511, 9.9937),
    "Frankfurt": (50.1109, 8.6821),
    "Cologne": (50.9375, 6.9603),
    "Brussels": (50.8503, 4.3517),
    "Antwerp": (51.2194, 4.4025),
    "Amsterdam": (52.3676, 4.9041),
    "Rotterdam": (51.9244, 4.4777),
    "The Hague": (52.0705, 4.3007),
    "Vienna": (48.2082, 16.3738),
    "Zurich": (47.3769, 8.5417),
    "Geneva": (46.2044, 6.1432),
    "Luxembourg City": (49.6117, 6.1319),
    
    # Southern Europe
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763),
    "Seville": (37.3891, -5.9845),
    "Lisbon": (38.7223, -9.1393),
    "Porto": (41.1579, -8.6291),
    "Rome": (41.9028, 12.4964),
    "Milan": (45.4642, 9.1900),
    "Naples": (40.8518, 14.2681),
    "Florence": (43.7696, 11.2558),
    "Venice": (45.4408, 12.3155),
    "Turin": (45.0703, 7.6869),
    "Athens": (37.9838, 23.7275),
    "Thessaloniki": (40.6401, 22.9444),
    "Valletta": (35.8989, 14.5146),
    
    # Northern Europe
    "Stockholm": (59.3293, 18.0686),
    "Gothenburg": (57.7089, 11.9746),
    "Oslo": (59.9139, 10.7522),
    "Bergen": (60.3913, 5.3228),
    "Copenhagen": (55.6761, 12.5683),
    "Aarhus": (56.1629, 10.2039),
    "Helsinki": (60.1699, 24.9384),
    "Reykjavik": (64.1466, -21.9426),
    "Dublin": (53.3498, -6.2603),
    "Tallinn": (59.4370, 24.7536),
    "Riga": (56.9496, 24.1052),
    "Vilnius": (54.6872, 25.2797),
    
    # Central & Eastern Europe
    "Warsaw": (52.2297, 21.0122),
    "Krakow": (50.0647, 19.9450),
    "Gdansk": (54.3520, 18.6466),
    "Prague": (50.0755, 14.4378),
    "Brno": (49.1951, 16.6068),
    "Budapest": (47.4979, 19.0402),
    "Bucharest": (44.4268, 26.1025),
    "Cluj-Napoca": (46.7712, 23.6236),
    "Sofia": (42.6977, 23.3219),
    "Belgrade": (44.7866, 20.4489),
    "Zagreb": (45.8150, 15.9819),
    "Split": (43.5081, 16.4402),
    "Ljubljana": (46.0569, 14.5058),
    "Bratislava": (48.1486, 17.1077),
    "Sarajevo": (43.8563, 18.4131),
    "Skopje": (41.9973, 21.4280),
    "Tirana": (41.3275, 19.8187),
    "Podgorica": (42.4304, 19.2594),
    "Pristina": (42.6629, 21.1655),
    "Chisinau": (47.0105, 28.8638),
    "Minsk": (53.9045, 27.5615),
    "Kyiv": (50.4501, 30.5234),
    "Lviv": (49.8397, 24.0297),
    "Odesa": (46.4825, 30.7233),
    "Moscow": (55.7558, 37.6173),
    "Saint Petersburg": (59.9311, 30.3609),
    "Kazan": (55.7887, 49.1221),
    
    # North America - Canada
    "Toronto": (43.6519, -79.3832),
    "Vancouver": (49.2827, -123.1207),
    "Montreal": (45.5017, -73.5673),
    "Calgary": (51.0447, -114.0719),
    "Ottawa": (45.4215, -75.6972),
    "Quebec City": (46.8139, -71.2080),
    
    # United States
    "New York City": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Francisco": (37.7749, -122.4194),
    "Boston": (42.3601, -71.0589),
    "Seattle": (47.6062, -122.3321),
    "Denver": (39.7392, -104.9903),
    "Miami": (25.7617, -80.1918),
    "Atlanta": (33.7490, -84.3880),
    "Detroit": (42.3314, -83.0458),
    "Portland": (45.5152, -122.6784),
    "Las Vegas": (36.1699, -115.1398),
    "New Orleans": (29.9511, -90.0715),
    "Washington, D.C.": (38.9072, -77.0369),
    
    # Mexico & Central America
    "Mexico City": (19.4326, -99.1332),
    "Guadalajara": (20.6597, -103.3496),
    "Monterrey": (25.6866, -100.3161),
    "Cancun": (21.1619, -86.8515),
    "Guatemala City": (14.6349, -90.5069),
    "San Salvador": (13.6929, -89.2182),
    "Tegucigalpa": (14.0650, -87.1715),
    "Managua": (12.1142, -86.2367),
    "San Jose": (9.9281, -84.0907),
    "Panama City": (8.9824, -79.5199),
    
    # Caribbean
    "Havana": (23.1136, -82.3666),
    "Santo Domingo": (18.4861, -69.9312),
    "San Juan": (18.4655, -66.1057),
    "Port-au-Prince": (18.5392, -72.3350),
    "Kingston": (17.9714, -76.7926),
    
    # South America
    "São Paulo": (-23.5505, -46.6333),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Brasília": (-15.7939, -47.8828),
    "Salvador": (-12.9714, -38.5014),
    "Fortaleza": (-3.7172, -38.5432),
    "Belo Horizonte": (-19.9167, -43.9345),
    "Buenos Aires": (-34.6037, -58.3816),
    "Córdoba": (-31.4201, -64.1888),
    "Rosario": (-32.9468, -60.6393),
    "Santiago": (-33.4489, -70.6693),
    "Valparaíso": (-33.0472, -71.6127),
    "Lima": (-12.0464, -77.0428),
    "Cusco": (-13.5319, -71.9675),
    "Bogotá": (4.7110, -74.0721),
    "Medellín": (6.2442, -75.5812),
    "Cali": (3.4516, -76.5320),
    "Cartagena": (10.3910, -75.4794),
    "Quito": (-0.1807, -78.4678),
    "Guayaquil": (-2.1199, -79.9230),
    "Caracas": (10.4806, -66.9036),
    "Maracaibo": (10.6427, -71.6127),
    "Montevideo": (-34.9011, -56.1645),
    "Asunción": (-25.2667, -57.6667),
    "La Paz": (-16.5000, -68.1500),
    "Sucre": (-19.0333, -65.2627),
    "Santa Cruz de la Sierra": (-17.7833, -63.1833),
    "Georgetown": (6.8013, -58.1550),
    "Paramaribo": (5.8520, -55.2038),
    "Cayenne": (4.9224, -52.3134),
    
    # Oceania
    "Sydney": (-33.8688, 151.2093),
    "Melbourne": (-37.8136, 144.9631),
    "Brisbane": (-27.4698, 153.0251),
    "Perth": (-31.9505, 115.8605),
    "Adelaide": (-34.9285, 138.6007),
    "Canberra": (-35.2809, 149.1300),
    "Hobart": (-42.8821, 147.3251),
    "Darwin": (-12.4634, 130.8456),
    "Auckland": (-36.8485, 174.7633),
    "Wellington": (-41.2865, 174.7762),
    "Christchurch": (-43.5321, 172.6362),
    "Hamilton": (-37.7870, 175.2793),
    "Port Moresby": (-9.4438, 147.1803),
    "Suva": (-18.1416, 178.4419),
    "Honiara": (-9.4456, 159.9724),
    "Nouméa": (-22.2758, 166.4580),
}

def generate_locations(city_name, num_locations=30):
    
    if city_name not in CITY_COORDINATES:
        print(f"City '{city_name}' not found in database!")
        print(f"Available cities: {len(CITY_COORDINATES)} total")
        return []
    
    center_lat, center_lon = CITY_COORDINATES[city_name]
    
    # Random offset range
    max_offset = 0.045  # about a 5km radius
    
    locations = []
    
    for i in range(num_locations):
        # Generate random offset
        lat_offset = random.uniform(-max_offset, max_offset)
        lon_offset = random.uniform(-max_offset, max_offset)
        
        final_lat = center_lat + lat_offset
        final_lon = center_lon + lon_offset

        url = f"https://www.google.com/maps/@{final_lat},{final_lon},3a,75y,90t/data=!3m8!1e1!3m6!1sAF1QipP4x8KjR6vM2nBc7Xy3Lw9FqA5sDgHjK1zZxXcVbN!2e10!3e11!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3D123456%26cb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26yaw%3D90%26pitch%3D0%26thumbfov%3D90!7i16384!8i8192"
        
        locations.append(url)
    
    return locations

def save_to_file(city_name, locations, filename=None):
    
    if filename is None:
        filename = f"{city_name.lower().replace(' ', '_')}_locations.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        for url in locations:
            f.write(url + '\n')
    
    return filename

def generate_multiple_cities(cities_dict):
    
    print("\n" + "="*60)
    print("MULTI-CITY LOCATION GENERATOR")
    print("="*60)
    
    for city_name, num_locations in cities_dict.items():
        print(f"\nGenerating {num_locations} locations for {city_name}...")
        
        locations = generate_locations(city_name, num_locations)
        
        if locations:
            filename = save_to_file(city_name, locations)
            print(f"Saved to: {filename}")
            print(f"First location: {locations[0][:80]}...")
        else:
            print(f"Failed to generate for {city_name}")

def interactive_mode():
    
    print("\n" + "="*60)
    print("STREET VIEW LOCATION GENERATOR")
    print("="*60)
    print(f"\nDatabase has {len(CITY_COORDINATES)} cities worldwide!")
    
    # Show available cities by region
    print("\nAvailable regions:")
    regions = {
        "Netherlands": ["Heerlen", "Brunssum", "Landgraaf", "Voerendaal"],
        "Africa": ["Cairo", "Lagos", "Nairobi", "Casablanca", "Cape Town"],
        "Asia": ["Tokyo", "Beijing", "Bangkok", "Mumbai", "Singapore"],
        "Europe": ["London", "Paris", "Berlin", "Rome", "Amsterdam"],
        "North America": ["New York City", "Los Angeles", "Toronto", "Mexico City"],
        "South America": ["São Paulo", "Buenos Aires", "Lima", "Bogotá"],
        "Oceania": ["Sydney", "Melbourne", "Auckland", "Suva"]
    }
    
    for region, cities in regions.items():
        print(f"  {region}: {', '.join(cities[:3])}... ({len(cities)} total)")
    
    while True:
        print("\n" + "-"*40)
        city_name = input("Enter city name (or 'list' to see all, 'quit' to exit): ").strip()
        
        if city_name.lower() == 'quit':
            break
        
        if city_name.lower() == 'list':
            print("\nAll available cities:")
            for i, city in enumerate(sorted(CITY_COORDINATES.keys()), 1):
                print(f"{i:3}. {city}")
            continue
        
        if city_name not in CITY_COORDINATES:
            print(f"City '{city_name}' not found! Use 'list' to see all cities.")
            continue
        
        while True:
            try:
                num = input(f"How many locations for {city_name}? (1-50): ")
                num_locations = int(num)
                if 1 <= num_locations <= 50:
                    break
                else:
                    print("Please enter a number between 1 and 50")
            except ValueError:
                print("Please enter a valid number")
        
        print(f"\n🔍 Generating {num_locations} random locations in {city_name}...")
        locations = generate_locations(city_name, num_locations)
        
        if locations:
            filename = save_to_file(city_name, locations)
            print(f"Success! Saved to: {filename}")
            
            print(f"\nPreview (first 3 locations):")
            for i, url in enumerate(locations[:3], 1):
                print(f"  {i}. {url}")
            
            # Option to test in browser
            test = input("\nTest first location in browser? (y/n): ").lower()
            if test == 'y' and locations:
                print("Opening in browser...")
                webbrowser.open(locations[0])
                time.sleep(2)
        else:
            print("Generation failed!")

def batch_generate_from_list(city_list_file):
    """Generate locations from a text file containing city names and numbers"""
    try:
        with open(city_list_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split(',')
                if len(parts) == 2:
                    city = parts[0].strip()
                    num = int(parts[1].strip())
                    locations = generate_locations(city, num)
                    if locations:
                        filename = save_to_file(city, locations)
                        print(f"{city}: {num} locations saved to {filename}")
                    else:
                        print(f"{city}: Failed to generate")
                else:
                    print(f"Invalid line: {line}")
    except FileNotFoundError:
        print(f"File '{city_list_file}' not found!")

def main():
    """Main menu"""
    
    print("\n" + "="*60)
    print("Street View Locations Generator")
    print("="*60)
    print("\nThis tool generates random Street View locations around any city")
    print("These locations will work in Ngav Guessr.")
    
    while True:
        print("\n" + "-"*40)
        print("Menu:")
        print("1. Interactive Mode (choose cities one by one)")
        print("2. Generate for specific city")
        print("3. Generate for multiple cities (batch mode)")
        print("4. Create a custom map file from a list")
        print("5. Show city database statistics")
        print("6. Exit")
        
        choice = input("\nOption: ").strip()
        
        if choice == '1':
            interactive_mode()
        
        elif choice == '2':
            city = input("Enter city name: ").strip()
            if city in CITY_COORDINATES:
                num = int(input("Number of locations (1-50): "))
                locations = generate_locations(city, num)
                if locations:
                    filename = save_to_file(city, locations)
                    print(f"Saved to: {filename}")
                    
                    # Option to open in browser
                    open_browser = input("Open first location in browser? (y/n): ").lower()
                    if open_browser == 'y':
                        webbrowser.open(locations[0])
            else:
                print(f"City '{city}' not found!")
        
        elif choice == '3':
            print("\nEnter cities in format: CityName,NumberOfLocations")
            print("Example: Tokyo,30")
            print("Type 'done' when finished\n")
            
            cities_to_generate = {}
            while True:
                entry = input("City,Number: ").strip()
                if entry.lower() == 'done':
                    break
                
                try:
                    city, num = entry.split(',')
                    city = city.strip()
                    num = int(num.strip())
                    
                    if city in CITY_COORDINATES:
                        if 1 <= num <= 50:
                            cities_to_generate[city] = num
                            print(f"Added {city} ({num} locations)")
                        else:
                            print("Number must be 1-50")
                    else:
                        print(f"City '{city}' not found!")
                except ValueError:
                    print("Invalid format! Use: CityName,Number")
            
            if cities_to_generate:
                generate_multiple_cities(cities_to_generate)
        
        elif choice == '4':
            file_path = input("Enter path to city list file: ").strip()
            batch_generate_from_list(file_path)
        
        elif choice == '5':
            print(f"\nDatabase Statistics:")
            print(f" Total cities: {len(CITY_COORDINATES)}")
            print(f"\nSample cities:")
            for i, city in enumerate(sorted(CITY_COORDINATES.keys())[:10000000], 1):
                lat, lon = CITY_COORDINATES[city]
                print(f"   {i:2}. {city:20} ({lat:.4f}, {lon:.4f})")
            print(f"   ... and {len(CITY_COORDINATES)-20} more")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()