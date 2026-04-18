import random
import math
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import webbrowser
import time
import pyautogui
import urllib.request
import json

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def parse_coords(url):
    try:
        part = url.split("@")[1]
        coords = part.split(",")
        return float(coords[0]), float(coords[1])
    except:
        return None


def get_popular_areas():
    """Return coordinates that definitely have Street View"""
    popular_spots = [
        # Cords generated with ChatGPT
        # EUROPE (100+ locations)
        (48.8584, 2.2945),   # Eiffel Tower, Paris
        (48.8606, 2.3376),   # Louvre Museum, Paris
        (48.8530, 2.3499),   # Notre-Dame, Paris
        (48.8742, 2.2950),   # Arc de Triomphe, Paris
        (48.8867, 2.3431),   # Montmartre, Paris
        (51.5074, -0.1278),  # London
        (51.5010, -0.1423),  # Buckingham Palace, London
        (51.5085, -0.0762),  # Tower of London
        (51.5055, -0.0753),  # Tower Bridge, London
        (51.5116, -0.1160),  # The Strand, London
        (41.9028, 12.4964),  # Rome
        (41.8902, 12.4922),  # Colosseum, Rome
        (41.9025, 12.4534),  # Vatican City
        (41.9009, 12.4833),  # Trevi Fountain, Rome
        (43.7696, 11.2558),  # Florence
        (43.7731, 11.2562),  # Florence Duomo
        (45.4408, 12.3155),  # Venice
        (45.4335, 12.3402),  # St. Mark's Square, Venice
        (40.8518, 14.2681),  # Naples
        (44.4949, 11.3426),  # Bologna
        (52.5200, 13.4050),  # Berlin
        (52.5163, 13.3777),  # Brandenburg Gate, Berlin
        (52.5206, 13.4095),  # Berlin Cathedral
        (52.5075, 13.1447),  # Charlottenburg Palace
        (48.1351, 11.5820),  # Munich
        (50.1109, 8.6821),   # Frankfurt
        (53.5511, 9.9937),   # Hamburg
        (50.9375, 6.9603),   # Cologne Cathedral
        (51.1657, 10.4515),  # Berlin (central Germany)
        (40.4168, -3.7038),  # Madrid
        (41.3851, 2.1734),   # Barcelona
        (39.4699, -0.3763),  # Valencia
        (37.3891, -5.9845),  # Seville
        (36.7213, -4.4216),  # Malaga
        (43.3623, -8.4115),  # A Coruña
        (52.3731, 4.8922),   # Amsterdam
        (51.9244, 4.4777),   # Rotterdam
        (52.0907, 5.1214),   # Utrecht
        (50.8467, 4.3525),   # Brussels
        (51.2194, 4.4025),   # Antwerp
        (48.2082, 16.3738),  # Vienna
        (48.2100, 16.3634),  # Schönbrunn Palace
        (48.3069, 14.2858),  # Linz
        (50.0755, 14.4378),  # Prague
        (49.1951, 16.6068),  # Brno
        (47.4979, 19.0402),  # Budapest
        (46.2548, 20.1485),  # Szeged
        (50.0647, 19.9450),  # Krakow
        (52.2297, 21.0122),  # Warsaw
        (51.1079, 17.0385),  # Wroclaw
        (54.3520, 18.6466),  # Gdansk
        (59.3293, 18.0686),  # Stockholm
        (57.7089, 11.9746),  # Gothenburg
        (55.6761, 12.5683),  # Copenhagen
        (56.2639, 9.5018),   # Silkeborg, Denmark
        (59.9139, 10.7522),  # Oslo
        (60.3913, 5.3228),   # Bergen, Norway
        (64.1466, -21.9426), # Reykjavik, Iceland
        (60.1699, 24.9384),  # Helsinki
        (59.4370, 24.7536),  # Tallinn
        (56.9496, 24.1052),  # Riga
        (54.6872, 25.2797),  # Vilnius
        (53.8932, 27.5478),  # Minsk
        (50.4501, 30.5234),  # Kyiv
        (46.4825, 30.7233),  # Odesa
        (44.4268, 26.1025),  # Bucharest
        (42.6977, 23.3219),  # Sofia
        (41.9973, 21.4280),  # Skopje
        (42.6629, 21.1655),  # Pristina
        (41.3275, 19.8187),  # Tirana
        (42.6507, 18.0944),  # Dubrovnik, Croatia
        (43.5081, 16.4402),  # Split, Croatia
        (43.8563, 18.4131),  # Sarajevo
        (44.7866, 20.4489),  # Belgrade
        (45.2671, 19.8335),  # Novi Sad
        (46.0569, 14.5058),  # Ljubljana
        (48.1486, 17.1077),  # Bratislava
        (47.1625, 27.5886),  # Iasi, Romania
        (45.7489, 21.2087),  # Timisoara, Romania
        (46.7712, 23.6236),  # Cluj-Napoca, Romania
        (47.0269, 28.8415),  # Chisinau, Moldova
        (41.9028, 12.4964),  # Rome (duplicate for coverage)
        
        # NORTH AMERICA (80+ locations)
        (40.7128, -74.0060),  # NYC
        (40.7580, -73.9855),  # Times Square
        (40.7489, -73.9680),  # Empire State Building
        (40.6892, -74.0445),  # Statue of Liberty
        (34.0522, -118.2437), # LA
        (34.0195, -118.4912), # Santa Monica
        (34.1016, -118.3407), # Hollywood
        (41.8781, -87.6298),  # Chicago
        (41.8929, -87.6352),  # Navy Pier, Chicago
        (37.7749, -122.4194), # San Francisco
        (37.8085, -122.4183), # Golden Gate Bridge
        (37.7937, -122.4030), # Alcatraz
        (47.6062, -122.3321), # Seattle
        (47.6195, -122.3488), # Space Needle
        (42.3601, -71.0589),  # Boston
        (38.9072, -77.0369),  # Washington DC
        (38.8895, -77.0353),  # White House
        (38.8977, -77.0365),  # National Mall
        (39.9526, -75.1652),  # Philadelphia
        (39.7439, -105.0201), # Denver
        (33.7490, -84.3880),  # Atlanta
        (25.7617, -80.1918),  # Miami
        (29.7604, -95.3698),  # Houston
        (32.7767, -96.7970),  # Dallas
        (30.2672, -97.7431),  # Austin
        (33.4484, -112.0740), # Phoenix
        (36.1699, -115.1398), # Las Vegas
        (32.7157, -117.1611), # San Diego
        (45.5152, -122.6784), # Portland
        (37.3382, -121.8863), # San Jose
        (38.6270, -90.1994),  # St. Louis
        (39.7684, -86.1581),  # Indianapolis
        (35.2271, -80.8431),  # Charlotte
        (39.9612, -82.9988),  # Columbus
        (42.3314, -83.0458),  # Detroit
        (43.6519, -79.3832),  # Toronto
        (45.5017, -73.5673),  # Montreal
        (49.2827, -123.1207), # Vancouver
        (51.0447, -114.0719), # Calgary
        (53.5461, -113.4938), # Edmonton
        (49.8951, -97.1384),  # Winnipeg
        (45.4215, -75.6972),  # Ottawa
        (46.8139, -71.2080),  # Quebec City
        (44.6488, -63.5752),  # Halifax
        (47.5596, -52.7126),  # St. John's
        (60.4720, -135.0655), # Whitehorse
        (68.3607, -133.7230), # Inuvik
        
        # SOUTH AMERICA (40+ locations)
        (-23.5505, -46.6333), # Sao Paulo
        (-23.5882, -46.6567), # Ibirapuera Park, Sao Paulo
        (-22.9068, -43.1729), # Rio de Janeiro
        (-22.9519, -43.2106), # Christ the Redeemer
        (-12.9714, -38.5014), # Salvador
        (-8.0543, -34.8813),  # Recife
        (-15.7939, -47.8828), # Brasilia
        (-30.0346, -51.2177), # Porto Alegre
        (-25.4284, -49.2733), # Curitiba
        (-3.7172, -38.5432),  # Fortaleza
        (-34.6037, -58.3816), # Buenos Aires
        (-34.6131, -58.3772), # La Boca, Buenos Aires
        (-31.4201, -64.1888), # Cordoba, Argentina
        (-32.9468, -60.6393), # Rosario, Argentina
        (-33.0472, -71.6127), # Valparaiso, Chile
        (-33.4489, -70.6693), # Santiago, Chile
        (-36.8270, -73.0503), # Concepcion, Chile
        (-4.4419, -81.2745),  # Piura, Peru
        (-12.0464, -77.0428), # Lima, Peru
        (-13.5319, -71.9675), # Cusco, Peru
        (4.7110, -74.0721),   # Bogota
        (6.2442, -75.5812),   # Medellin
        (3.4516, -76.5320),   # Cali, Colombia
        (10.3910, -75.4794),  # Cartagena, Colombia
        (-2.1199, -79.9230),  # Guayaquil, Ecuador
        (-0.1807, -78.4678),  # Quito, Ecuador
        (10.4806, -66.9036),  # Caracas, Venezuela
        (8.5376, -71.3700),   # Merida, Venezuela
        (5.0836, -55.6256),   # Paramaribo, Suriname
        (6.8013, -58.1550),   # Georgetown, Guyana
        (-25.9667, -57.5667), # Asuncion, Paraguay
        (-34.9011, -56.1645), # Montevideo, Uruguay
        
        # ASIA (120+ locations)
        (35.6895, 139.6917),  # Tokyo
        (35.6586, 139.7454),  # Tokyo Tower
        (35.7140, 139.7963),  # Skytree, Tokyo
        (34.6937, 135.5023),  # Osaka
        (35.0116, 135.7680),  # Kyoto
        (35.1815, 136.9066),  # Nagoya
        (43.0618, 141.3545),  # Sapporo
        (33.5904, 130.4017),  # Fukuoka
        (34.3853, 132.4553),  # Hiroshima
        (31.2304, 121.4737),  # Shanghai
        (39.9042, 116.4074),  # Beijing
        (39.9040, 116.3914),  # Forbidden City
        (40.4312, 116.5704),  # Great Wall (Badaling)
        (23.1291, 113.2644),  # Guangzhou
        (22.5431, 114.0579),  # Shenzhen
        (30.5728, 104.0668),  # Chengdu
        (34.3416, 108.9402),  # Xi'an
        (36.0986, 103.7180),  # Lanzhou
        (29.5630, 106.5516),  # Chongqing
        (32.0603, 118.7781),  # Nanjing
        (36.6512, 117.1201),  # Jinan
        (38.9048, 121.6019),  # Dalian
        (22.3193, 114.1694),  # Hong Kong
        (22.1588, 113.5694),  # Macau
        (25.0330, 121.5654),  # Taipei
        (37.5665, 126.9780),  # Seoul
        (37.5512, 126.9882),  # Myeongdong, Seoul
        (35.1796, 129.0756),  # Busan
        (37.4563, 126.7052),  # Incheon
        (35.8562, 128.6087),  # Daegu
        (28.6139, 77.2090),   # New Delhi
        (28.6328, 77.2196),   # India Gate, Delhi
        (19.0760, 72.8777),   # Mumbai
        (22.5726, 88.3639),   # Kolkata
        (12.9716, 77.5946),   # Bangalore
        (13.0827, 80.2707),   # Chennai
        (17.3850, 78.4867),   # Hyderabad
        (23.0225, 72.5714),   # Ahmedabad
        (26.9124, 75.7873),   # Jaipur
        (1.3521, 103.8198),   # Singapore
        (3.1390, 101.6869),   # Kuala Lumpur
        (5.4149, 100.3288),   # George Town, Malaysia
        (6.1239, 100.3678),   # Alor Setar, Malaysia
        (13.7367, 100.5231),  # Bangkok
        (18.7883, 98.9853),   # Chiang Mai
        (7.9519, 98.3381),    # Phuket
        (16.4330, 102.8330),  # Khon Kaen
        (10.8231, 106.6297),  # Ho Chi Minh City
        (21.0285, 105.8542),  # Hanoi
        (16.0544, 108.2022),  # Da Nang
        (14.0583, 108.2772),  # Pleiku, Vietnam
        (19.6765, 101.1834),  # Luang Prabang, Laos
        (11.5564, 104.9282),  # Phnom Penh
        (14.6760, 104.5206),  # Siem Reap (Angkor Wat)
        (16.8409, 96.1735),   # Yangon, Myanmar
        (27.7172, 85.3240),   # Kathmandu, Nepal
        (27.4698, 89.6383),   # Thimphu, Bhutan
        (23.8103, 90.4125),   # Dhaka, Bangladesh
        (6.9271, 79.8612),    # Colombo, Sri Lanka
        (4.1755, 73.5093),    # Male, Maldives
        (33.6844, 73.0479),   # Islamabad, Pakistan
        (31.5497, 74.3436),   # Lahore, Pakistan
        (24.8607, 67.0011),   # Karachi, Pakistan
        (51.1796, 71.4475),   # Astana, Kazakhstan
        (43.2383, 76.9457),   # Almaty, Kazakhstan
        (39.9040, 66.2624),   # Samarkand, Uzbekistan
        (41.3111, 69.2797),   # Tashkent, Uzbekistan
        (37.9409, 58.3771),   # Ashgabat, Turkmenistan
        (40.3926, 49.8814),   # Baku, Azerbaijan
        (41.6938, 44.8015),   # Tbilisi, Georgia
        (40.1774, 44.5125),   # Yerevan, Armenia
        
        # MIDDLE EAST (30+ locations)
        (25.2048, 55.2708),   # Dubai
        (25.1972, 55.2744),   # Burj Khalifa
        (24.4539, 54.3773),   # Abu Dhabi
        (26.2285, 50.5869),   # Manama, Bahrain
        (29.3759, 47.9774),   # Kuwait City
        (23.5880, 58.3829),   # Muscat, Oman
        (25.2854, 51.5310),   # Doha, Qatar
        (24.7136, 46.6753),   # Riyadh, Saudi Arabia
        (21.4225, 39.8262),   # Mecca, Saudi Arabia
        (24.5247, 39.5692),   # Medina, Saudi Arabia
        (31.6295, 74.8777),   # Lahore (listed earlier)
        (31.5204, 74.3587),   # Lahore Fort
        (33.6844, 73.0479),   # Islamabad
        (32.0853, 34.7818),   # Tel Aviv
        (31.7683, 35.2137),   # Jerusalem
        (32.7940, 34.9896),   # Haifa
        (31.2456, 34.7908),   # Beersheba
        (29.5577, 34.9519),   # Eilat
        (33.5138, 36.2765),   # Damascus, Syria
        (33.8938, 35.5018),   # Beirut, Lebanon
        (31.9539, 35.9106),   # Amman, Jordan
        (29.5324, 35.0065),   # Aqaba, Jordan
        (30.0444, 31.2357),   # Cairo
        (31.2001, 29.9187),   # Alexandria
        (26.8206, 30.8025),   # Luxor
        (24.0889, 32.8998),   # Aswan
        (32.8872, 13.1913),   # Tripoli, Libya
        (36.8065, 10.1815),   # Tunis, Tunisia
        (33.5731, -7.5898),   # Casablanca
        (34.0209, -6.8416),   # Rabat, Morocco
        (31.6295, -7.9811),   # Marrakech
        (35.7595, -5.8340),   # Tangier, Morocco
        
        # AFRICA (60+ locations)
        (-33.9249, 18.4241),  # Cape Town
        (-33.9245, 18.4248),  # Table Mountain
        (-26.1952, 28.0344),  # Johannesburg
        (-29.8587, 31.0218),  # Durban
        (-25.7479, 28.2293),  # Pretoria
        (-33.9069, 18.4172),  # Cape Town waterfront
        (28.0474, -15.4369),  # Las Palmas, Canary Islands
        (28.1235, -15.4362),  # Gran Canaria
        (28.4636, -16.2518),  # Tenerife
        (14.5995, -15.4690),  # Dakar, Senegal
        (9.5350, -13.6787),   # Conakry, Guinea
        (6.3176, -10.8041),   # Monrovia, Liberia
        (5.3599, -4.0082),    # Abidjan, Ivory Coast
        (5.6037, -0.1870),    # Accra, Ghana
        (6.4402, 3.3944),     # Lagos, Nigeria
        (9.0765, 7.3986),     # Abuja, Nigeria
        (4.0511, 9.7679),     # Douala, Cameroon
        (3.8480, 11.5021),    # Yaounde, Cameroon
        (0.3476, 32.5825),    # Kampala, Uganda
        (-1.2864, 36.8172),   # Nairobi, Kenya
        (-4.0435, 39.6682),   # Mombasa, Kenya
        (-6.7924, 39.2083),   # Dar es Salaam, Tanzania
        (-3.3614, 36.6795),   # Arusha, Tanzania
        (-1.9403, 29.8739),   # Kigali, Rwanda
        (-3.3891, 29.9288),   # Bujumbura, Burundi
        (11.5634, 13.1665),   # N'Djamena, Chad
        (12.3692, -1.5255),   # Ouagadougou, Burkina Faso
        (12.6392, -8.0029),   # Bamako, Mali
        (14.6937, -17.4441),  # Dakar (Senegal)
        (18.5424, -72.2949),  # Port-au-Prince, Haiti
        (18.4668, -69.9401),  # Santo Domingo, DR
        (23.1136, -82.3666),  # Havana, Cuba
        (19.4326, -99.1332),  # Mexico City
        (20.6597, -103.3496), # Guadalajara, Mexico
        (25.6866, -100.3161), # Monterrey, Mexico
        (20.9668, -89.6215),  # Merida, Mexico
        (21.1619, -86.8515),  # Cancun, Mexico
        (14.6349, -90.5069),  # Guatemala City
        (13.6929, -89.2182),  # San Salvador
        (14.0650, -87.1715),  # Tegucigalpa, Honduras
        (12.1142, -86.2367),  # Managua, Nicaragua
        (9.9281, -84.0907),   # San Jose, Costa Rica
        (8.9824, -79.5199),   # Panama City
        (18.4861, -69.9312),  # Santo Domingo
        (18.4655, -66.1057),  # San Juan, Puerto Rico
        
        # OCEANIA (40+ locations)
        (-33.8688, 151.2093), # Sydney
        (-33.8568, 151.2153), # Sydney Opera House
        (-33.8474, 151.2100), # Sydney Harbour Bridge
        (-37.8136, 144.9631), # Melbourne
        (-37.8175, 144.9672), # Flinders Street Station
        (-27.4698, 153.0251), # Brisbane
        (-31.9505, 115.8605), # Perth
        (-34.9285, 138.6007), # Adelaide
        (-35.2809, 149.1300), # Canberra
        (-12.4634, 130.8456), # Darwin
        (-42.8821, 147.3251), # Hobart
        (-16.9186, 145.7781), # Cairns
        (-19.2576, 146.8239), # Townsville
        (-38.1486, 144.3613), # Geelong
        (-36.8485, 174.7633), # Auckland
        (-41.2865, 174.7762), # Wellington
        (-43.5321, 172.6362), # Christchurch
        (-45.8788, 170.5028), # Dunedin
        (-37.6878, 176.1651), # Tauranga
        (-39.4928, 176.9120), # Napier
        (-36.7811, 174.7521), # North Shore, Auckland
        (-17.7134, 177.4543), # Nadi, Fiji
        (-18.1428, 178.4319), # Suva, Fiji
        (-21.1368, -175.2018), # Nuku'alofa, Tonga
        (-17.7321, 168.3171), # Port Vila, Vanuatu
        (-9.4456, 159.9724),  # Honiara, Solomon Islands
        (1.3532, 173.0368),   # Tarawa, Kiribati
        (7.4872, 134.6255),   # Ngerulmud, Palau
        (6.9219, 158.2152),   # Palikir, Micronesia
        (-8.5167, 179.2167),  # Funafuti, Tuvalu
        (-29.0551, 167.9607), # Kingston, Norfolk Island
        (-25.0669, -130.1008), # Adamstown, Pitcairn
        (9.3653, 167.7412),   # Majuro, Marshall Islands
        (-17.5334, -149.5667), # Papeete, Tahiti
        (-22.2684, 166.4448), # Noumea, New Caledonia
        (-20.2312, 57.4869),  # Port Louis, Mauritius
        (-4.6191, 55.4465),   # Victoria, Seychelles
        (-20.1609, 28.5784),  # Bulawayo, Zimbabwe (for coverage)
    ]
    
    unique_spots = []
    seen = set()
    for spot in popular_spots:
        key = f"{spot[0]:.2f},{spot[1]:.2f}"
        if key not in seen:
            seen.add(key)
            unique_spots.append(spot)
    
    while len(unique_spots) < 500:
        base_lat, base_lon = random.choice(popular_spots)
        # Add small random offset (within ~50km)
        lat_offset = random.uniform(-0.5, 0.5)
        lon_offset = random.uniform(-0.5, 0.5)
        new_lat = base_lat + lat_offset
        new_lon = base_lon + lon_offset
        new_key = f"{new_lat:.2f},{new_lon:.2f}"
        if new_key not in seen:
            seen.add(new_key)
            unique_spots.append((new_lat, new_lon))
    
    return unique_spots[:500]

class GeoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ngav Guessr")
        self.root.configure(bg="#121212")

        self.locations = []
        self.current = None

        self.round = 1
        self.max_rounds = 5
        self.total_score = 0

        self.mode_frame()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def label(self, text, size=12):
        return tk.Label(self.root, text=text,
                        font=("Arial", size),
                        bg="#121212", fg="white")

    def button(self, text, cmd):
        return tk.Button(self.root, text=text, command=cmd,
                         bg="#1f1f1f", fg="white",
                         relief="flat", padx=10, pady=5)

    def mode_frame(self):
        self.clear()

        self.label("Select Mode", 18).pack(pady=20)
        self.button("World", self.full_world).pack(pady=10)
        self.button("Custom Map", self.load_file).pack(pady=10)

    def full_world(self):
        rounds_input = simpledialog.askinteger(
            "Number of Rounds",
            f"How many rounds do you want to play?\n(Enter a number between 1 and {len(get_popular_areas())})",
            minvalue=1,
            maxvalue=len(get_popular_areas()),
            parent=self.root
        )
        
        if rounds_input is None:
            self.mode_frame()
            return
        
        self.max_rounds = rounds_input
        
        all_locations = get_popular_areas()
        
        selected_spots = random.sample(all_locations, self.max_rounds)
        
        self.locations = []
        for lat, lon in selected_spots:
            self.locations.append({
                "lat": lat,
                "lon": lon,
                "url": f"https://www.google.com/maps?q=&layer=c&cbll={lat},{lon}"
            })

        self.start_game()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        self.locations = []

        with open(file_path, "r") as f:
            for line in f:
                url = line.strip()
                coords = parse_coords(url)

                if coords:
                    lat, lon = coords
                    self.locations.append({
                        "lat": lat,
                        "lon": lon,
                        "url": url
                    })

        if not self.locations:
            messagebox.showerror("Error", "No valid locations found")
            return

        self.max_rounds = len(self.locations)
        self.start_game()

    def start_game(self):
        self.round = 1
        self.total_score = 0

        if self.max_rounds == 0:
            messagebox.showerror("Error", "No locations")
            return
        
        random.shuffle(self.locations)

        self.next_round()

    def next_round(self):
        if self.round > self.max_rounds:
            # Calculate percentage score and display result messsages
            max_possible_score = self.max_rounds * 5000
            percentage = (self.total_score / max_possible_score) * 100
            
            result_msg = f"Final Score: {self.total_score}/{max_possible_score}\n"
            result_msg += f"Accuracy: {percentage:.1f}%\n\n"
            
            if percentage >= 90:
                result_msg += "Perfect! You're a geography master!"
            elif percentage >= 70:
                result_msg += "Great job!"
            elif percentage >= 50:
                result_msg += "Good work!"
            elif percentage >= 30:
                result_msg += "Keep practicing!"
            else:
                result_msg += "Try again to improve your geography skills!"
            
            messagebox.showinfo("Game Over", result_msg)
            self.mode_frame()
            return

        self.clear()

        self.current = self.locations[self.round - 1]

        self.label(f"Round {self.round}/{self.max_rounds}", 14).pack(pady=5)
        self.label(f"Score: {self.total_score}", 12).pack(pady=5)

        self.button("Open Street View", self.open_location).pack(pady=10)
        self.button("Open Map", self.open_map).pack(pady=5)

        self.guess_entry = tk.Entry(self.root,
                                    bg="#1f1f1f",
                                    fg="white",
                                    insertbackground="white",
                                    width=30)
        self.guess_entry.pack(pady=10)
        self.guess_entry.insert(0, "")

        self.button("Submit Guess", self.check_guess).pack(pady=10)

    def open_location(self):
        lat = self.current["lat"]
        lon = self.current["lon"]

        url = f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}"
        webbrowser.open(url)

        time.sleep(2)

        pyautogui.press("f11")

    def open_map(self):
        webbrowser.open(
            "https://www.google.com/maps/@45.2029598,22.9689072,3483229m/data=!3m1!1e3"
        )

    def check_guess(self):
        try:
            guess_text = self.guess_entry.get().strip().lower()
            
            if guess_text == "no":
                result = messagebox.askyesno("Skip Location", 
                                            "This location will be skipped and not count toward your score.\n\n"
                                            "Do you want to skip it?")
                if result:
                    self.round += 1
                    self.next_round()
                return
            
            parts = guess_text.split(",")
            if len(parts) != 2:
                raise ValueError
            g_lat = float(parts[0].strip())
            g_lon = float(parts[1].strip())
            
            if not (-90 <= g_lat <= 90):
                messagebox.showerror("Error", "Latitude must be between -90 and 90")
                return
            if not (-180 <= g_lon <= 180):
                messagebox.showerror("Error", "Longitude must be between -180 and 180")
                return
                
        except ValueError:
            messagebox.showerror("Error", "Invalid format!\n\n"
                                          "Use: latitude, longitude\n"
                                          "Example: 48.8584, 2.2945\n\n"
                                          "Or type 'no' to skip this location")
            return

        r_lat = self.current["lat"]
        r_lon = self.current["lon"]

        dist = haversine(g_lat, g_lon, r_lat, r_lon)
        score = max(0, int(5000 - dist * 10))

        self.total_score += score

        messagebox.showinfo("Result",
                            f"Actual location: {r_lat:.4f}, {r_lon:.4f}\n"
                            f"Your guess: {g_lat:.4f}, {g_lon:.4f}\n"
                            f"Distance: {dist:.2f} km\n"
                            f"Score: {score} points")

        self.round += 1
        self.next_round()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("420x500")
    app = GeoGame(root)
    root.mainloop()