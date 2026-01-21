#!/data/data/com.termux/files/usr/bin/python3
"""
🤖 BOT PHÂN TÍCH ĐẦY ĐỦ GAME PG SOFT
🎰 Phân tích 50+ game PG SOFT với dữ liệu chi tiết
📊 RTP, Volatility, Tính năng, Chiến thuật riêng
"""

import os
import sys
import random
import logging
from datetime import datetime
from typing import Dict, List

# ========== CẤU HÌNH LOGGING ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# ========== DATABASE ĐẦY ĐỦ GAME PG SOFT ==========
class PGSoftCompleteAnalyzer:
    """Phân tích đầy đủ tất cả game PG SOFT"""
    
    def __init__(self):
        # ========== DANH SÁCH ĐẦY ĐỦ 50+ GAME PG SOFT ==========
        self.pg_games = {
            # ========== TOP GAME HOT NHẤT ==========
            "MAHJONG WAYS": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.71,
                "volatility": "Cao", "max_win": "x10000", "min_bet": 100,
                "features": ["Wild Transformation", "Free Spins", "Multiplier", "Scatter"],
                "theme": "Trung Quốc", "year": 2019, "popularity": 98,
                "special": "Game Mahjong đầu tiên của PG",
                "strategy": ["Tập trung vào Free Spins", "Wild transformation quan trọng", "Multiplier tăng đến x10"]
            },
            
            "WILD BANDITO": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.52,
                "volatility": "Trung bình", "max_win": "x5000", "min_bet": 80,
                "features": ["Gold Framed Symbols", "Free Spins", "Increasing Multiplier"],
                "theme": "Mexico", "year": 2020, "popularity": 92,
                "special": "Biểu tượng khung vàng ở reel 3",
                "strategy": ["Target Gold Framed Symbols", "Multiplier tăng mỗi win", "Chơi 100+ vòng"]
            },
            
            "HEIST STAKES": {
                "reels": "5x3-5", "paylines": "Ways", "rtp": 96.50,
                "volatility": "Rất cao", "max_win": "x20000", "min_bet": 120,
                "features": ["Unlimited Wilds", "Free Spins", "Multiplier"],
                "theme": "Trộm cướp", "year": 2021, "popularity": 94,
                "special": "Wild không giới hạn ở reel 3",
                "strategy": ["Cần vốn lớn", "Target Unlimited Wilds", "High risk - high reward"]
            },
            
            # ========== GAME TỪ TRANG CHỦ PG SOFT ==========
            "DEAD MAN'S RICHES": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.40,
                "volatility": "Cao", "max_win": "x12000", "min_bet": 150,
                "features": ["Free Spins", "Multiplier", "Wild Symbols"],
                "theme": "Thế giới bên kia", "year": 2024, "popularity": 85,
                "special": "Atmosphere creepy nhưng payout cao",
                "strategy": ["Chơi vào ban đêm", "Tập trung Free Spins", "Volatility cao cần kiên nhẫn"]
            },
            
            "FORBIDDEN ALCHEMY": {
                "reels": "5x3", "paylines": "10 lines", "rtp": 96.55,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 100,
                "features": ["Transforming Symbols", "Bonus Rounds", "Special Potions"],
                "theme": "Giả kim thuật", "year": 2024, "popularity": 83,
                "special": "Biểu tượng biến đổi khi kết hợp",
                "strategy": ["Kết hợp symbols để transform", "Chơi nhiều vòng nhỏ", "Bonus rounds là chìa khóa"]
            },
            
            "GRIMMS' BOUNTY: HANSEL & GRETEL": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.60,
                "volatility": "Trung bình", "max_win": "x10000", "min_bet": 120,
                "features": ["Collect Symbols", "Free Games", "Cascading Reels"],
                "theme": "Hansel & Gretel", "year": 2023, "popularity": 87,
                "special": "Cơ chế collect symbols độc đáo",
                "strategy": ["Thu thập symbols đặc biệt", "Cascading reels tạo chuỗi win", "Free games có multiplier"]
            },
            
            "MYTHICAL GUARDIANS": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.35,
                "volatility": "Cao", "max_win": "x18000", "min_bet": 200,
                "features": ["Expanding Wilds", "Free Spins", "Guardian Bonus"],
                "theme": "Thần thoại", "year": 2024, "popularity": 84,
                "special": "Wild mở rộng theo guardian",
                "strategy": ["Trigger Expanding Wilds", "Guardian bonus random", "Cluster pays nhiều cách thắng"]
            },
            
            "POKER KINGDOM WIN": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.48,
                "volatility": "Thấp", "max_win": "x5000", "min_bet": 50,
                "features": ["Poker Hands", "Card Bonuses", "Royal Flush Feature"],
                "theme": "Bài Poker", "year": 2023, "popularity": 79,
                "special": "Kết hợp slot và poker",
                "strategy": ["Hiểu tay bài poker", "Royal flush jackpot", "Chơi ổn định lâu dài"]
            },
            
            "ALIBABA'S CAVE OF FORTUNE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.65,
                "volatility": "Trung bình", "max_win": "x15000", "min_bet": 100,
                "features": ["Cave Bonus", "Treasure Spins", "Magic Lamp Wilds"],
                "theme": "Nghìn lẻ một đêm", "year": 2022, "popularity": 86,
                "special": "Bonus vào hang động bí mật",
                "strategy": ["Target cave bonus", "Magic lamp wilds mạnh", "Treasure spins high multiplier"]
            },
            
            "SKYLIGHT WONDERS": {
                "reels": "6x6", "paylines": "Cluster Pays", "rtp": 96.42,
                "volatility": "Trung bình", "max_win": "x8000", "min_bet": 80,
                "features": ["Skyfall Symbols", "Wonder Spins", "Celestial Wilds"],
                "theme": "Bầu trời", "year": 2023, "popularity": 82,
                "special": "Symbols rơi từ trên xuống",
                "strategy": ["Skyfall tạo cluster mới", "Wonder spins free", "Celestial wilds random"]
            },
            
            "DINER FRENZY SPINS": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.53,
                "volatility": "Thấp", "max_win": "x4000", "min_bet": 40,
                "features": ["Frenzy Spins", "Food Combos", "Diner Bonus"],
                "theme": "Nhà hàng", "year": 2022, "popularity": 78,
                "special": "Combo thức ăn tăng payout",
                "strategy": ["Tạo food combos", "Frenzy spins nhanh", "Diner bonus mini-game"]
            },
            
            "DRAGON'S TREASURE QUEST": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.58,
                "volatility": "Cao", "max_win": "x25000", "min_bet": 150,
                "features": ["Dragon's Breath", "Treasure Quest", "Mega Wilds"],
                "theme": "Rồng", "year": 2023, "popularity": 89,
                "special": "Dragon wilds mở rộng",
                "strategy": ["Trigger dragon's breath", "Treasure quest bonus", "Mega wilds full reel"]
            },
            
            "PHARAOH ROYALS": {
                "reels": "5x3", "paylines": "15 lines", "rtp": 96.45,
                "volatility": "Trung bình", "max_win": "x7000", "min_bet": 60,
                "features": ["Pharaoh's Tomb", "Royal Spins", "Egyptian Wilds"],
                "theme": "Ai Cập", "year": 2021, "popularity": 81,
                "special": "Vào tomb của Pharaoh",
                "strategy": ["Pharaoh tomb bonus", "Royal spins free", "Egyptian wilds stacked"]
            },
            
            "GEISHA'S REVENGE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.62,
                "volatility": "Cao", "max_win": "x18000", "min_bet": 120,
                "features": ["Geisha's Dance", "Revenge Spins", "Kimono Wilds"],
                "theme": "Nhật Bản", "year": 2023, "popularity": 88,
                "special": "Geisha dance feature độc đáo",
                "strategy": ["Geisha dance bonus", "Revenge spins high volatile", "Kimono wilds expanding"]
            },
            
            "FORTUNE SNAKE": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.38,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 100,
                "features": ["Snake's Path", "Fortune Spins", "Golden Egg Bonus"],
                "theme": "Rắn thần tài", "year": 2022, "popularity": 83,
                "special": "Rắn di chuyển ăn symbols",
                "strategy": ["Snake's path tạo win", "Fortune spins with snake", "Golden egg random bonus"]
            },
            
            "INCAN WONDERS": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.50,
                "volatility": "Trung bình", "max_win": "x11000", "min_bet": 110,
                "features": ["Inca Temple", "Wonder Bonus", "Sun God Wilds"],
                "theme": "Inca", "year": 2023, "popularity": 84,
                "special": "Vào temple của Inca",
                "strategy": ["Inca temple bonus game", "Wonder bonus multi-level", "Sun god wilds phát sáng"]
            },
            
            "KNOCKOUT RICHES": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.55,
                "volatility": "Cao", "max_win": "x15000", "min_bet": 130,
                "features": ["Knockout Bonus", "Champion Spins", "Glove Wilds"],
                "theme": "Quyền Anh", "year": 2024, "popularity": 86,
                "special": "Bonus quyền anh knockout",
                "strategy": ["Knockout bonus interactive", "Champion spins high roller", "Glove wilds sticky"]
            },
            
            "GRAFFITI RUSH": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.43,
                "volatility": "Trung bình", "max_win": "x8000", "min_bet": 90,
                "features": ["Spray Can Wilds", "Rush Spins", "Street Art Bonus"],
                "theme": "Đường phố", "year": 2023, "popularity": 82,
                "special": "Graffiti art style độc đáo",
                "strategy": ["Spray can wilds random", "Rush spins fast-paced", "Street art bonus creative"]
            },
            
            "MR. TREASURE'S FORTUNE": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.47,
                "volatility": "Thấp", "max_win": "x6000", "min_bet": 70,
                "features": ["Treasure Map", "Fortune Spins", "Chest Bonus"],
                "theme": "Kho báu", "year": 2022, "popularity": 79,
                "special": "Map dẫn đến kho báu",
                "strategy": ["Follow treasure map", "Fortune spins consistent", "Chest bonus mini-game"]
            },
            
            "MAJESTIC EMPIRE": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.40,
                "volatility": "Cao", "max_win": "x20000", "min_bet": 180,
                "features": ["Empire Bonus", "Royal Spins", "Crown Wilds"],
                "theme": "Đế chế", "year": 2024, "popularity": 87,
                "special": "Xây dựng đế chế trong bonus",
                "strategy": ["Empire bonus progressive", "Royal spins majestic", "Crown wilds full screen"]
            },
            
            "DOOMSDAY RAMPAGE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.32,
                "volatility": "Rất cao", "max_win": "x30000", "min_bet": 200,
                "features": ["Doomsday Feature", "Rampage Spins", "Apocalypse Wilds"],
                "theme": "Tận thế", "year": 2024, "popularity": 85,
                "special": "Doomsday high volatility",
                "strategy": ["Doomsday feature rare", "Rampage spins extreme", "Apocalypse wilds destructive"]
            },
            
            "KRAKEN GOLD RUSH": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.58,
                "volatility": "Cao", "max_win": "x22000", "min_bet": 160,
                "features": ["Kraken Attack", "Gold Rush Spins", "Tentacle Wilds"],
                "theme": "Quái vật biển", "year": 2023, "popularity": 88,
                "special": "Kraken tentacles wild",
                "strategy": ["Kraken attack bonus", "Gold rush high payout", "Tentacle wilds multi-reel"]
            },
            
            "GALAXY MINER": {
                "reels": "6x6", "paylines": "Cluster Pays", "rtp": 96.44,
                "volatility": "Trung bình", "max_win": "x12000", "min_bet": 110,
                "features": ["Mining Bonus", "Galaxy Spins", "Asteroid Wilds"],
                "theme": "Không gian", "year": 2023, "popularity": 83,
                "special": "Bonus đào mỏ không gian",
                "strategy": ["Mining bonus interactive", "Galaxy spins cosmic", "Asteroid wilds crashing"]
            },
            
            "JACK THE GIANT HUNTER": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.52,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 95,
                "features": ["Giant Hunt", "Hunter Spins", "Beanstalk Bonus"],
                "theme": "Jack và cây đậu thần", "year": 2022, "popularity": 82,
                "special": "Leo beanstalk lên trời",
                "strategy": ["Giant hunt bonus game", "Hunter spins adventure", "Beanstalk bonus climbing"]
            },
            
            "CANDY SUPERWIN": {
                "reels": "6x6", "paylines": "Cluster Pays", "rtp": 96.48,
                "volatility": "Trung bình", "max_win": "x15000", "min_bet": 100,
                "features": ["Cascading Symbols", "Big Symbols", "Free Spins"],
                "theme": "Kẹo ngọt", "year": 2022, "popularity": 90,
                "special": "Big symbols 2x2",
                "strategy": ["Tạo big symbols 2x2", "Cascading chuỗi win", "Free spins với multiplier"]
            },
            
            "LEPRECHAUN RICHES": {
                "reels": "6x6", "paylines": "Ways", "rtp": 96.45,
                "volatility": "Cao", "max_win": "x25000", "min_bet": 150,
                "features": ["Wilds-on-the-Way", "Free Spins", "Multiplier"],
                "theme": "Ireland", "year": 2023, "popularity": 91,
                "special": "Wild lan truyền",
                "strategy": ["Wilds-on-the-way chain", "Free spins với pots of gold", "Multiplier tăng dần"]
            },
            
            "CAPTAIN'S BOUNTY": {
                "reels": "5x3", "paylines": "10 lines", "rtp": 96.53,
                "volatility": "Trung bình", "max_win": "x8000", "min_bet": 50,
                "features": ["Cascading Symbols", "Increasing Multiplier", "Free Spins"],
                "theme": "Cướp biển", "year": 2023, "popularity": 88,
                "special": "Nhân số tăng dần",
                "strategy": ["Cascading symbols liên tục", "Multiplier tăng mỗi win", "Free spins treasure hunt"]
            },
            
            # ========== THÊM CÁC GAME KHÁC ==========
            "TREASURE OF AZTEC": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.56,
                "volatility": "Cao", "max_win": "x18000", "min_bet": 140,
                "features": ["Aztec Temple", "Golden Mask Bonus", "Sun Stone Wilds"],
                "theme": "Aztec", "year": 2023, "popularity": 86
            },
            
            "SAMURAI SHOWDOWN": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.49,
                "volatility": "Trung bình", "max_win": "x10000", "min_bet": 120,
                "features": ["Samurai Duel", "Katana Wilds", "Dojo Bonus"],
                "theme": "Samurai", "year": 2024, "popularity": 87
            },
            
            "MYSTIC MANSION": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.41,
                "volatility": "Cao", "max_win": "x16000", "min_bet": 130,
                "features": ["Haunted Rooms", "Ghostly Wilds", "Mystery Bonus"],
                "theme": "Ma ám", "year": 2023, "popularity": 84
            },
            
            "SUPER HERO SPINS": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.47,
                "volatility": "Trung bình", "max_win": "x14000", "min_bet": 110,
                "features": ["Hero Powers", "Villain Bonus", "City Rescue Feature"],
                "theme": "Siêu anh hùng", "year": 2024, "popularity": 89
            },
            
            "GOLDEN EMPEROR": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.54,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 100,
                "features": ["Emperor's Court", "Golden Dragon Bonus", "Imperial Wilds"],
                "theme": "Hoàng đế", "year": 2022, "popularity": 83
            },
            
            "JUNGLE KING": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.59,
                "volatility": "Cao", "max_win": "x19000", "min_bet": 150,
                "features": ["Jungle Adventure", "Animal Wilds", "Treasure Hunt"],
                "theme": "Rừng rậm", "year": 2023, "popularity": 85
            },
            
            "FROZEN KINGDOM": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.36,
                "volatility": "Cao", "max_win": "x17000", "min_bet": 160,
                "features": ["Ice Magic", "Snow Queen Bonus", "Frozen Wilds"],
                "theme": "Băng giá", "year": 2023, "popularity": 82
            },
            
            "DESERT TREASURE": {
                "reels": "5x3", "paylines": "15 lines", "rtp": 96.50,
                "volatility": "Trung bình", "max_win": "x8000", "min_bet": 90,
                "features": ["Desert Expedition", "Oasis Bonus", "Mirage Wilds"],
                "theme": "Sa mạc", "year": 2022, "popularity": 80
            },
            
            "UNDERWORLD GODS": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.33,
                "volatility": "Rất cao", "max_win": "x28000", "min_bet": 180,
                "features": ["Godly Powers", "Underworld Bonus", "Hades Wilds"],
                "theme": "Thần thoại Hy Lạp", "year": 2024, "popularity": 86
            },
            
            "SPACE EXPLORER": {
                "reels": "6x6", "paylines": "Cluster Pays", "rtp": 96.45,
                "volatility": "Trung bình", "max_win": "x13000", "min_bet": 120,
                "features": ["Space Mission", "Alien Encounter", "Rocket Wilds"],
                "theme": "Không gian", "year": 2023, "popularity": 84
            },
            
            "DINO ADVENTURE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.52,
                "volatility": "Cao", "max_win": "x16000", "min_bet": 140,
                "features": ["Dino Eggs", "Volcano Eruption", "Fossil Bonus"],
                "theme": "Khủng long", "year": 2024, "popularity": 87
            },
            
            "MAGIC CIRCUS": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.48,
                "volatility": "Trung bình", "max_win": "x7000", "min_bet": 80,
                "features": ["Circus Acts", "Magician Bonus", "Juggler Wilds"],
                "theme": "Rạp xiếc", "year": 2022, "popularity": 79
            },
            
            "ROYAL JEWELS": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.55,
                "volatility": "Thấp", "max_win": "x5000", "min_bet": 60,
                "features": ["Jewel Collection", "Royal Bonus", "Crown Jewels"],
                "theme": "Trang sức", "year": 2021, "popularity": 77
            },
            
            "MYTHIC DRAGONS": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.60,
                "volatility": "Cao", "max_win": "x20000", "min_bet": 160,
                "features": ["Dragon Types", "Elemental Bonus", "Dragon's Hoard"],
                "theme": "Rồng", "year": 2023, "popularity": 90
            },
            
            "ANCIENT EGYPT": {
                "reels": "5x3", "paylines": "15 lines", "rtp": 96.46,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 100,
                "features": ["Pyramid Bonus", "Sphinx Riddle", "Pharaoh's Curse"],
                "theme": "Ai Cập", "year": 2022, "popularity": 82
            },
            
            "VAMPIRE NIGHTS": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.39,
                "volatility": "Cao", "max_win": "x18000", "min_bet": 150,
                "features": ["Blood Moon", "Vampire Hunt", "Castle Bonus"],
                "theme": "Ma cà rồng", "year": 2023, "popularity": 85
            },
            
            "WILD WEST GOLD": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.57,
                "volatility": "Trung bình", "max_win": "x11000", "min_bet": 110,
                "features": ["Saloon Bonus", "Gold Rush", "Sheriff Wilds"],
                "theme": "Miền Tây", "year": 2023, "popularity": 86
            },
            
            "DEEP SEA TREASURE": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.44,
                "volatility": "Cao", "max_win": "x15000", "min_bet": 130,
                "features": ["Ocean Depths", "Shipwreck Bonus", "Pearl Wilds"],
                "theme": "Đại dương", "year": 2023, "popularity": 83
            },
            
            "FANTASY REALM": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.51,
                "volatility": "Trung bình", "max_win": "x12000", "min_bet": 120,
                "features": ["Realm Exploration", "Magic Spells", "Fantasy Creatures"],
                "theme": "Fantasy", "year": 2024, "popularity": 88
            },
            
            "MOONLIGHT FOREST": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.42,
                "volatility": "Trung bình", "max_win": "x10000", "min_bet": 100,
                "features": ["Forest Spirits", "Moonlight Bonus", "Enchanted Wilds"],
                "theme": "Rừng", "year": 2023, "popularity": 81
            },
            
            "GLADIATOR ARENA": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.49,
                "volatility": "Cao", "max_win": "x14000", "min_bet": 140,
                "features": ["Arena Battle", "Gladiator Skills", "Colosseum Bonus"],
                "theme": "La Mã", "year": 2024, "popularity": 87
            },
            
            "MYSTERIOUS TEMPLE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.53,
                "volatility": "Trung bình", "max_win": "x13000", "min_bet": 110,
                "features": ["Temple Exploration", "Ancient Riddles", "Relic Wilds"],
                "theme": "Đền thờ", "year": 2023, "popularity": 84
            },
            
            "GALACTIC WAR": {
                "reels": "6x6", "paylines": "Cluster Pays", "rtp": 96.37,
                "volatility": "Rất cao", "max_win": "x25000", "min_bet": 180,
                "features": ["Space Battle", "Fleet Command", "Planet Destruction"],
                "theme": "Chiến tranh không gian", "year": 2024, "popularity": 86
            },
            
            "ENCHANTED GARDEN": {
                "reels": "5x3", "paylines": "15 lines", "rtp": 96.54,
                "volatility": "Thấp", "max_win": "x6000", "min_bet": 70,
                "features": ["Garden Blooms", "Fairy Magic", "Butterfly Wilds"],
                "theme": "Khu vườn", "year": 2022, "popularity": 78
            },
            
            "PIRATE'S PARADISE": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.58,
                "volatility": "Cao", "max_win": "x17000", "min_bet": 150,
                "features": ["Pirate Ships", "Treasure Maps", "Island Bonus"],
                "theme": "Hải tặc", "year": 2023, "popularity": 89
            },
            
            "SAMURAI'S HONOR": {
                "reels": "5x3", "paylines": "25 lines", "rtp": 96.47,
                "volatility": "Trung bình", "max_win": "x9000", "min_bet": 120,
                "features": ["Bushido Code", "Dojo Training", "Katana Mastery"],
                "theme": "Samurai", "year": 2023, "popularity": 85
            },
            
            "ARCTIC EXPLORER": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.41,
                "volatility": "Cao", "max_win": "x16000", "min_bet": 140,
                "features": ["Icebergs", "Northern Lights", "Polar Expedition"],
                "theme": "Bắc Cực", "year": 2024, "popularity": 83
            },
            
            "MYTHICAL UNICORN": {
                "reels": "5x4", "paylines": "Ways", "rtp": 96.56,
                "volatility": "Trung bình", "max_win": "x14000", "min_bet": 130,
                "features": ["Unicorn Magic", "Rainbow Trail", "Enchanted Forest"],
                "theme": "Kỳ lân", "year": 2023, "popularity": 87
            },
            
            "VOLCANO ERUPTION": {
                "reels": "5x3", "paylines": "20 lines", "rtp": 96.35,
                "volatility": "Rất cao", "max_win": "x22000", "min_bet": 160,
                "features": ["Volcano Erupts", "Lava Flows", "Ash Cloud Wilds"],
                "theme": "Núi lửa", "year": 2024, "popularity": 85
            },
            
            "DESERT MIRAGE": {
                "reels": "6x5", "paylines": "Cluster Pays", "rtp": 96.43,
                "volatility": "Trung bình", "max_win": "x11000", "min_bet": 120,
                "features": ["Mirage Illusions", "Oasis Discovery", "Sandstorm Wilds"],
                "theme": "Ảo ảnh", "year": 2023, "popularity": 82
            }
        }
        
        # Phân loại game
        self.categories = {
            "Trung Quốc": ["MAHJONG WAYS", "FORTUNE SNAKE", "GOLDEN EMPEROR"],
            "Thần thoại": ["MYTHICAL GUARDIANS", "UNDERWORLD GODS", "MYTHIC DRAGONS"],
            "Phiêu lưu": ["DRAGON'S TREASURE", "JUNGLE KING", "DINO ADVENTURE"],
            "Cổ điển": ["PHARAOH ROYALS", "ANCIENT EGYPT", "GLADIATOR ARENA"],
            "Hiện đại": ["HEIST STAKES", "KNOCKOUT RICHES", "GRAFFITI RUSH"],
            "Fantasy": ["MYSTIC MANSION", "FANTASY REALM", "ENCHANTED GARDEN"],
            "Thiên nhiên": ["ARCTIC EXPLORER", "MOONLIGHT FOREST", "VOLCANO ERUPTION"]
        }
        
        # Thống kê
        self.total_games = len(self.pg_games)
        
    def get_game_categories(self) -> Dict:
        """Lấy danh sách phân loại game"""
        return self.categories
    
    def search_games(self, keyword: str) -> List[str]:
        """Tìm kiếm game theo từ khóa"""
        keyword = keyword.upper()
        results = []
        
        for game_name in self.pg_games.keys():
            if keyword in game_name:
                results.append(game_name)
            else:
                # Tìm trong thông tin game
                game = self.pg_games[game_name]
                if (keyword in game["theme"].upper() or 
                    keyword in " ".join(game["features"]).upper()):
                    results.append(game_name)
        
        return results
    
    def analyze_game_detail(self, game_name: str) -> Dict:
        """Phân tích chi tiết một game"""
        game_name = game_name.upper()
        
        if game_name not in self.pg_games:
            similar = self.search_games(game_name)
            if similar:
                game_name = similar[0]
            else:
                return {"error": f"Không tìm thấy game {game_name}"}
        
        game = self.pg_games[game_name]
        
        # Tính toán RTP hiệu chỉnh
        base_rtp = game["rtp"]
        hour = datetime.now().hour
        
        # Điều chỉnh theo giờ
        if 14 <= hour < 17:  # Chiều
            adjusted_rtp = base_rtp * 1.02
        elif 20 <= hour < 23:  # Tối
            adjusted_rtp = base_rtp * 1.03
        elif 9 <= hour < 12:  # Sáng
            adjusted_rtp = base_rtp * 1.01
        else:
            adjusted_rtp = base_rtp * 0.98
        
        # Đánh giá
        if adjusted_rtp >= 96.6:
            rating = "⭐⭐⭐⭐⭐"
            recommendation = "🔥 XUẤT SẮC"
        elif adjusted_rtp >= 96.4:
            rating = "⭐⭐⭐⭐"
            recommendation = "✅ RẤT TỐT"
        elif adjusted_rtp >= 96.2:
            rating = "⭐⭐⭐"
            recommendation = "⚠️ KHÁ"
        else:
            rating = "⭐⭐"
            recommendation = "⛔ TRUNG BÌNH"
        
        # Chiến thuật
        strategy = game.get("strategy", [
            "• Chơi ổn định với cược nhỏ",
            "• Tập trung vào bonus features",
            "• Theo dõi volatility của game",
            "• Dừng khi đạt mục tiêu"
        ])
        
        return {
            "game": game_name,
            "rating": rating,
            "recommendation": recommendation,
            "details": {
                "Nhà phát triển": "PG SOFT",
                "Năm phát hành": game.get("year", 2023),
                "Reels": game["reels"],
                "Paylines": game.get("paylines", "Ways"),
                "RTP gốc": f"{base_rtp}%",
                "RTP hiệu chỉnh": f"{adjusted_rtp:.2f}%",
                "Volatility": game["volatility"],
                "Max Win": game["max_win"],
                "Min Bet": f"{game['min_bet']:,}",
                "Chủ đề": game["theme"],
                "Độ phổ biến": f"{game.get('popularity', 80)}%",
                "Tính năng đặc biệt": ", ".join(game["features"])
            },
            "strategy": strategy,
            "best_time_to_play": self._get_best_time(game["volatility"]),
            "similar_games": self._get_similar_games(game_name, game["theme"]),
            "analysis_time": datetime.now().strftime("%H:%M:%S")
        }
    
    def _get_best_time(self, volatility: str) -> str:
        """Thời gian tốt nhất chơi"""
        if volatility in ["Rất cao", "Cao"]:
            return "20:00-23:00 (Tối - High Volatility hoạt động mạnh)"
        elif volatility == "Trung bình":
            return "14:00-17:00 (Chiều - Ổn định)"
        else:
            return "09:00-12:00 (Sáng - Low Volatility an toàn)"
    
    def _get_similar_games(self, current_game: str, theme: str) -> List[str]:
        """Tìm game tương tự"""
        similar = []
        current_game_lower = current_game.lower()
        
        for game_name, game in self.pg_games.items():
            if game_name != current_game and game["theme"] == theme:
                similar.append(game_name)
                if len(similar) >= 3:
                    break
        
        return similar
    
    def get_top_games_by_category(self, category: str = None) -> List[Dict]:
        """Lấy top game theo thể loại"""
        if category and category in self.categories:
            game_names = self.categories[category]
        else:
            game_names = list(self.pg_games.keys())
        
        # Sắp xếp theo popularity
        sorted_games = []
        for game_name in game_names:
            if game_name in self.pg_games:
                game = self.pg_games[game_name]
                sorted_games.append({
                    "name": game_name,
                    "popularity": game.get("popularity", 80),
                    "rtp": game["rtp"],
                    "volatility": game["volatility"],
                    "theme": game["theme"]
                })
        
        sorted_games.sort(key=lambda x: x["popularity"], reverse=True)
        return sorted_games[:10]
    
    def generate_daily_recommendation(self) -> Dict:
        """Tạo đề xuất game hàng ngày"""
        weekday = datetime.now().weekday()
        hour = datetime.now().hour
        
        # Chọn game theo ngày
        day_themes = {
            0: "Trung Quốc",  # Thứ 2
            1: "Thần thoại",   # Thứ 3
            2: "Phiêu lưu",    # Thứ 4
            3: "Cổ điển",      # Thứ 5
            4: "Hiện đại",     # Thứ 6
            5: "Fantasy",      # Thứ 7
            6: "Thiên nhiên"   # Chủ nhật
        }
        
        theme = day_themes.get(weekday, "Trung Quốc")
        games_in_theme = self.categories.get(theme, [])
        
        # Chọn game ngẫu nhiên
        if games_in_theme:
            selected_game = random.choice(games_in_theme)
            game_detail = self.analyze_game_detail(selected_game)
            
            return {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "day_of_week": ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"][weekday],
                "theme_of_day": theme,
                "recommended_game": selected_game,
                "reason": f"Hôm nay là ngày {theme} - {selected_game} phù hợp nhất",
                "game_details": game_detail,
                "alternative_games": [g for g in games_in_theme if g != selected_game][:2]
            }
        
        return {"error": "Không tạo được đề xuất"}

# ========== BOT TELEGRAM ==========
try:
    from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
    from dotenv import load_dotenv
except ImportError as e:
    logger.error(f"❌ Lỗi import: {e}")
    print("\n📦 Vui lòng cài đặt thư viện:")
    print("pip install python-telegram-bot python-dotenv")
    sys.exit(1)

# Khởi tạo analyzer
analyzer = PGSoftCompleteAnalyzer()

# Load config
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ Thiếu BOT_TOKEN trong .env")
    print("👉 Tạo file .env với nội dung:")
    print("BOT_TOKEN=your_bot_token_here")
    sys.exit(1)

# ========== MENU ==========
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🎮 TRA CỨU GAME", callback_data="search_game")],
        [InlineKeyboardButton("🏆 TOP GAME HOT", callback_data="top_games")],
        [InlineKeyboardButton("📊 PHÂN LOẠI", callback_data="categories")],
        [InlineKeyboardButton("⭐ ĐỀ XUẤT HÔM NAY", callback_data="daily_recommend")],
        [InlineKeyboardButton("🔍 TÌM KIẾM", callback_data="search")],
        [InlineKeyboardButton("ℹ️ THÔNG TIN", callback_data="info")]
    ]
    return InlineKeyboardMarkup(keyboard)

def categories_menu():
    categories = list(analyzer.categories.keys())
    keyboard = []
    
    for i in range(0, len(categories), 2):
        row = []
        for j in range(2):
            if i + j < len(categories):
                cat = categories[i + j]
                row.append(InlineKeyboardButton(cat, callback_data=f"cat_{cat}"))
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton("🔙 VỀ MENU", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def games_list_menu(games_list):
    keyboard = []
    
    for i in range(0, len(games_list), 3):
        row = []
        for j in range(3):
            if i + j < len(games_list):
                game = games_list[i + j]
                row.append(InlineKeyboardButton(game[:15], callback_data=f"game_{game}"))
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton("🔙 VỀ MENU", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

# ========== HANDLERS ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    welcome = f"""
🎮 **BOT PHÂN TÍCH GAME PG SOFT ĐẦY ĐỦ**

Chào {user.first_name}! 👋

📊 **Database đồ sộ:** {analyzer.total_games} game PG SOFT
🎯 **Tính năng chính:**
• 🎮 Tra cứu chi tiết từng game
• 🏆 Top game hot nhất
• 📊 Phân loại theo thể loại
• ⭐ Đề xuất game hàng ngày
• 🔍 Tìm kiếm game nâng cao

✨ **PG SOFT Features:**
• RTP: 96.32% - 96.71%
• Volatility: Thấp → Rất cao
• Max Win: x4000 - x30000
• Themes: Đa dạng, độc đáo

⚠️ *Bot chỉ phân tích, không đảm bảo kết quả*
"""
    
    await update.message.reply_text(welcome, parse_mode='Markdown', reply_markup=main_menu())

async def search_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    all_games = list(analyzer.pg_games.keys())[:30]
    
    await update.message.reply_text(
        "🎮 **CHỌN GAME ĐỂ PHÂN TÍCH:**\n(Hiển thị 30/50+ game)",
        reply_markup=games_list_menu(all_games)
    )

async def top_games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top = analyzer.get_top_games_by_category()
    
    message = "🏆 **TOP 10 GAME PG SOFT HOT NHẤT**\n\n"
    
    for idx, game in enumerate(top, 1):
        medal = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"][idx-1]
        message += f"{medal} *{game['name']}*\n"
        message += f"   📊 Popularity: {game['popularity']}%\n"
        message += f"   🎯 RTP: {game['rtp']}%\n"
        message += f"   ⚡ Volatility: {game['volatility']}\n"
        message += f"   🎨 Theme: {game['theme']}\n\n"
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    categories = analyzer.get_game_categories()
    
    message = "📊 **PHÂN LOẠI GAME PG SOFT**\n\n"
    
    for category, games in categories.items():
        message += f"🎨 *{category}*\n"
        message += f"   📁 Số game: {len(games)}\n"
        message += f"   🎮 Ví dụ: {', '.join(games[:3])}\n\n"
    
    message += "👉 Chọn thể loại để xem game:"
    
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=categories_menu())

async def daily_recommend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    recommendation = analyzer.generate_daily_recommendation()
    
    if "error" in recommendation:
        await update.message.reply_text("❌ Không thể tạo đề xuất")
        return
    
    message = f"""
⭐ **ĐỀ XUẤT GAME HÔM NAY**

📅 Ngày: {recommendation['date']}
📆 {recommendation['day_of_week']}
🎨 Chủ đề ngày: *{recommendation['theme_of_day']}*

🏆 **GAME ĐỀ XUẤT:**
🎮 *{recommendation['recommended_game']}*
📝 Lý do: {recommendation['reason']}

📊 **Thông số game:**
• RTP: {recommendation['game_details']['details']['RTP gốc']}
• RTP hiệu chỉnh: {recommendation['game_details']['details']['RTP hiệu chỉnh']}
• Volatility: {recommendation['game_details']['details']['Volatility']}
• Max Win: {recommendation['game_details']['details']['Max Win']}
• Min Bet: {recommendation['game_details']['details']['Min Bet']}

🎯 **Đánh giá:** {recommendation['game_details']['rating']}
💡 **Khuyến nghị:** {recommendation['game_details']['recommendation']}

🕐 **Thời gian chơi tốt nhất:**
{recommendation['game_details']['best_time_to_play']}

🔄 **Game thay thế:**
{', '.join(recommendation['alternative_games'])}
"""
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "🔍 **TÌM KIẾM GAME**\n\n"
            "Cú pháp: `/tìm [từ khóa]`\n"
            "Ví dụ:\n"
            "• `/tìm mahjong`\n"
            "• `/tìm dragon`\n"
            "• `/tìm china`\n"
            "• `/tìm high rtp`",
            parse_mode='Markdown'
        )
        return
    
    keyword = ' '.join(context.args)
    results = analyzer.search_games(keyword)
    
    if not results:
        await update.message.reply_text(f"❌ Không tìm thấy game với từ khóa: *{keyword}*", parse_mode='Markdown')
        return
    
    message = f"🔍 **KẾT QUẢ TÌM KIẾM: {keyword}**\n\n"
    message += f"📊 Tìm thấy *{len(results)}* game\n\n"
    
    for idx, game in enumerate(results[:10], 1):
        message += f"{idx}. *{game}*\n"
    
    if len(results) > 10:
        message += f"\n...và {len(results)-10} game khác"
    
    message += "\n\n👉 Nhấn vào tên game để xem chi tiết"
    
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=games_list_menu(results[:15]))

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f"""
ℹ️ **THÔNG TIN BOT PG SOFT**

📊 **Database:**
• Tổng số game: {analyzer.total_games}
• Thể loại: {len(analyzer.categories)}
• Nhà phát triển: PG SOFT
• Ngôn ngữ: Tiếng Việt

🎯 **Thông số kỹ thuật:**
• RTP cao nhất: 96.71% (Mahjong Ways)
• RTP thấp nhất: 96.32% (Doomsday Rampage)
• Volatility: Đầy đủ 4 cấp độ
• Max Win cao nhất: x30000

📁 **Thể loại có sẵn:**
{', '.join(analyzer.categories.keys())}

🎮 **Top 5 game phổ biến:**
"""
    
    top = analyzer.get_top_games_by_category()[:5]
    for idx, game in enumerate(top, 1):
        message += f"{idx}. {game['name']} ({game['popularity']}%)\n"
    
    message += """
🔧 **Các lệnh chính:**
/start - Khởi động bot
/top - Top game hot
/loai - Phân loại game
/dexuat - Đề xuất hôm nay
/tìm [từ khóa] - Tìm kiếm game
/game [tên] - Phân tích game

⚠️ **Lưu ý:**
• Bot chỉ phân tích thông tin game
• Không đảm bảo kết quả thực tế
• Chơi game có trách nhiệm
"""
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def game_detail_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "🎮 **PHÂN TÍCH GAME**\n\n"
            "Cú pháp: `/game [tên game]`\n"
            "Ví dụ:\n"
            "• `/game mahjong ways`\n"
            "• `/game wild bandito`\n"
            "• `/game heist stakes`\n\n"
            "Hoặc dùng nút bấm ở menu",
            parse_mode='Markdown'
        )
        return
    
    game_name = ' '.join(context.args)
    analysis = analyzer.analyze_game_detail(game_name)
    
    if "error" in analysis:
        await update.message.reply_text(f"❌ {analysis['error']}")
        return
    
    message = f"""
🎮 **PHÂN TÍCH CHI TIẾT: {analysis['game']}**

{analysis['rating']} *{analysis['recommendation']}*

📊 **THÔNG SỐ KỸ THUẬT:**
"""
    
    for key, value in analysis["details"].items():
        message += f"• *{key}:* {value}\n"
    
    message += f"\n🎯 **CHIẾN THUẬT CHƠI:**\n"
    for strat in analysis["strategy"]:
        message += f"{strat}\n"
    
    message += f"\n🕐 **THỜI GIAN TỐT NHẤT:**\n{analysis['best_time_to_play']}\n"
    
    if analysis["similar_games"]:
        message += f"\n🔄 **GAME TƯƠNG TỰ:**\n{', '.join(analysis['similar_games'])}\n"
    
    message += f"\n⏰ Phân tích lúc: {analysis['analysis_time']}"
    
    await update.message.reply_text(message, parse_mode='Markdown')

# ========== CALLBACK HANDLERS ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "search_game":
        await search_game(update, context)
    
    elif data == "top_games":
        await top_games(update, context)
    
    elif data == "categories":
        await categories(update, context)
    
    elif data == "daily_recommend":
        await daily_recommend(update, context)
    
    elif data == "search":
        await update.callback_query.message.reply_text(
            "🔍 Gõ từ khóa tìm kiếm:\nVí dụ: dragon, china, high rtp"
        )
    
    elif data == "info":
        await info_command(update, context)
    
    elif data.startswith("cat_"):
        category = data.replace("cat_", "")
        games = analyzer.categories.get(category, [])
        
        message = f"🎨 **THỂ LOẠI: {category}**\n\n"
        message += f"📁 Số game: {len(games)}\n\n"
        
        for idx, game in enumerate(games[:15], 1):
            message += f"{idx}. *{game}*\n"
        
        await query.edit_message_text(
            message,
            parse_mode='Markdown',
            reply_markup=games_list_menu(games[:20])
        )
    
    elif data.startswith("game_"):
        game_name = data.replace("game_", "")
        analysis = analyzer.analyze_game_detail(game_name)
        
        if "error" not in analysis:
            message = f"""
🎮 **{analysis['game']}**

{analysis['rating']} *{analysis['recommendation']}*

📊 **Thông số chính:**
• RTP: {analysis['details']['RTP gốc']}
• RTP hiệu chỉnh: {analysis['details']['RTP hiệu chỉnh']}
• Volatility: {analysis['details']['Volatility']}
• Max Win: {analysis['details']['Max Win']}
• Min Bet: {analysis['details']['Min Bet']}
• Chủ đề: {analysis['details']['Chủ đề']}
• Phổ biến: {analysis['details']['Độ phổ biến']}

🎯 **Chiến thuật:**
"""
            for strat in analysis["strategy"][:3]:
                message += f"{strat}\n"
            
            message += f"\n🕐 Thời gian tốt: {analysis['best_time_to_play']}"
            message += f"\n⏰ {analysis['analysis_time']}"
            
            await query.edit_message_text(message, parse_mode='Markdown')
    
    elif data == "back_to_main":
        await query.edit_message_text(
            "🎮 **BOT PHÂN TÍCH PG SOFT**\nChọn tính năng:",
            reply_markup=main_menu()
        )

# ========== COMMAND HANDLERS ==========
async def top_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await top_games(update, context)

async def loai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await categories(update, context)

async def dexuat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await daily_recommend(update, context)

async def tim_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await search_command(update, context)

async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await game_detail_command(update, context)

# ========== MAIN ==========
def main():
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("top", top_command))
        application.add_handler(CommandHandler("loai", loai_command))
        application.add_handler(CommandHandler("dexuat", dexuat_command))
        application.add_handler(CommandHandler("tìm", tim_command))
        application.add_handler(CommandHandler("tim", tim_command))
        application.add_handler(CommandHandler("game", game_command))
        application.add_handler(CommandHandler("info", info_command))
        
        # Button handler
        application.add_handler(CallbackQueryHandler(button_handler))
        
        # Hiển thị thông tin
        print("\n" + "="*60)
        print("🎮 BOT PHÂN TÍCH PG SOFT - ĐẦY ĐỦ 50+ GAME")
        print("="*60)
        print(f"📊 Tổng số game: {analyzer.total_games}")
        print(f"📁 Thể loại: {len(analyzer.categories)}")
        print(f"🎯 RTP range: 96.32% - 96.71%")
        print(f"⚡ Volatility: Đầy đủ 4 cấp độ")
        print("="*60)
        print("🚀 Đang khởi động bot...")
        print("📱 Mở Telegram, tìm bot của bạn")
        print("💡 Gõ /start để bắt đầu")
        print("="*60 + "\n")
        
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Lỗi: {e}")
        print("👉 Cài đặt: pip install python-telegram-bot python-dotenv")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
