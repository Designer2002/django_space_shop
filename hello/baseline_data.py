from hello.models import Weapon
from hello.models import CustomUser

users = [
    CustomUser(username="admin", email="admin@spaceshop.com", is_admin=True),
    CustomUser(username="jane", email="marytun2003@gmail.com"),
    CustomUser(username="amogus", email="marytun2002@yandex.ru"),
]


weapons = [
    Weapon(
        name="Photon Blaster X1",
        price=299.99,
        description="Compact yet powerful blaster with photon beams ideal for short-range combat.",
        power_consumption="500W",
        charging_method="Solar Charging",
        range="50 meters",
        weight="2.5 kg",
        warranty="2 years"
    ),
    Weapon(
        name="Plasma Rifle Pro",
        price=749.99,
        description="High-tech rifle delivering precise plasma shots for medium-range engagements.",
        power_consumption="1200W",
        charging_method="Battery Pack",
        range="200 meters",
        weight="4.5 kg",
        warranty="5 years"
    ),
    Weapon(
        name="Quantum Destroyer",
        price=1299.99,
        description="A devastating weapon capable of firing quantum disruption waves for large areas.",
        power_consumption="3000W",
        charging_method="Hybrid Battery and Solar",
        range="500 meters",
        weight="10 kg",
        warranty="3 years"
    ),
    Weapon(
        name="Nebula Handgun",
        price=199.99,
        description="Lightweight handgun perfect for stealth operations in close combat.",
        power_consumption="300W",
        charging_method="Mini Battery",
        range="30 meters",
        weight="1.2 kg",
        warranty="1 year"
    ),
    Weapon(
        name="Stellar Cannon",
        price=999.99,
        description="Heavy-duty cannon designed for long-range assaults and fortifications.",
        power_consumption="5000W",
        charging_method="Fuel Cell",
        range="1000 meters",
        weight="20 kg",
        warranty="3 years"
    ),
    Weapon(
        name="Gamma Blaster Mk II",
        price=499.99,
        description="Upgraded blaster optimized for rapid fire and increased accuracy.",
        power_consumption="800W",
        charging_method="Battery Pack",
        range="150 meters",
        weight="3 kg",
        warranty="4 years"
    ),
    Weapon(
        name="Eclipse Sniper",
        price=1099.99,
        description="Precision sniper rifle with cutting-edge optics for pinpoint accuracy.",
        power_consumption="1500W",
        charging_method="Fusion Battery",
        range="1200 meters",
        weight="8 kg",
        warranty="5 years"
    ),
    Weapon(
        name="Vortex Launcher",
        price=1399.99,
        description="Explosive launcher firing vortex bombs capable of disabling large fleets.",
        power_consumption="3500W",
        charging_method="Hydrogen Cell",
        range="800 meters",
        weight="15 kg",
        warranty="2 years"
    ),
    Weapon(
        name="Cosmic Blade",
        price=399.99,
        description="Melee weapon emitting an energy blade for close-quarters combat.",
        power_consumption="200W",
        charging_method="Compact Charger",
        range="N/A",
        weight="2 kg",
        warranty="2 years"
    ),
    Weapon(
        name="Aurora Shield Disruptor",
        price=849.99,
        description="Specialized tool for neutralizing enemy energy shields.",
        power_consumption="1000W",
        charging_method="Inductive Charging",
        range="300 meters",
        weight="5 kg",
        warranty="3 years"
    ),
]

def init():
    for weapon in weapons:
        weapon.save()

    for user in users:
        user.set_password("123")
        user.save()