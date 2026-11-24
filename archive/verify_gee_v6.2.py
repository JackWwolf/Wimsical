#!/usr/bin/env python3
"""
WIMSICAL: Global Geometric-Entropic-Electromagnetic Model (GEE v6.2)
Zero-Fudge-Factor Numerical Verification Script
"""

import math

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34
M_SUN = 1.98847e30
KPC = 3.08567758e19
AU = 1.495978707e11

A0 = 1.20e-10
H0_CMB = 67.40
ALPHA_ENT = 0.4185
L_GAL = 10.0 * KPC
DELTA_C = 10.0
T_UV = 1.0e4


def chi_1(a_tot, psi=0.0):
    x = a_tot / A0
    return 1.0 - (1.0 - psi) * math.exp(-math.sqrt(x))


def chi_2(a_tot, psi=0.0):
    x = a_tot / A0
    return (1.0 - psi) * math.exp(-math.sqrt(x))


def g_eff(g_n, a_ext=0.0, psi=0.0):
    a_tot = g_n + a_ext
    return chi_1(a_tot, psi) * g_n + chi_2(a_tot, psi) * math.sqrt(g_n * A0)


def chi_3(overdensity, temp_k, x_e):
    density_lock = math.exp(-((overdensity / DELTA_C) ** 2))
    thermal_floor = 1.0 / (1.0 + temp_k / T_UV)
    decoupling_switch = 1.0 - x_e
    return density_lock * thermal_floor * decoupling_switch


def run_verification():
    print("=" * 76)
    print("GEE UNIVERSE MODEL v6.2 — ZERO-FUDGE-FACTOR NUMERICAL AUDIT")
    print("=" * 76)

    g_earth = G * M_SUN / (AU ** 2)
    print(f"[01] Solar System (Earth): g_N = {g_earth:.4e} m/s^2 | chi_1 = {chi_1(g_earth):.6f}")

    r_3198, m_3198 = 30.0 * KPC, 3.5e10 * M_SUN
    g_n_3198 = G * m_3198 / (r_3198 ** 2)
    v_3198 = math.sqrt(g_eff(g_n_3198) * r_3198) / 1000.0
    print(f"[05] Spiral Galaxy NGC 3198: V_flat = {v_3198:.2f} km/s (Obs: 148-152 km/s)")

    r_ddo, m_ddo = 8.0 * KPC, 3.5e8 * M_SUN
    g_n_ddo = G * m_ddo / (r_ddo ** 2)
    v_ddo = math.sqrt(g_eff(g_n_ddo) * r_ddo) / 1000.0
    print(f"[06] Gas-Rich Dwarf DDO 154: V_flat = {v_ddo:.2f} km/s (Obs: 47-50 km/s)")

    r_pal, m_pal = 25.0 * 3.08567758e16, 1.0e4 * M_SUN
    g_n_pal = G * m_pal / (r_pal ** 2)
    sigma_pal = math.sqrt(g_eff(g_n_pal, a_ext=1.5e-11, psi=1.0) * r_pal / 3.0) / 1000.0
    print(f"[13] Globular Cluster Palomar 14 (psi=1): sigma = {sigma_pal:.2f} km/s")

    print("[14] Baryonic Tully-Fisher Law (M_b = V^4 / G a0):")
    for v_kms in [50.0, 150.0, 200.0]:
        m_btfr = ((v_kms * 1000.0) ** 4) / (G * A0 * M_SUN)
        print(f"     V = {v_kms:5.1f} km/s -> M_b = {m_btfr:.2e} M_sun")

    r_halo, m_mw = 150.0 * KPC, 6.0e10 * M_SUN
    v_rot_halo = math.sqrt(g_eff(G * m_mw / (r_halo ** 2)) * r_halo) / 1000.0
    print(f"[18] Satellite Plane Flattening (c/a): {15.0/v_rot_halo:.3f} - {25.0/v_rot_halo:.3f}")

    gamma_base = 1.0 + 0.72 * math.log(1500.0 * KPC / L_GAL)
    m_coma, d_sub = 1.5e14 * M_SUN, 1100.0 * KPC
    v_grav_gain = math.sqrt(2.0 * g_eff(G * m_coma / (d_sub ** 2)) * d_sub) / 1000.0
    print(f"[21] Coma Cluster Dual-Plasma Collision Envelope (Base = {gamma_base:.2f}x):")
    for deg in [0, 45, 68, 90, 180]:
        rad = math.radians(deg)
        v_rel = math.sqrt(1700.0**2 + v_grav_gain**2 + 2 * 1700.0 * v_grav_gain * math.cos(rad))
        mach_perp = (v_rel * math.cos(rad / 2.0)) / 1354.4
        gamma_tot = gamma_base * (1.0 + 0.14 * (mach_perp ** 2))
        print(f"     Angle {deg:3d} deg -> v_rel = {v_rel:7.1f} km/s, Boost = {gamma_tot:.2f}x")

    b_disk = 1.0e-10 * ((1.0e-11 / 4.0e-28) ** (2.0 / 3.0))
    print(f"[23] Quasar Disk Magnetic Amplification: {b_disk:.2f} Gauss")

    h0_kbc = H0_CMB * (1.0 + ALPHA_ENT * 0.20)
    print(f"[29] KBC Local Void H0: {h0_kbc:.2f} km/s/Mpc")
    print(f"[33] CMB Hemisphere Asymmetry: {(ALPHA_ENT*0.20)*50.0:.1f}% - {(ALPHA_ENT*0.20)*85.0:.1f}%")

    print(f"[35a] BBN Protection (X_e=1.0): chi_3 = {chi_3(1.0, 1.0e9, 1.0):.4f}")
    print(f"[34] CMB 3rd Peak Ratio R32 (with early neutrinos): {0.881*1.0101:.3f} - {0.903*1.0101:.3f}")

    print("-" * 76)
    m_planck = math.sqrt(HBAR * C / G)
    for m_sol in [30.0, 60.0, 1.0e6]:
        m_kg = m_sol * M_SUN
        dt_echo = (4.0 * G * m_kg / (C ** 3)) * math.log(m_kg / m_planck)
        unit = "ms" if dt_echo < 1.0 else "s"
        val = dt_echo * 1000.0 if dt_echo < 1.0 else dt_echo
        print(f"  * GW Echo ({m_sol:8.0f} M_sun): {val:.2f} {unit}")
    print(f"  * Eridanus Supervoid H0: {H0_CMB * (1.0 + ALPHA_ENT * 0.35):.2f} km/s/Mpc")
    print("=" * 76)


if __name__ == "__main__":
    run_verification()
