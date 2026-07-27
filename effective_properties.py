# For Mono-nano Particle Nano fluid(water)

def eff_prop_mono(rho_w, Cp_w, k_w, mu_w,
                         rho_n, Cp_n, k_n, phi):

    rho_nf = (1 - phi) * rho_w + phi * rho_n                       # linear mixture

    Cp_nf = ((1 - phi) * rho_w * Cp_w + phi * rho_n * Cp_n) / rho_nf  #enery-weighted


    k_nf = k_w * (                                                 # Classical Maxwell-relation
        (k_n + 2*k_w - 2*phi*(k_w - k_n)) /
        (k_n + 2*k_w + phi*(k_w - k_n))
    )

    mu_nf = mu_w / (1 - phi) ** 2.5                                # Brinkman relation

    return rho_nf, Cp_nf, k_nf, mu_nf


# Di-nano Particle Nano Fluid(water)

def eff_prop_di(rho_w, Cp_w, k_w, mu_w,
                rho_n1, Cp_n1, k_n1, phi1,
                rho_n2, Cp_n2, k_n2, phi2):

    phi_t = phi1 + phi2
 
    rho_hf = (1 - phi_t) * rho_w + phi1 * rho_n1 + phi2 * rho_n2
    rhoCp_hf = (1 - phi_t) * rho_w * Cp_w + phi1 * rho_n1 * Cp_n1 + phi2 * rho_n2 * Cp_n2
    Cp_hf = rhoCp_hf / rho_hf

    mu_hf = mu_w / (((1 - phi1) ** 2.5) * ((1 - phi2) ** 2.5))                 # Brinkman relation

     # Sequential two-step Maxwell model: water+particle1 -> "base fluid" for particle2 
    knf  = k_w * (
        (k_n1 + 2 * k_w - 2 * phi1*(k_w - k_n1))
        / 
        (k_n1 + 2 * k_w + phi1 * (k_w - k_n1))
        )
    k_hnf = knf * (
        (k_n2 + 2 * knf - 2 * phi2*(knf - k_n2)) 
        / 
        (k_n2 + 2 * knf + phi2 * (knf - k_n2))
        )

    return rho_hf, Cp_hf, k_hnf, mu_hf