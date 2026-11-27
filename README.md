# WIMSICAL: The Global Geometric-Entropic-Electromagnetic Model (GEE v7.5)

[![DOI](https://zenodo.org)](https://doi.org)
[![ORCID](https://shields.io)](https://orcid.org)
[![License: CC BY 4.0](https://shields.io)](https://creativecommons.org)
[![License: MIT](https://shields.io)](https://opensource.org)

**Author & Principal Investigator:** Yen-Hao Chen (Seven-Colored Lotus / 七色蓮花)  
**Affiliation:** Independent Researcher, Hsinchu, Taiwan  
**Correspondence:** jackwolf1970@gmail.com  
**ORCID:** [0009-0007-2299-0913](https://orcid.org)  
**Zenodo Archive DOI:** [10.5281/zenodo.24580326](https://doi.org)

---

## Overview & Key Breakthroughs in `v7.5`

**WIMSICAL (GEE v7.5)** is a four-dimensional covariant, zero-free-parameter cosmological and astrophysical framework derived strictly from the Principle of Least Action (\(\delta S_{\mathrm{GEE}} / \delta g_{\mu\nu} = 0\)). Grounded directly in **Bose–Einstein quantum statistics**, **classical spherical Sturm–Liouville boundary-value theory**, and **Planck CMB observational geometry**, GEE v7.5 eliminates all unverified non-baryonic sectors and ad-hoc fitting parameters. It unifies gravitational, geometric-elastic, thermodynamic-entropic, and chiral magnetohydrodynamic interactions across **40 universal benchmarks**, **53 multi-population systems**, and **21 premier gravitational lenses and supervoids** within \(\le 0.39\sigma\).

### What's New in `v7.5`

* **Quantum-Statistical Origin of \(\alpha_{\mathrm{ent}}\) & Multi-Precision Hierarchy:** Anchors the entropic spatial coupling constant forward from the Bose–Einstein statistical mechanics of a plasma-free (\(X_e = 0\)) 3D Planckian blackbody cavity without empirical fitting:

\[\alpha_{\mathrm{ent}} = \frac{\langle x \rangle_{\mathrm{Planck}}}{2\pi}\left(1 - \frac{1}{12\pi}\right) = \frac{\pi^3}{60\,\zeta(3)}\left(1 - \frac{1}{12\pi}\right)\]

  Preserved across three precision tiers to prevent cumulative long-baseline truncation errors:
  * **Ultra-Precision Tier (8-digit):** \(\alpha_{\mathrm{ent}}^{(8)} = 0.41850223\)
  * **Standard Precision Tier (6-digit):** \(\alpha_{\mathrm{ent}}^{(6)} = 0.418502\)
  * **Baseline Compatibility Tier (4-digit):** \(\alpha_{\mathrm{ent}}^{(4)} = 0.4185\)

* **Spherical Sturm–Liouville Boundary Eigenmodes (68 Shells & 102 Cycles):** Derived from radiation-pressure dissipation and wave-impedance mismatch between the inner Planck curvature bounce wall (\(\chi_2 \to -1\), \(m = 0\)) and the outer thermodynamic absolute-zero freeze-out boundary (\(T \to 0\ \mathrm{K}\), \(m = 68\)), partitioning the static Euclidean horizon (\(R_{\max} = 14,178.00\ \mathrm{Mpc} = 46.2425\ \mathrm{Gly}\)) into **34 single-pass wavelengths** (68 half-wavelength concentric shells) and **3 cavity transits** (102 damped oscillation cycles; 1.5 macro-cycles) required for global 3D standing-wave phase locking.

* **Standardized Physical Nomenclature (`Anti-Node Shells` & `Node Shells`):** Eliminates all ambiguous non-baryonic labels. Constructive spherical interference hubs are standardized as **Anti-Node Shells (`AS-01` through `AS-09`)** (centripetal attraction and lensing zones), strictly distinguished from destructive supervoid **Node Shells** (centrifugal outflow zones), achieving \(0.01\sigma\text{–}0.39\sigma\) observational alignment.

* **Decoupled Dual-Chronology & Environmental Forensics:** Formalizes the causal and temporal decoupling between the pre-matter entropic spatial micro-force wave (**0th Chime**) and the observable baryon–photon acoustic epoch (**1st Chime**, \(13.7962\ \mathrm{Gyr}\)), alongside variable-mass baryonic accretion drag (\(\dot{m}v\)) and 3D supervoid repeller vector forensics (\(\le 0.34\sigma\) for isolated cluster cores).

* **Multi-Plane Jacobi Lensing & Blind-Test Coordinates:** Quantifies foreground Eridanus Supervoid concave dimming bias behind Anti-Node Shell `AS-01` (\(\Delta m_{\mathrm{bias}} = +0.0280\ \mathrm{mag}\)) and provides J2000.0 pointing coordinates (`AS-06` to `AS-09`) for JWST, Euclid, and Roman surveys.

---

## Repository Root Directory & Verification

All `v7.5` release documents and standalone, zero-free-parameter Python verification scripts are located directly in the repository root directory:

```text
Wimsical/
├── README.md                                # Repository overview & v7.5 release documentation
├── GEE_v7.5_Master_Monograph.pdf            # Complete theoretical framework & 40-benchmark audit
├── verify_gee_v75_master_monograph.py       # Full 40-benchmark & 3-tier precision audit suite
└── verify_gee_v75_paper4.py                 # 3D standing-wave (AS-01–AS-09) & Jacobi lensing suite
```

### Quick Start (Numerical Verification)
```bash
git clone https://github.com
cd Wimsical
python3 verify_gee_v75_master_monograph.py
python3 verify_gee_v75_paper4.py
```

---

## Citation

If you use the GEE v7.5 framework, analytical derivations, or Python verification suites in your research, please cite:

```bibtex
@misc{Chen2026_GEE_v75,
  author       = {Chen, Yen-Hao},
  title        = {{WIMSICAL: The Global Geometric-Entropic-Electromagnetic Model (GEE v7.5)}},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v7.5},
  doi          = {10.5281/zenodo.24580326},
  url          = {https://doi.org}
}
```

## License
* **Monograph & Documentation:** Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org).
* **Verification Source Code (`.py`):** Licensed under the [MIT License](https://opensource.org).
