#=================================== Water Proreties===================================
water_properties = {
    20: {"density": 998.21, "viscosity": 1.002e-3, "cp": 4.185, "conductivity": 0.598},
    30: {"density": 995.65, "viscosity": 0.797e-3, "cp": 4.180, "conductivity": 0.616},
    40: {"density": 992.22, "viscosity": 0.653e-3, "cp": 4.179, "conductivity": 0.631},
    50: {"density": 988.05, "viscosity": 0.547e-3, "cp": 4.180, "conductivity": 0.644},
    60: {"density": 983.21, "viscosity": 0.466e-3, "cp": 4.183, "conductivity": 0.654},
    70: {"density": 977.78, "viscosity": 0.404e-3, "cp": 4.188, "conductivity": 0.663},
    80: { "density": 971.80, "viscosity": 0.354e-3,"cp": 4.196, "conductivity": 0.670}
}

#======================= Nano particles =============================
nanoparticles = {
    "al2o3": {"density": 3970, "Cp": 765,"k": 40, "lamda": 0.85e-5},
    "cuo"  : {"density": 6400, "Cp": 540, "k": 18, "lamda": 0.85e-5},
    "h-bn" : {"density": 2280, "Cp": 760,"k": 400, "lamda": 0.40e-5,},
    "tio2" : {"density": 4250, "Cp": 686,"k": 8.95,"lamda": 0.90e-5},
    "sio2" : {"density": 2200, "Cp": 745,"k": 1.4, "lamda": 0.63e-5, },
    "fe3o4": {"density": 5200, "Cp": 670,"k": 6.0, "lamda": 1.30e-5,}
}



# ============================ For Word File ==============================

# Display labels for nanoparticle keys
DISPLAY = {
    "al2o3": "Al2O3", "cuo": "CuO", "h-bn": "h-BN",
    "tio2": "TiO2", "sio2": "SiO2", "fe3o4": "Fe3O4",
}

DESIGN_MATRIX = [
    ("h-BN - Al2O3", "h-bn", "al2o3",
     "Best mono performer + cost-effective booster",
     [0.5, 1.0, 1.5], [(25, 75), (50, 50)]),
 
    ("h-BN - CuO", "h-bn", "cuo",
     "Best mono performer + second booster for comparison",
     [0.5, 1.0, 1.5], [(25, 75), (50, 50)]),
 
    ("Al2O3 - CuO", "al2o3", "cuo",
     "Benchmark hybrid; most-studied combination in the literature",
     [1.5, 5.0, 10.0], [(25, 75), (50, 50)]),
 
    ("Fe3O4 - SiO2", "fe3o4", "sio2",
     "Magnetic + stable combination; reported as promising in recent reviews",
     [0.5, 1.0, 1.5], [(25, 75), (50, 50)]),
 
    ("Al2O3 - SiO2", "al2o3", "sio2",
     "Inexpensive, chemically stable pairing; higher SiO2 share raises k further",
     [1.0, 1.5, 4.0], [(20, 80), (50, 50)]),
 
    ("CuO - Fe3O4", "cuo", "fe3o4",
     "Combines best-performing oxide with a magnetically responsive particle",
     [0.5, 1.0, 1.5], [(25, 75), (50, 50)]),
 
    ("h-BN - SiO2", "h-bn", "sio2",
     "High-k booster + cheapest, most stable oxide; good cost-vs-performance trade-off",
     [0.5, 1.0, 1.5], [(25, 75), (50, 50)]),
]